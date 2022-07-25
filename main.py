#Develop a python script for SSH/SCP
# Install Python 3
# Follow the PEP 8 for formatting your script
# Develop the SSH/SCP script
# Implement GUI for it (tkinter) (as time permit)
    # User Window
    # Terminal window (interactive)
    # Similar to PuTTY, but for the NI TestStand

from multiprocessing import AuthenticationError
from paramiko import SSHClient, AutoAddPolicy, AuthenticationException, SSHException, BadHostKeyException
from rich import print, pretty, inspect

pretty.install()
#Login through host keys



#Login by user

def parse():
    host = "sample" #find current ip address
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    return host, username, password

def login(host, port, username, password):
    client = SSHClient()
    
    # load existing keys 
    client.load_system_host_keys()


    # Known_host policy
    client.set_missing_host_key_policy(AutoAddPolicy())


    # client.connect('IP', username='root', password='password')
    client.connect(host, port=port, username=username, password=password)
    return client

def invoke_shell(client):
    channel = client.get_transport().open_session()


def execute(client, cmd):
    if cmd == "temp":
        pass
    else:
        stdin, stdout, stderr = client.exec_command(cmd)
        cmd_output = stdout.read()



if __name__ == '__main__':
    _stdin, _stdout, _stderr = None
    host, username, password = parse()
    port = 22
    client = login(host, port, username, password)
    invoke_shell(client)
    cmd = "temp"
    while cmd != "exit":
        # command = input("Enter a command: ")
        # _stdin, _stdout, _stderr = client.exec_command(command)
        # print(_stdout)
        # print(_stderr)

    
    if command == "exit":
        _stdin.close()
        _stdout.close()
        _stderr.close()




        





