# imports
import paramiko
import telnetlib

def ssh_login(host, port, username, password):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(host, port=port, username=username, password=password)
        ssh_session = ssh.get_transport().open_session()
        if ssh_session.active:
            print('Login Successful on %s:%s with username: %s and password: %s' % (host, port, username, password))
    except Exception as e:
        return
    ssh.close()

def telnet_login(host, port, username, password):
    user = bytes(username + "\n", 'utf-8')
    password = bytes(password + "\n", 'utf-8')

    try:
        tn = telnetlib.Telnet(host, port)
        tn.read_until(bytes("login: ", "utf-8"))
        tn.write(user)
        tn.read_until(bytes("password: ", "utf-8"))
        tn.write(password)
    except Exception as e:
        print("Telnet is not running")
        return

    try:
        result = tn.expect([bytes("Last Login: ", "utf-8")], timeout=2)
        if result[0] >= 0:
            print("Telnet Login Successful on %s:%s with username: %s and password: %s " % (host, port, username, password))
        tn.close()
    except EOFError:
        print("Telnet Login Failed with username: %s and password: %s" % (username, password))

if __name__ == "__main__":
    host = "126.0.0.1"

    with open("defaults.txt", "r") as f:
        for line in f:
            vals = line.split()
            username = vals[0].strip()
            password = vals[1].strip()
            ssh_login(host, 22, username, password)
            telnet_login(host, 23, username, password)


