import yaml
import subprocess


def atomic_file_open():
    file_path = "T1222.002.yaml"

    # Load the YAML file
    with open(file_path, "r") as file:
        atomic_test = yaml.safe_load(file)

    # Print the details of the test
    print("Atomic Test Description:", atomic_test['atomic_tests'][0]['description'])
    print("Executor:", atomic_test['atomic_tests'][0]['executor']['name'])
    print("Command:", atomic_test['atomic_tests'][0]['executor']['command'])

    # Example PowerShell command from the Atomic Test (T1059.001)
    command = atomic_test['atomic_tests'][0]['executor']['command']

    # Execute the command (only if it's safe and tested in a controlled environment)
    result = subprocess.run(command, shell=True, capture_output=True, text=True)

    # Output the result
    print("Command Output:", result.stdout)
    print("Command Error (if any):", result.stderr)

if __name__ == '__main__':
    atomic_file_open()