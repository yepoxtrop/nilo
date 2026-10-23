# -*- mode: python ; coding: utf-8 -*-

from pathlib import Path

project_root = Path(SPECPATH)
media_path = project_root / "src" / "frontend" / "media"
message_scripts_path = project_root / "src" / "backend" / "utils" / "message-error"
camera_tools_path = project_root / "src" / "backend" / "utils" / "take-phtoto"

a = Analysis(
    [str(project_root / "Raven.py")],
    pathex=[str(project_root)],
    binaries=[],
    datas=[
        (str(media_path), "src/frontend/media"),
        (str(message_scripts_path), "src/backend/utils/message-error"),
        (str(camera_tools_path), "src/backend/utils/take-phtoto"),
    ],
    hiddenimports=[],
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
    a.binaries,
    a.datas,
    [],
    name='Raven',
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
    icon=['src/frontend/media/icon.ico'],
)
