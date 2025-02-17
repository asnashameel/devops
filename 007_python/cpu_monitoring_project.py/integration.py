import pytest
import time
import psutil
from unittest.mock import patch, MagicMock
from monitor import monitor_cpu
from email_alerts import send_email
from process_manager import restart_process, kill_process
from utils import is_application_process, is_system_process
from config import CPU_THRESHOLD

@pytest.fixture
def mock_high_cpu_process():
    """Creates a mock process object with high CPU usage."""
    process = MagicMock()
    process.info = {'pid': 4321, 'name': 'chrome.exe', 'username': 'user'}
    process.cpu_percent.return_value = CPU_THRESHOLD + 10  # Simulate high CPU usage
    process.exe.return_value = "C:\\Users\\User\\chrome.exe"
    return process

@patch("psutil.process_iter")
@patch("monitor.send_email")
@patch("monitor.restart_process")
@patch("monitor.kill_process")
def test_monitor_cpu(mock_kill, mock_restart, mock_email, mock_psutil_process_iter, mock_high_cpu_process):
    mock_psutil_process_iter.return_value = [mock_high_cpu_process]

    with patch("time.sleep", return_value=None):  # Prevent delay
        monitor_cpu()

    # Verify the correct action is taken
    if is_system_process(mock_high_cpu_process.info["name"], mock_high_cpu_process.info["username"]):
        mock_email.assert_called_once()
    elif is_application_process(mock_high_cpu_process):
        mock_restart.assert_called_once()
    else:
        mock_kill.assert_called_once()
