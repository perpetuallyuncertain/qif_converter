from setuptools import setup

# Define your app entry point and additional files
APP = ['wrapper.py']  # Entry point script
DATA_FILES = ['main.py']  # Any additional files required by your app
OPTIONS = {
    'argv_emulation': True,  # Ensure command-line arguments are handled correctly
    'packages': ['streamlit', 'pandas'],  # Include dependencies
    'plist': {  # macOS-specific metadata
        'CFBundleName': 'Mumma_Converter',
        'CFBundleVersion': '1.0',
        'CFBundleIdentifier': 'com.example.mumma_converter',
    },
}

# Configure the py2app setup
setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
