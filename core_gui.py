from re import S, T
import tkinter as tk
from tkinter import ttk
from tkinter import Text
from tkinter import END
from tkinter.messagebox import showerror
from threading import Thread
from tkinter import filedialog
import sys
from itertools import islice
from subprocess import Popen, PIPE, run
from textwrap import dedent
import core
import os

try:
    import tkinter as tk
    from queue import Queue, Empty
except ImportError:
    import tkinter as tk # Enforce Python3
    from queue import Queue, Empty # Enforce Python3

class AsyncDownload(Thread):
    def __init__(self, input):
        super().__init__()
        self.input = None
        self.data = None

    # functions 
    def openFile():
        tf = filedialog.askopenfilename(initialdir = "/",
                                            title = "Select a File",
                                            filetypes = (("Text files", "*.txt*"), ("all files", "*.*")))
        # pathh.insert(END, tf)
        # tf = open(tf)
        # file_cont = tf.read()
        # txtarea.insert(END, file_cont)
    
        # tf.close()

def iter_except(function, exception):
    try:
        while True:
            yield function()
    except exception:
        return


# class DisplaySubprocessOutput:
#     def __init__(self, root):
#         self.root = root
#         self.process = os.system("python core.py")
#         outputQueue = Queue(maxsize=1024)
#         t = Thread(target=self.thread_reader, args=[outputQueue])
#         t.daemon = True
#         t.start()

#         # Show subprocess stdout
#         self.label = tk.Label(root, text='  ', font=(None, 200))
#         self.label.pack(ipadx=4, padx=4, ipady=4, pady=4, fill='both')
#         self.update(outputQueue)

#     def thread_reader(self, outputQueue):
#         try:
#             with self.process.stdout as pipe:
#                 for line in iter(pipe.readline, b''):
#                     outputQueue.put(line)
#         finally:
#             outputQueue.put(None)

#     def update(self, outputQueue):
#         for line in iter_except(outputQueue.get_nowait, Empty):
#             if line is None:
#                 self.quit()
#                 return
#             else:
#                 self.label['text'] = line
#                 break
#         self.root.after(40, self.update, outputQueue)

#     def quit(self):
#         # self.process.kill()
        # self.root.destroy()


class Client(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('SSH/SCP Client')
        self.geometry('800x800')
        self.resizable(0, 0)
        
        # self.read()
        self.create_header_frame()
        self.create_body_frame()
        self.create_footer_frame()



    def create_header_frame(self):
        self.header = ttk.Frame(self)


        # Grid Configuration
        self.header.columnconfigure(0, weight=1)
        self.header.columnconfigure(1, weight=10)
        self.header.columnconfigure(2, weight=1)

        # Label
        self.label = ttk.Label(self.header, text='SAMPLE')
        self.label.grid(column=0, row=0, sticky=tk.W)


        # Entry
        self.input = ttk.Entry(self.header, textvariable=tk.StringVar(), width=30)
        self.input.grid(column=1, row=0, sticky=tk.EW)

        # Attached Header Frame
        self.header.grid(column=0, row=0, sticky=tk.NSEW, padx=10, pady=10)

        

    def monitor(self, thread):
        if thread.is_alive():
            self.after(50, lambda: self.monitor(thread))
        else:
            pass

    def create_body_frame(self):
        self.body = ttk.Frame(self)

        # Text and Scrollbar

        self.data = tk.Text(self.body, height=20)
        self.data.grid(column=0, row=1)

        scrollbar = ttk.Scrollbar(self.body, orient='vertical', command=self.data.yview)

        scrollbar.grid(column=1, row=1, sticky=tk.NS)

        self.body.grid(column=0, row=1, sticky=tk.NSEW, padx=10, pady=10)
        
    def create_footer_frame(self):
        self.footer = ttk.Frame(self)

        # Configure the grid
        self.footer.columnconfigure(0, weight=1)
        # Exit button

        self.exit_button = ttk.Button(self.footer, text='Exit', command=self.destroy)

        self.exit_button.grid(column=0, row=0, sticky=tk.E)

        # Attach the footer frame
        self.footer.grid(column=0, row=2, sticky=tk.NSEW, padx=10, pady=10)
        

# def read():
#     p = subprocess.Popen(['python', 'core.py'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
#     output, errors = p.communicate()
#     print
    # text = Text(p)
    # text.pack()
    # text.insert(END, output)



if __name__ == "__main__":
    client = Client()
    client.mainloop()
    # root = tk.Tk()
    # app = DisplaySubprocessOutput(root)
    # root.mainloop()