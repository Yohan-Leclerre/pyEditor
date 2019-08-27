from tkinter import Tk, scrolledtext, Menu, filedialog, END, messagebox, simpledialog
import os
import time

#1 for debug mode, 0 for no debug mode
debug = 0

if debug == 1:
    print("DEBUGGER ON")
if debug == 0:
    print("DEBUGGER OFF")
if debug > 1 or debug < 0:
    print("DEBUGGER ERROR!")

#Root for main window
root = Tk(className = "pyEditor")
root.iconbitmap(r'icon32x32.ico')
textArea = scrolledtext.ScrolledText(root, width=50, height=30)

#Functions

def newFile():
    if len(textArea.get('1.0', END+'-1c')) > 0:
        if messagebox.askyesno("Save?", "Do you want to save?"):
            saveFile()

        else:
            textArea.delete('1.0', END)

def openFile():
    textArea.delete('1.0', END)
    file = filedialog.askopenfile(parent=root, mode='rb', title='Select a file to view', filetypes=(("Text file", "*.txt"),("All files", "*.*"), ("Python files", "*.py *.pyw")))

    root.title(os.path.basename(file.name) + " - TEXT EDITOR")

    if file != None:
        contents = file.read()
        textArea.insert('1.0', contents)
        file.close()

def saveFile():
    file = filedialog.asksaveasfile(mode='w', defaultextension=".*", filetypes=(("Text file", "*.txt"),("All files", "*.*"), ("Python files", "*.py *.pyw")))

    if file != None:
        #slice off the last character from get, as an extra return (enter) is added
        data = textArea.get('1.0', END+'-1c')
        file.write(data)
        file.close()

def findInFile():
    findString = simpledialog.askstring("Find...", "Enter Text")
    textData = textArea.get('1.0', END)

    occureneces = textData.upper().count(findString.upper())
    
    if textData.upper().count(findString.upper()) > 0:
        label = messagebox.showinfo("Results", findString + " has multiple occurences, " + str(occureneces))

    else:
        label = messagebox.showinfo("Results","Nothing found :( ")
    
    count = 0

    if debug == 1:
        print(textData.upper().count(findString.upper()))

def about():
    label = messagebox.showinfo("About pyView 1.0","The Python version of Microsoft Windows Notepad")
    if debug == 1:
        print("INFO SHOWN (ABOUT PYEDITOR)")

def tip():
    label = messagebox.showinfo("Tip","You can use the Python Shell as a debugger.")
    if debug == 1:
        print("INFO SHOWN (TIP)")
    
def exitRoot():
    if messagebox.askyesno("Quit", "Are you sure you want to quit?"):
        time.sleep(1)
        if debug == 1:
            print("EXITED")
            time.sleep(1)
        root.destroy()

def pyhelp():
    label = messagebox.showinfo("Help","How to turn on the DEBUG MODE: set the debug value to 1 or 0 to turn off. (line 5)")
    if debug == 1:
        print("INFO SHOWN (HELP)")

#Menu options
menu = Menu(root)
root.config(menu=menu)
fileMenu = Menu(menu)
menu.add_cascade(label="File", menu=fileMenu)
fileMenu.add_command(label="New", command=newFile)
fileMenu.add_command(label="Open", command=openFile)
fileMenu.add_command(label="Save", command=saveFile)
fileMenu.add_command(label="Find", command=findInFile)
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command=exitRoot)

helpMenu = Menu(menu)
menu.add_cascade(label="Help", command=pyhelp)
menu.add_cascade(label="About", command=about)
menu.add_cascade(label="Tip", command=tip)

textArea.pack()

#Keep opened
root.mainloop()
