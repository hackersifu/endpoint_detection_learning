import yaml
import subprocess


def atomic_file_open():
    test_file = open("secret.txt", "w")
    # File path to modify permissions (make sure this file exists)
    file_path = "secret.txt"

    # Display current permissions
    current_permissions = subprocess.run(['ls', '-l', file_path], capture_output=True, text=True)
    print("Current Permissions:", current_permissions.stdout)

    # Command to modify the file permissions (e.g., make the file world-readable and writable)
    command = f"chmod 777 {file_path}"

    # Execute the command
    result = subprocess.run(command, shell=True, capture_output=True, text=True)

    # Output the result of the command execution
    if result.returncode == 0:
        print(f"Permissions for {file_path} successfully modified.")
    else:
        print(f"Failed to modify permissions for {file_path}: {result.stderr}")

    # Display new permissions
    new_permissions = subprocess.run(['ls', '-l', file_path], capture_output=True, text=True)
    print("New Permissions:", new_permissions.stdout)


if __name__ == '__main__':
    atomic_file_open()