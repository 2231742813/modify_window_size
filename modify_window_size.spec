# -*- mode: python ; coding: utf-8 -*-

block_cipher = None #加密
a = Analysis(
        # 其他py文件
    ['modify_window_size.py','modify_by_pygetwindows.py','set_log.py'],
    # 项目所在的路径
    pathex=['G:\Pycharm Pro\pythonProject\modify_window_size'],
    binaries=[],
    # 依赖文件所在的路径
    datas=[('./config.yaml','./')],
    # 第三方包
    hiddenimports=[],
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
    [],
    exclude_binaries=True,
    # 打包后程序的名称
    name='Modify_Window',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    # 无黑色控制台
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    # 图标，需要绝对路径
    icon='G:\Pycharm Pro\pythonProject\modify_window_size\\icon7.ico',
)
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    debug=False,
    upx=True,
    upx_exclude=[],
    name='modify_window',
)


