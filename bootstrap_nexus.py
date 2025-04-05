import os
import subprocess
import sys
import shutil

def run_command(command, shell=False):
    """Helper to run a system command"""
    result = subprocess.run(command, shell=shell)
    if result.returncode != 0:
        print(f"⚠️ Command failed: {command}")
        sys.exit(1)

def bootstrap_nexus():
    print("≡🛠️ Bootstrapping Nexus Core Cleanly...")

    # Step 1: Clear existing virtual environment
    if os.path.exists("venv"):
        print("≡🧹 Deleting old virtual environment...")
        shutil.rmtree("venv")

    # Step 2: Create a new virtual environment
    print("≡⚙️ Creating fresh virtual environment...")
    run_command([sys.executable, "-m", "venv", "venv"])

    # Step 3: Activate virtual environment
    activate_script = os.path.join("venv", "Scripts", "activate") if os.name == "nt" else "source venv/bin/activate"
    print(f"≡🧬 Activating virtual environment ({activate_script})...")
    
    # Step 4: Upgrade pip
    print("≡🚀 Upgrading pip...")
    run_command([os.path.join("venv", "Scripts", "python.exe") if os.name == "nt" else "./venv/bin/python3", "-m", "pip", "install", "--upgrade", "pip"])

    # Step 5: Install dependencies
    if os.path.exists("requirements.txt"):
        print("≡📦 Installing dependencies from requirements.txt...")
        run_command([os.path.join("venv", "Scripts", "pip.exe") if os.name == "nt" else "./venv/bin/pip", "install", "-r", "requirements.txt"])
    else:
        print("⚠️ WARNING: requirements.txt not found, skipping dependency installation.")

    # Step 6: Launch the application
    print("≡🧬 Igniting Nexus Core...")
    python_path = os.path.join("venv", "Scripts", "python.exe") if os.name == "nt" else "./venv/bin/python3"
    run_command([python_path, "-m", "uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8080"])

if __name__ == "__main__":
    bootstrap_nexus()