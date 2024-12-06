# -*- mode: python ; coding: utf-8 -*-

import platform

# Dynamically set the path to the streamlit binary based on the platform
if platform.system() == 'Darwin':  # macOS
    streamlit_binary = ('venv/bin/streamlit', 'streamlit')
elif platform.system() == 'Windows':  # Windows
    streamlit_binary = ('.venv/Scripts/streamlit.exe', 'streamlit')
else:
    raise ValueError("Unsupported platform: Update wrapper.spec for other platforms.")

a = Analysis(
    ['wrapper.py'],
    pathex=[],
    binaries=[
    streamlit_binary,  # Dynamically set Streamlit binary path
    ("/Library/Frameworks/Python.framework/Versions/3.9", "python.framework/Versions/3.9")  # Full Python framework
    ],
    datas=[
        ('main.py', '.')  # Include main.py
    ],
    hiddenimports=[
        'streamlit'  # Ensure Streamlit is included as a hidden import
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)

pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='wrapper',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='wrapper'
)
