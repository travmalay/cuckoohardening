# Windows registry access/ (Windows Registry API) provides functions to expose the Windows registry API to Python
from _winreg import *
import os

browserNumber = 0

browserKeys = [r'SOFTWARE\Microsoft\Windows\CurrentVersion\App Paths\chrome.exe', r'SOFTWARE\Microsoft\Windows\CurrentVersion\App Paths\iexplore.exe', r'SOFTWARE\Mozilla']

#connecting to key in registry
REG = ConnectRegistry(None,HKEY_LOCAL_MACHINE)

for browserKey in browserKeys:
	try:
		Opened_Key = OpenKey(REG, browserKey)
		browserNumber += 1
	except:
		pass 

if browserCount >= 2:
	print("Proceed!")
else:
	print("Number of Browsers: " + str(browserNumber))
