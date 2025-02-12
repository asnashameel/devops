import os
import subprocess
import sys

VENV_DIR = "newenv"

def create_virtual_env():
    """Create a virtual environment if it doesn't exist."""
    if not os.path.exists(VENV_DIR):
        print("Creating virtual environment...")
        subprocess.run([sys.executable, "-m", "venv", VENV_DIR])
    else:
        print("Virtual environment already exists.")

def install_requirements():
    """Install required packages from requirements.txt if the file exists."""
    requirements_file = "requirements.txt"
    if os.path.exists(requirements_file):
        print("Installing dependencies...")
        subprocess.run([os.path.join(VENV_DIR, "Scripts", "pip"), "install", "-r", requirements_file], shell=True)
    else:
        print("No requirements.txt found. Skipping dependency installation.")

def activate_and_run():
    """Activate the virtual environment and run the app."""
    print("Starting the application...")

    # Determine the correct activation command and execution method based on OS
    if os.name == "nt":  # Windows
        python_executable = os.path.join(VENV_DIR, "Scripts", "python.exe")
    else:  # macOS/Linux
        python_executable = os.path.join(VENV_DIR, "bin", "python")

    # Run the application (app.py)
    subprocess.run([python_executable, "app.py"], shell=True)

if __name__ == "__main__":
    create_virtual_env()
    install_requirements()
    activate_and_run()
