import subprocess
import os

if __name__ == "__main__":
      # Determine the base directory of the executable
    base_dir = os.path.dirname(os.path.abspath(__file__))

    # Path to main.py
    main_path = os.path.join(base_dir, "main.py")
    print(f"Looking for main.py at: {main_path}")

    # Call Streamlit to run the application
    if os.path.exists(main_path):
        subprocess.run(["streamlit", "run", main_path])
    else:
        print(f"Error: main.py not found at {main_path}")
