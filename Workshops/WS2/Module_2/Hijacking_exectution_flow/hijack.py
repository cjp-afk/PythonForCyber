import os, winreg

def read_path_value(reghive, regpath):
    reg = winreg.ConnectRegistry(None, reghive)
    key = winreg.OpenKey(reg, regpath, 0, access=winreg.KEY_READ)
    index = 0
    while True:
        val = winreg.EnumValue(key, index)
        if val[0] == "Path":
            return val[1]
        index = index + 1

def edit_path_value(reghive, regpath, targetdir):
    path = read_path_value(reghive, regpath)
    newpath =  targetdir + ";" + path

    reg = winreg.ConnectRegistry(None, reghive)
    key = winreg.OpenKey(reg, regpath, 0, access=winreg.KEY_SET_VALUE)
    winreg.SetValueEx(key, "Path", 0, winreg.REG_SZ, newpath)

if __name__ == "__main__":
    reghive = winreg.HKEY_CURRENT_USER
    regpath = "Environment"
    targetdir = os.getcwd()

    edit_path_value(reghive, regpath, targetdir)