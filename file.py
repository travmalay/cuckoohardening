#importing os module 
import os

ProofOfSandbox = []

VboxPathsToCheck = [r'C:\windows\System32\drivers\Vmmouse.sys', r'C:\Windows\System32\drivers\VBoxGuest.sys',
r'C:\windows\System32\drivers\vm3dgl.dll', r'C:\windows\System32\drivers\vmdum.dll', 
r'C:\windows\System32\drivers\vm3dver.dll', r'C:\windows\System32\drivers\vmtray.dll',
r'C:\windows\System32\drivers\vmci.sys', r'C:\windows\System32\drivers\vmusbmouse.sys',
r'C:\windows\System32\drivers\vmx_svga.sys', r'C:\windows\System32\drivers\vmxnet.sys',
r'C:\windows\System32\drivers\VMToolsHook.dll', r'C:\windows\System32\drivers\vmhgfs.dll',
r'C:\windows\System32\drivers\vmmousever.dll', r'C:\windows\System32\drivers\vmGuestLib.dll',
r'C:\windows\System32\drivers\VmGuestLibJava.dll', r'C:\windows\System32\drivers\vmscsi.sys',
r'C:\windows\System32\drivers\VBoxMouse.sys', r'C:\windows\System32\drivers\VBoxGuest.sys',
r'C:\windows\System32\drivers\VBoxSF.sys', r'C:\windows\System32\drivers\VBoxVideo.sys',
r'C:\windows\System32\vboxdisp.dll', r'C:\windows\System32\vboxhook.dll',
r'C:\windows\System32\vboxmrxnp.dll', r'C:\windows\System32\vboxogl.dll',
r'C:\windows\System32\vboxoglarrayspu.dll', r'C:\windows\System32\vboxoglcrutil.dll',
r'C:\windows\System32\vboxoglerrorspu.dll', r'C:\windows\System32\vboxoglfeedbackspu.dll',
r'C:\windows\System32\vboxoglpackspu.dll', r'C:\windows\System32\vboxoglpassthroughspu.dll',
r'C:\windows\System32\vboxservice.exe', r'C:\windows\System32\vboxtray.exe',
r'C:\windows\System32\VBoxControl.exe']
#for loop to check those path once for each time
for FilePath in VboxPathsToCheck:
# reason to use os.path.isfile() method is to check whether the specific path is an existing file
	if os.path.isfile(FilePath):
    #if any file exists then added those files via append method
		ProofOfSandbox.append(FilePath)

if ProofOfSandbox:
	print("Vbox file exists. Do not proceed.\n{0}".format(ProofOfSandbox))
else:
	print("Vbox file does not exist. Proceed!")