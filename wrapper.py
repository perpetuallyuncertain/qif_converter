import subprocess
import os

if __name__ == "__main__":
     # Get the directory where the executable is located
    base_dir = os.path.dirname(os.path.abspath(__file__))
    # Construct the full path to main.py
    main_path = os.path.join(base_dir, "main.py")
    # Call Streamlit to run the application
    subprocess.run(["streamlit", "run", main_path])
