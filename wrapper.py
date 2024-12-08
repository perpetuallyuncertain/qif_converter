#!/usr/bin/env python

import os
import sys

# Adjust paths to use the app's bundled Python framework
sys.executable = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "python"
)
os.environ["PYTHONHOME"] = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "../Frameworks/Python.framework/Versions/Current"
)
os.environ["PYTHONPATH"] = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "../Resources/lib/python3.9"
)

# Execute the main app script using Streamlit
if __name__ == "__main__":
    os.execv(sys.executable, [sys.executable, "-m", "streamlit", "run", "main.py"])
