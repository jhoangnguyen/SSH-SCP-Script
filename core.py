from multiprocessing import AuthenticationError
from paramiko import SSHClient, AutoAddPolicy, AuthenticationException, SSHException, BadHostKeyException
from tkinter import *
from openpyxl.styles.borders import Side
from rich import print, pretty, inspect
import sys
import time
import threading
import subprocess
import core_gui


def parse():
    host = "iron27"
    # username = input("Enter your username: ")
    # password = input("Enter your password: ")
    username = "johnson.nguyen"
    password = "JHN@lolpower12"
    return [host, username, password]


def group_parse(client_num):
    print("Please input the following login details for each client.")
    accounts = []
    for _ in range(int(client_num)):
        host = input("Host: ")
        username = input("Username: ")
        password = input("Password: ")
        accounts.append([host, username, password])
    return accounts
# The Login-Execute functions below are used exclusively for sequential commands, with further functionality
# to be added.

# def login(host, port, username, password):
    
#     # client = SSHClient()
    
#     # # Load existing keys 
#     # client.load_system_host_keys()


#     # # Known_host policy
#     # client.set_missing_host_key_policy(AutoAddPolicy())


#     # # client.connect('IP', username='root', password='password')
#     # client.connect(host, port=port, username=username, password=password)
#     # print("Login successful")
#     # return client
#     i = 0
#     while True:
#         try:
#             client = SSHClient()
            
#             # Load existing keys 
#             client.load_system_host_keys()


#             # Known_host policy
#             client.set_missing_host_key_policy(AutoAddPolicy())


#             # client.connect('IP', username='root', password='password')
#             client.connect(host, port=port, username=username, password=password)
#             break
#         except AuthenticationException:
#             print("Authentication failed when connecting to %s" % host)
#             sys.exit(1)
#         except:
#             print("Could not SSH to %s, waiting for it to start" % host)
#             i += 1
#             time.sleep(2)
        
#     if i >= 5:
#         print("Could not connect to %s. Giving up" % host)
#         sys.exit(1)

#     return client

def login(fields, root):

    text = []

    for entry in fields:
        text.append(entry[1].get())
    
    i = 0
    while True:
        try:
            client = SSHClient()
            
            # Load existing keys 
            client.load_system_host_keys()


            # Known_host policy
            client.set_missing_host_key_policy(AutoAddPolicy())


            # client.connect('IP', username='root', password='password')
            client.connect(text[0], port=22, username=text[1], password=text[2])
            break
        except AuthenticationException:
            print("Authentication failed when connecting to %s" % text[0])
            sys.exit(1)
        except:
            print("Could not SSH to %s, waiting for it to start" % text[0])
            i += 1
            time.sleep(2)
            if i >= 5:
                print("Could not connect to %s. Giving up" % text[0])
                sys.exit(1)

    return client

def execute(client, cmd):
    if cmd == "temp":
        pass
    try:
        stdin, stdout, stderr = client.exec_command(cmd)
        cmd_output = stdout.read()
        print(cmd_output.decode())
    finally:
        client.close()


# This function is used exclusively for batch commands, as paramiko does not support
# persisting clients across threads. Hard-coded retry attempts of 5 upon failure.

def group_execute(host, port, username, password, cmd, thread_num):
    i = 0
    while True:
        try:
            client = SSHClient()
            
            # Load existing keys 
            client.load_system_host_keys()


            # Known_host policy
            client.set_missing_host_key_policy(AutoAddPolicy())


            # client.connect('IP', username='root', password='password')
            client.connect(host, port=port, username=username, password=password)
            break
        except AuthenticationException:
            print("Authentication failed when connecting to %s" % host)
            sys.exit(1)
        except:
            print("Could not SSH to %s, waiting for it to start" % host)
            i += 1
            time.sleep(2)
        
    if i >= 5:
        print("Could not connect to %s. Giving up" % host)
        sys.exit(1)
    

    try:
        stdin, stdout, stderr = client.exec_command(cmd)
        cmd_output = stdout.read()
        
        print("Thread " + str(thread_num) + "'s output:")
        print(cmd_output.decode())
    finally:
        client.close()


