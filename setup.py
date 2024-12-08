from setuptools import setup

# Define your app entry point and additional files
APP = ['wrapper.py']  # Entry point script
DATA_FILES = ['main.py']  # Any additional files required by your app
OPTIONS = {
    'argv_emulation': True,
    'packages': ['streamlit', 'pandas'],  # Include dependencies
    'frameworks': ['/Library/Frameworks/Python.framework'],  # Include Python framework
    'plist': {
        'CFBundleName': 'Mumma_Converter',
        'CFBundleVersion': '1.0',
        'CFBundleIdentifier': 'com.example.mumma_converter',
        'PyRuntimeLocations': [
            '@executable_path/../Frameworks',
            '/usr/local/Frameworks',
            '/Library/Frameworks',
            '/System/Library/Frameworks',
        ],
    },
}


# Configure the py2app setup
setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
