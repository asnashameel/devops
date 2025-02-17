# cpu_monitor.py
import time
import psutil
from email_alerts import send_email
from process_manager import restart_process, kill_process
from utils import is_application_process, is_system_process
from config import CPU_THRESHOLD

def monitor_cpu():
    while True:
        for process in psutil.process_iter(['pid', 'name', 'cpu_percent', 'username']):
            try:
                process_pid = process.info['pid']
                process_name = process.info['name']
                username = process.info.get('username', 'Unknown')

                # Get fresh CPU usage
                cpu_usage = process.cpu_percent(interval=1) / psutil.cpu_count()

                if cpu_usage > CPU_THRESHOLD:
                    print(f"High CPU Usage: {process_name} (PID: {process_pid}) using {cpu_usage:.2f}% CPU")

                    # System Process → Send Email
                    if is_system_process(process_name, username):
                        print(f"Sending email alert for system process: {process_name} (PID: {process_pid})")
                        send_email(process_name, process_pid, cpu_usage)
                    
                    # Application Process → Restart
                    elif is_application_process(process):
                        print(f"Restarting application process: {process_name} (PID: {process_pid})")
                        restart_process(process_pid, process_name)
                    
                    # Other Processes → Kill
                    else:
                        print(f"Killing high CPU process: {process_name} (PID: {process_pid})")
                        kill_process(process_pid, process_name)

            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess) as e:
                print(f"Error: {e} - Skipping process.")
                continue

        time.sleep(5)

if __name__ == "__main__":
    monitor_cpu()