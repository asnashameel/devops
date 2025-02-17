import pytest
import psutil
from unittest.mock import patch, MagicMock
from email_alerts import send_email
from process_manager import restart_process, kill_process
from utils import is_application_process, is_system_process
from config import SYSTEM_PROCESSES

@pytest.fixture
def mock_process():
    """Creates a mock process object."""
    process = MagicMock()
    process.info = {'pid': 1234, 'name': 'test_app.exe', 'username': 'user'}
    process.exe.return_value = "C:\\Program Files\\test_app.exe"
    return process

#  Test Email Sending
@patch("smtplib.SMTP")
def test_send_email(mock_smtp):
    send_email("test_process", 1234, 80.5)
    mock_smtp.assert_called_once()

#  Test Restart Process
@patch("os.system")
def test_restart_process(mock_os_system):
    restart_process(1234, "test_app.exe")
    assert mock_os_system.call_count == 2  # Should call `taskkill` and `start`

#  Test Kill Process
@patch("psutil.Process")
def test_kill_process(mock_psutil_process):
    mock_proc = MagicMock()
    mock_psutil_process.return_value = mock_proc

    kill_process(1234, "test_app.exe")
    mock_proc.terminate.assert_called_once()

#  Test System Process Detection
def test_is_system_process():
    assert is_system_process("System", "system") is True
    assert is_system_process("notepad.exe", "user") is False

# Test Application Process Detection
def test_is_application_process(mock_process):
    assert is_application_process(mock_process) is True
