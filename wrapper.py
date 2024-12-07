import os
import subprocess
import sys

# Locate the PyInstaller temporary folder
current_dir = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))

# Build the path to streamlit in the extracted folder
streamlit_path = os.path.join(current_dir, 'streamlit')

# Ensure streamlit exists in the bundled files
if not os.path.exists(streamlit_path):
    print(f"Error: Streamlit not found at: {streamlit_path}")
    sys.exit(1)

# Path to main.py
main_py_path = os.path.join(current_dir, 'main.py')

# Ensure main.py exists
if not os.path.exists(main_py_path):
    print(f"Error: main.py not found at: {main_py_path}")
    sys.exit(1)

# Execute Streamlit
try:
    subprocess.run([streamlit_path, "run", main_py_path])
except Exception as e:
    print(f"Error running Streamlit: {e}")
    sys.exit(1)
