# -*- mode: python ; coding: utf-8 -*-
from PyInstaller.building.api import PYZ, EXE, COLLECT
from PyInstaller.building.build_main import Analysis

block_cipher = None

# Analisa os scripts python que é usado e suas dependências
a = Analysis(['main.py'], # lista de scripts especificados como nomes de arquivos
             pathex=\
['D:\\GitHub\\PythonCourseUdemy\\kivy\\aulas\\Seção 27 - Empacotamento\\04 - Empacotando com pyinstaller'],
             # lista opcional de paths a sererm pesquisados antes do sys.path
             binaries=[], # lista opcional de binários adicionais a serem incluídos
             datas=[], # uma lista opcional de arquivos adicionais a serem inclusos
             hiddenimports=[], # lista opcional de módulos ocultos a serem adicionados
             hookspath=[], # list opcional de paths para buscar hooks
             runtime_hooks=[], # list a opcional de descripts par uso como hook em execução
             excludes=[], # lista opcional de módulos que serão ignorados no empacotamento
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
# cria uma ZlibArchive que contém todos módulos Python puros
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

# cria o executável final do aplicativo
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='main',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True )

# cria a pasta de saída com todos arquivos necessários
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='main')
