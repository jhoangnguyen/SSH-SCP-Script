from subprocess import Popen, PIPE
from threading import Thread, Lock
import tkinter as tk
from paramiko import SSHClient, AutoAddPolicy, AuthenticationException, SSHException, BadHostKeyException

class Client:
    def __init__(self, hostname, port, username, password):
        self.hostname = hostname
        self.port = port
        self.username = username
        self.password = password
        self.command = None


    def start(self):
        try:
            client = SSHClient()
            client.load_system_host_keys()
            client.set_missing_host_key_policy(AutoAddPolicy())
            client.connect(self.hostname, port = self.port, username = self.username, password = self.password)


            while True:
                try:
                    cmd = input("$> ")
                    self.command = cmd
                    if cmd == "exit" : break
                    stdin, stdout, stderr = client.exec_command(cmd)
                    print(stdout.read().decode())
                except KeyboardInterrupt:
                    break
            client.close()

        except Exception as err:

            print(str(err))



class TkinterPopen(tk.Text):
    def __init__(self, master, state="disabled", **kwargs):
        super().__init__(master, state=state, **kwargs)
        self.commands = []
        self.proc = None
        self.running = True
        self.stdout_buffer = ""
        self.stdout_buffer_lock = Lock()

    def stdout_loop(self, last_loop:bool=False) -> None:
        with self.stdout_buffer_lock:
            # Get the data and clear the buffer:
            data, self.stdout_buffer = self.stdout_buffer, ""
        state = super().cget("state")
        super().config(state="normal")
        super().insert("end", data)
        super().see("end")
        super().config(state=state)
        if self.proc is None:
            if len(self.commands) == 0:
                # If we are done with all of the commands:
                if last_loop:
                    return None
                super().after(100, self.stdout_loop, True)
            else:
                # If we have more commands to do call `start_next_proc`
                self.start_next_proc()
        else:
            super().after(100, self.stdout_loop)

    def start_next_proc(self) -> None:
        command = self.commands.pop(0) # Take the first one from the list
        self.proc = Popen(command, stdout=PIPE)
        new_thread = Thread(target=self.read_stdout, daemon=True)
        new_thread.start()
        self.stdout_loop()

    def run_commands(self, commands:list) -> None:
        self.commands = commands
        self.start_next_proc()

    def read_stdout(self):
        while self.proc.poll() is None:
            self._read_stdout()
        self._read_stdout()
        self.proc = None

    def _read_stdout(self) -> None:
        line = self.proc.stdout.readline()
        with self.stdout_buffer_lock:
            self.stdout_buffer += line.decode()


if __name__ == "__main__":
    def start_echo():
        command = ["echo", "hi"]
        tkinter_popen.run_commands([command])

    def start_ping():
        # For linux use "-c". For windows use "-n"
        command = ["ping", "1.1.1.1", "-n", "3"]
        tkinter_popen.run_commands([command])

    def start_write():
        client = Client("iron27", "22", "johnson.nguyen", "JHN@lolpower12")
        command = [client.command]
        tkinter_popen.run_commands([command])
    root = tk.Tk()

    tkinter_popen = TkinterPopen(root)
    tkinter_popen.pack()

    button = tk.Button(root, text="Run echo", command=start_echo)
    button.pack()

    button = tk.Button(root, text="Run ping", command=start_ping)
    button.pack()

    root.mainloop()