# Multithreading function with a hard coded limit of five threads. Any
# additional threads will require a thread pool architecture.
def initializeThreads(accounts, repeat, client_num, cmd):
    outlock = threading.Lock()
    # hosts = [1, 2]
    # loginDetails = ["user", "password"]
    threads = []
    print(accounts)
    if repeat == True:
        for index in range(int(client_num)):
            t = threading.Thread(target=group_execute, args=(accounts[0], 22, accounts[1], accounts[2], "ls /shared/gitrepo/johnson.nguyen/", index))
            t.start()
            print("Thread " + str(index) + " is starting!")
            threads.append(t)
            if len(threads) > 5:
                break
        for t in threads:
            t.join()
    else:
        for index, account in enumerate(accounts):
            t = threading.Thread(target=group_execute, args=(account[0], 22, account[1], account[2], "ls /shared/gitrepo/johnson.nguyen/", index))
            t.start()
            print("Thread " + str(index) + " is starting!" + " Machine " + account[0])
            threads.append(t)
            if len(threads) > 5:
                break
        for t in threads:
            t.join()
    return threads

# def invoke_shell():
#     subprocess.call(["ssh", "johnson.nguyen@iron27"])

def makeform(root, fields):
    entries = []
    for field in fields:
        row = Frame(root)
        lab = Label(row, width=15, text=field, anchor='w')
        ent = Entry(row)
        row.pack(side=TOP, fill=X, padx=5, pady=5)
        lab.pack(side=LEFT)
        ent.pack(side=LEFT, expand=NO, fill=X)
        entries.append((field, ent))
    la = Label(root, width=15, text="Output :", anchor='w')
    la.pack(side=LEFT)
    return entries


# REFACTORED VERSION TO INCLUDE A GUI
if __name__ == '__main__':
    fields = 'Host :','Username :', 'Password :', 'Command :', 'Single Client? (Y/N) :'
    root = Tk()
    root.title("SSH Login Application")
    ents = makeform(root, fields)
    root.bind('<Return>', (lambda event, e=ents: login(e))) 
    b1 = Button(root, text='Login',command=(lambda e=ents:login(e, root)))
    b1.pack(side=LEFT, padx=5, pady=5)
    b2 = Button(root, text='Quit', command=root.quit)
    b2.pack(side=LEFT, padx=5, pady=5)
    root.mainloop()


# PURE CMD OUTPUT, DOES NOT INCLUDE GUI
# if __name__ == '__main__':
    
#     threadCheck = input("Input a number below. \n1: Single client, single-thread  \n2: Multiple clients, multi-thread batch output \n")
#     while True:
#         if threadCheck == "1":
#             account = parse()
#             port = 22
#             client = login(account[0], port, account[1], account[2])
#             execute(client, "ls /shared/gitrepo/johnson.nguyen/")
#             break
#         elif threadCheck == "2":
#             client_num = input("How many clients are needed? (Note: Maximum number of clients is 5.) \n")
#             repeat = bool(input("Will all clients run under the same user? Press enter if No."))
#             command = input("Input scripts into single line format: (Logical linux operators include ;, &&, and ||. \nA sample sequential operation is 'cd /shared/gitrepo && python sample.py')")
#             if repeat == False:
#                 accounts = group_parse(client_num)
#                 port = 22
#                 threads = initializeThreads(accounts, repeat, client_num, command)
#                 break
#             else:
#                 account = parse()
#                 port = 22
#                 threads = initializeThreads(account, repeat, client_num, command)
#                 break
#         else:
#             print("Invalid response. Please try again.")
#             threadCheck = input("1: Single client, single-thread \n2: Multiple clients, multi-thread batch output \n")

