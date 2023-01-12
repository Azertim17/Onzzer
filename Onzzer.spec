# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(
    ['C:/Users/Tim/source/repos/Azertim17/Onzzer/Onzzer/Onzzer.py'],
    pathex=[],
    binaries=[],
    datas=[('C:/Users/Tim/source/repos/Azertim17/Onzzer/Onzzer/Icones', 'Icones/'), ('C:/Users/Tim/source/repos/Azertim17/Onzzer/Onzzer/request_albums.py', '.'), ('C:/Users/Tim/source/repos/Azertim17/Onzzer/Onzzer/request_artistes.py', '.'), ('C:/Users/Tim/source/repos/Azertim17/Onzzer/Onzzer/request_pistes.py', '.'), ('C:/Users/Tim/source/repos/Azertim17/Onzzer/Onzzer/youtube_search.py', '.')],
    hiddenimports=['json', 'requests', 'PyQt5', 'os', 'sys', 'webbrowser'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='Onzzer',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['C:\\Users\\Tim\\source\\repos\\Azertim17\\Onzzer\\Onzzer\\Icones\\app.ico'],
)
