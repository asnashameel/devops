# process_manager.py
import os
import time
import psutil

def restart_process(process_pid, process_name):
    """ Kills and restarts a process if it's an application. """
    try:
        os.system(f"taskkill /F /PID {process_pid}")  # Force kill process
        time.sleep(2)  # Wait before restarting

        # Restart only if it's a user application
        if not process_name.lower().startswith("system"):
            os.system(f"start {process_name}")  
            print(f"Successfully restarted {process_name}.")
    except Exception as e:
        print(f"Error restarting {process_name}: {e}")

def kill_process(process_pid, process_name):
    """ Terminates a process. """
    try:
        psutil.Process(process_pid).terminate()
        print(f"Process '{process_name}' (PID: {process_pid}) terminated.")
    except Exception as e:
        print(f"Failed to terminate {process_name}: {e}")
