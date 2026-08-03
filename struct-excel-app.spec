# -*- mode: python ; coding: utf-8 -*-
from PyInstaller.utils.hooks import collect_all, copy_metadata

datas = []
binaries = []
hiddenimports = []

for pkg in (
    "streamlit",
    "sqlmodel",
    "sqlalchemy",
    "pycountry",
    "altair",
    "pyarrow",
    "pandas",
    "openpyxl",
    "phonenumbers",
    "pydantic",
):
    d, b, h = collect_all(pkg)
    datas += d
    binaries += b
    hiddenimports += h

hiddenimports += [
    "struct_excel",
    "struct_excel.app",
    "struct_excel.database",
    "struct_excel.excel",
    "struct_excel.models",
    "struct_excel.normalization",
    "struct_excel.parser",
    "struct_excel.reader",
    "struct_excel.report",
    "struct_excel.transform",
]

for meta in (
    "streamlit",
    "altair",
    "pandas",
    "pyarrow",
    "sqlmodel",
    "sqlalchemy",
    "pydantic",
):
    datas += copy_metadata(meta)

datas += [("struct_excel/app.py", "struct_excel")]

a = Analysis(
    ["run_app.py"],
    pathex=["."],
    binaries=binaries,
    datas=datas,
    hiddenimports=hiddenimports,
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
    name="struct-excel",
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
