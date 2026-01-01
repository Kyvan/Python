#!/home/kyvan/python_env/bin/python

import subprocess
import sys

def install_dependencies():
    """Installs packages listed in requirements.txt."""
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("All dependencies installed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error installing dependencies: {e}")
        sys.exit(1)

if __name__ == "__main__":
    install_dependencies()
