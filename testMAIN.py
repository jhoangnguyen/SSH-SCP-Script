from paramiko import SSHClient, AutoAddPolicy, AuthenticationException, SSHException, BadHostKeyException

class Client:
    def __init__(self, hostname, port, username, password):
        self.hostname = hostname
        self.port = port
        self.username = username
        self.password = password


    def start(self):
        try:
            client = SSHClient()
            client.load_system_host_keys()
            client.set_missing_host_key_policy(AutoAddPolicy())
            client.connect(self.hostname, port = self.port, username = self.username, password = self.password)


            while True:
                try:
                    cmd = input("$> ")
                    if cmd == "exit" : break
                    stdin, stdout, stderr = client.exec_command(cmd)
                    print(stdout.read().decode())
                except KeyboardInterrupt:
                    break
            client.close()

        except Exception as err:

            print(str(err))




