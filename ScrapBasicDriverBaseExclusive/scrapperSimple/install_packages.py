import subprocess

def install_packages(file_path='requirements.txt'):
    try:
        with open(file_path, 'r') as file:
            packages = file.read().splitlines()
            for package in packages:
                subprocess.run(['pip', 'install', package])
            print("Packages installed successfully.")
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    install_packages()