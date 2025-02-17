import psutil

SYSTEM_PROCESSES = {"System Idle Process", "System", "svchost.exe", "wininit.exe", "services.exe"}

def is_application_process(process):
    """ Check if a process is a user application (not a system service). """
    try:
        exe_path = process.exe()
        return "Program Files" in exe_path or "Users" in exe_path  # Windows example
    except (psutil.AccessDenied, psutil.NoSuchProcess):
        return False

def is_system_process(process_name, username):
    """ Check if a process is a system process. """
    return process_name in SYSTEM_PROCESSES or username.lower() in {'system', 'root'}
