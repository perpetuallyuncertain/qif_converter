import sys
import os
import subprocess

# Print debug information
print("Starting the app...")
print("Python executable:", sys.executable)
print("Python version:", sys.version)
print("Python paths:", sys.path)

# Set the working directory
resources_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../Resources")
os.chdir(resources_dir)
print("Working directory set to:", os.getcwd())

# Try running Streamlit
try:
    subprocess.run(["streamlit", "run", "main.py"], check=True)
except Exception as e:
    print("Error starting Streamlit:", e)
    sys.exit(1)
