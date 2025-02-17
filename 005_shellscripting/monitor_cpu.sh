#!/bin/bash

CPU_THRESHOLD=60  # Set CPU usage threshold
EMAIL_RECEIVER="muhdshameeln@gmail.com"
SYSTEM_PROCESSES=("systemd" "init" "kthreadd" "rcu_sched" "kworker" "watchdog" "kswapd" "systemd-journald")

# Function to send an email alert for system processes
send_email() {
    local process_name=$1
    local process_pid=$2
    local cpu_usage=$3

    subject="High CPU Usage Alert: System Process"
    body="System process '$process_name' (PID: $process_pid) is consuming $cpu_usage% CPU."

    echo "$body" | mail -s "$subject" "$EMAIL_RECEIVER"
    echo "Email sent for system process: $process_name (PID: $process_pid) using $cpu_usage% CPU."
}

# Function to restart an application process
restart_process() {
    local process_pid=$1
    local process_name=$2

    kill -9 "$process_pid"
    sleep 2

    nohup "$process_name" &>/dev/null &
    echo "Restarted: $process_name (PID: $process_pid)"
}

# Function to check if a process is an application
is_application_process() {
    local exe_path
    exe_path=$(readlink -f "/proc/$1/exe" 2>/dev/null)
    
    [[ "$exe_path" == *"/usr/bin/"* || "$exe_path" == *"/usr/local/bin/"* ]]
}

# Monitor CPU usage
while true; do
    ps aux | awk 'NR>1 {print $2, $11, $3}' | while read -r process_pid process_name cpu_usage; do
        cpu_usage=${cpu_usage%.*}  # Convert float to integer

        if [ "$cpu_usage" -gt "$CPU_THRESHOLD" ]; then
            echo "High CPU Usage: $process_name (PID: $process_pid) using $cpu_usage% CPU"

            # Check if it's a system process
            if [[ " ${SYSTEM_PROCESSES[*]} " =~ " $process_name " ]]; then
                send_email "$process_name" "$process_pid" "$cpu_usage"

            # Check if it's an application process
            elif is_application_process "$process_pid"; then
                restart_process "$process_pid" "$process_name"

            # If neither, just kill the process
            else
                kill -9 "$process_pid"
                echo "Killed process: $process_name (PID: $process_pid)"
            fi
        fi
    done

    sleep 5  # Wait for 5 seconds before checking again
done
