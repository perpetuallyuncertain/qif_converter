import subprocess
import sys

if __name__ == "__main__":
    # Call Streamlit to run the application
    subprocess.run(["streamlit", "run", "main.py"] + sys.argv[1:])
