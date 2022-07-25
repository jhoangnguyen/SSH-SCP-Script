from tkinter import *
from tkinter import filedialog

# functions 
def openFile():
    tf = filedialog.askopenfilename(initialdir = "/",
                                          title = "Select a File",
                                          filetypes = (("Text files", "*.txt*"), ("all files", "*.*")))
    pathh.insert(END, tf)
    tf = open(tf)
    file_cont = tf.read()
    txtarea.insert(END, file_cont)
   
    tf.close()

def saveFile():
    tf = filedialog.asksaveasfile(
        mode='w',

        title ="Save file",
        defaultextension=".txt"
        )
    tf.config(mode='w')

    pathh.insert(END, tf)
    data = str(txtarea.get(1.0, END))
    tf.write(data)
   
    tf.close()

ws = Tk()
ws.title("Test Editing GUI")
ws.geometry("1920x1080")
ws['bg']='#2a636f'

# adding frame
frame = Frame(ws)
frame.pack(pady=20)

# adding scrollbars 
ver_sb = Scrollbar(frame, orient=VERTICAL)
ver_sb.pack(side=RIGHT, fill=BOTH)

hor_sb = Scrollbar(frame, orient=HORIZONTAL)
hor_sb.pack(side=BOTTOM, fill=BOTH)

# adding writing space
txtarea = Text(frame, width=200, height=40)
txtarea.pack(side=LEFT)

# binding scrollbar with text area
txtarea.config(yscrollcommand=ver_sb.set)
ver_sb.config(command=txtarea.yview)

txtarea.config(xscrollcommand=hor_sb.set)
hor_sb.config(command=txtarea.xview)

# adding path showing box
pathh = Entry(ws)
pathh.pack(expand=True, fill=X, padx=10)

# adding buttons 
Button(
    ws, 
    text="Open File", 
    command=openFile
    ).pack(side=LEFT, expand=True, fill=X, padx=20)

Button(
    ws, 
    text="Save File", 
    command=saveFile
    ).pack(side=LEFT, expand=True, fill=X, padx=20)

Button(
    ws, 
    text="Exit", 
    command=lambda:ws.destroy()
    ).pack(side=LEFT, expand=True, fill=X, padx=20, pady=20)

ws.mainloop()
















































# # Python program to create
# # a file explorer in Tkinter
  
# # import all components
# # from the tkinter library
# from tkinter import *
  
# # import filedialog module
# from tkinter import filedialog
  
# # Function for opening the
# # file explorer window
# def browseFiles():
#     filename = filedialog.askopenfilename(initialdir = "/",
#                                           title = "Select a File",
#                                           filetypes = (("Text files", "*.txt*"), ("all files", "*.*")))
      
#     # Change label contents
#     label_file_explorer.configure(text="File Opened: "+ filename)
#     # configfile = Text(window, wrap=WORD, width=45, height= 20)
#     # with open(filename, 'r') as f:
#     #     configfile.insert(INSERT, f.read())
#     pathh.insert(END, tf)
#     tf = open(tf)  # or tf = open(tf, 'r')
#     data = tf.read()
#     txtarea.insert(END, data)
#     tf.close()

                                                                                                  
# # Create the root window
# window = Tk()
  
# # Set window title
# window.title('File Explorer')
  
# # Set window size
# window.geometry("700x500")
  
# #Set window background color
# window.config(background = "white")
  
# # Create a File Explorer label
# label_file_explorer = Label(window,
#                             text = "File Explorer using Tkinter",
#                             width = 100, height = 4,
#                             fg = "blue")
  
      
# button_explore = Button(window,
#                         text = "Browse Files",
#                         command = browseFiles)
  
# button_exit = Button(window,
#                      text = "Exit",
#                      command = exit)
  
# # Grid method is chosen for placing
# # the widgets at respective positions
# # in a table like structure by
# # specifying rows and columns
# label_file_explorer.grid(column = 1, row = 1)
  
# button_explore.grid(column = 1, row = 2)
  
# button_exit.grid(column = 1,row = 3)
  
# # Let the window wait for any events
# window.mainloop()















































# # Main import
# import tkinter as tk
# from tkinter import ttk
# from tkinter import filedialog as fd
# from tkinter.messagebox import showinfo
# import subprocess

# # create root window
# root = tk.Tk()

# # root window title and dimension
# root.title("Sample root")

# # root dimensions (width x height)
# root.geometry('1920x1080')

# def select_file():
#     filetypes = (
#         ('text files', '*.txt'),
#         ('All files', '*.*')
#     )


#     filename = fd.askopenfilenames(
#         title='Open a file',
#         initialdir='/',
#         filetypes=filetypes
#     )

#     showinfo(
#         title='Selected File',
#         message=filename
#     )
    



# open_button = ttk.Button(root, text='Open a File', command=open_text_file)

# open_button.pack(expand=True)

# root.mainloop()

















# # adding menu bar in root window

# menu = Menu(root)
# item = Menu(menu)
# item.add_command(label='New')
# menu.add_cascade(label='File', menu=item)
# root.config(menu=menu)

# # adding a label to the root window
# lbl = Label(root, text = "Testing sample")
# lbl.grid()

# # adding input box
# txt = Entry(root, width=10)
# txt.grid(column=1, row=0)

# # function for button response
# def clicked():

#     res = "You wrote" + txt.get()
#     lbl.configure(text=res)

# # button widget
# btn = Button(root, text = "", fg= "black", command=clicked)

# # Set Button Grid
# btn.grid(column=2, row=0)
# root.mainloop()