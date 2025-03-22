# FiveM Balanced Settings launcher
# by fahmiyufrizal@2025

import xml.etree.ElementTree as ET
import subprocess
import os
from os import path
import sys
from sys import exit
import time
import pathlib
import ctypes

# parameters
version = 'v1.0'
titlewindow = 'fahmiyufrizal@2025 [github.com/fahmiyufrizal]'
WWFN = (r'Launch_FiveM_Balanced.exe')
dp0 = os.getcwd()

def prepare_folder():
	km00 = 'ÿþ'
	km1 = '@echo off\n'
	km2 = 'rd /s /q "%Appdata%\CitizenFX"'
	km3 = 'mklink /J "%Appdata%\CitizenFX" "%~dp0CitizenFX"'
	
	symlink = open(r'symlink.bat','w+')
	symlink.writelines([km00,km1 + "\n",km2 + "\n",km3 + "\n"])
	symlink.close()
	subprocess.call([r'symlink.bat'], stdout=subprocess.DEVNULL,
		stderr=subprocess.STDOUT)
	os.remove('symlink.bat')

#blocked eheheh
run_fivem()
