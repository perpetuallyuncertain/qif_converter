from setuptools import setup

# Define your app entry point and additional files
APP = ['wrapper.py']  # Entry point script
DATA_FILES = ['main.py']  # Any additional files required by your app
OPTIONS = {
    'argv_emulation': True,  # Ensure command-line arguments are handled correctly
    'packages': ['streamlit', 'pandas', 'numpy', 'altair', 'pydeck'],  # Include key dependencies
    'includes': ['tornado', 'certifi', 'pyarrow', 'pytz'],  # Additional dependencies
    'excludes': ['tkinter', 'test'],  # Exclude unnecessary modules
    'plist': {  # macOS-specific metadata
        'CFBundleName': 'Mumma_Converter',
        'CFBundleVersion': '1.0',
        'CFBundleIdentifier': 'com.example.mumma_converter',
        'PyRuntimeLocations': [
            '@executable_path/../Frameworks',  # Preferred location within the app bundle
            '/usr/local/Frameworks',          # Fallback to globally installed Python frameworks
            '/Library/Frameworks',
            '/System/Library/Frameworks',     # Fallback to system frameworks
        ],
    },
    'frameworks': ['/Library/Frameworks/Python.framework'],  # Explicitly include Python framework
}

# Configure the py2app setup
setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
