import os
import subprocess
import sys

class CyberPath:
    def __init__(self):
        self.check_admin_privileges()

    def check_admin_privileges(self):
        try:
            is_admin = os.getuid() == 0
        except AttributeError:
            is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0

        if not is_admin:
            print("Please run this program as an administrator.")
            sys.exit(1)

    def check_for_updates(self):
        print("Checking for updates...")
        try:
            result = subprocess.run(
                ['powershell', '-Command', 'Get-WindowsUpdate'],
                capture_output=True,
                text=True
            )
            if result.returncode == 0:
                print("Updates available:\n", result.stdout)
            else:
                print("Failed to check for updates:\n", result.stderr)
        except Exception as e:
            print(f"An error occurred while checking for updates: {e}")

    def install_updates(self):
        print("Installing updates...")
        try:
            result = subprocess.run(
                ['powershell', '-Command', 'Install-WindowsUpdate', '-AcceptAll', '-AutoReboot'],
                capture_output=True,
                text=True
            )
            if result.returncode == 0:
                print("Updates installed successfully:\n", result.stdout)
            else:
                print("Failed to install updates:\n", result.stderr)
        except Exception as e:
            print(f"An error occurred while installing updates: {e}")

if __name__ == "__main__":
    cyber_path = CyberPath()
    cyber_path.check_for_updates()
    user_input = input("Do you want to install these updates? (y/n): ")
    if user_input.lower() == 'y':
        cyber_path.install_updates()