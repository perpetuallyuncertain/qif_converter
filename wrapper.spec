# -*- mode: python ; coding: utf-8 -*-

import platform

# Dynamically set the path to the Streamlit binary based on the platform
if platform.system() == 'Darwin':  # macOS
    streamlit_binary = ('venv/bin/streamlit', 'streamlit')
elif platform.system() == 'Windows':  # Windows
    streamlit_binary = ('.venv/Scripts/streamlit.exe', 'streamlit')
else:
    raise ValueError("Unsupported platform: Update wrapper.spec for other platforms.")

a = Analysis(
    ['wrapper.py'],  # Main script to analyze
    pathex=[],  # Additional paths to include in the search
    binaries=[streamlit_binary],
    datas=[
        ('main.py', '.')  # Include main.py in the root of the bundle
    ],
    hiddenimports=[
        'streamlit'  # Ensure Streamlit is included as a hidden import
    ],
    hookspath=[],  # Paths to custom hooks
    hooksconfig={},  # Optional hook configuration
    runtime_hooks=[],  # Hooks to execute at runtime
    excludes=[],  # Modules to exclude
    noarchive=False,  # Do not bundle everything in a single archive
    optimize=0,  # Optimization level
)

pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],  # Additional options
    exclude_binaries=True,  # Exclude binaries (handled by COLLECT)
    name='converter',  # Name of the output executable
    debug=False,  # Disable debug mode
    bootloader_ignore_signals=False,
    strip=False,  # Do not strip binaries
    upx=True,  # Enable UPX compression
    upx_exclude=[],  # Exclude specific files from UPX compression
    runtime_tmpdir=None,  # Temporary directory for runtime files
    console=True,  # Enable console output
    disable_windowed_traceback=False,
    argv_emulation=False,  # Disable argv emulation (used for macOS apps)
    target_arch=None,  # Target architecture (optional)
    codesign_identity=None,  # Code signing identity (optional)
    entitlements_file=None,  # Entitlements for macOS code signing (optional)
)

coll = COLLECT(
    exe,
    a.binaries,  # Include binaries
    a.zipfiles,  # Include Python libraries as zip
    a.datas,  # Include data files
    strip=False,
    upx=True,
    upx_exclude=[],  # Exclude specific files from UPX compression
    name='mumma_converter'  # Output folder name
)
