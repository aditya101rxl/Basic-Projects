from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter import messagebox
import os
from wikipedia import *


def exitApp():
    root.destroy()


def newFile():
    global file
    root.title("Untitled-Notepad")
    file = None
    text_area.delete(1.0, END)


def openFile():
    global file
    file = askopenfilename(defaultextension=".txt", filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])
    if file == "":
        file = None
    else:
        try:
            f = open(file, "r")
            root.title(os.path.basename(file)+"-Notepad")
            text_area.delete(1.0, END)
            text_area.insert(1.0, f.read())
            f.close()
        except Exception as e:
            messagebox.showerror("Error..", "Unable to the selected file\n\ncheck the file type and try again")


def saveFile():
    global file
    if file is None:
        file = asksaveasfilename(initialfile='Untitled.txt', defaultextension=".txt",
                                 filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])
        if file == "":
            file = None
        else:
            try:
                f = open(file, "w")
                f.write(text_area.get(1.0, END))
                f.close()
            except Exception as e:
                messagebox.showerror("Error..", "File not Saved\n Try again")
    else:
        f = open(file, "w")
        f.write(text_area.get(1.0, END))
        f.close()
    root.title(os.path.basename(file)+"-Notepad")


def saveAsFile():
    global file
    file = asksaveasfilename(initialfile='Untitled.txt', defaultextension=".txt",
                             filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])
    if file == "":
        file = None
    else:
        try:
            f = open(file, "w")
            f.write(text_area.get(1.0, END))
            f.close()
        except Exception as e:
            messagebox.showerror("Error..", "File not Saved\n Try again")


def cut():
    text_area.event_generate("<<Cut>>")


def copy():
    text_area.event_generate("<<Copy>>")


def paste():
    text_area.event_generate("<<Paste>>")


def selectAll():
    text_area.event_generate("<<SelectAll>>")


def font():
    pass


def fontSize():
    pass


def backgroundColor(color):
    global text_area
    g = text_area.get(1.0, END)
    text_area.destroy()
    text_area = Text(root, font=("calibre", 12), bg=color)
    text_area.pack(fill=BOTH, expand=True)
    text_area.insert(1.0, g)

    # setting scrollbar
    scroll_bar = Scrollbar(text_area)
    scroll_bar.pack(side=RIGHT, fill=Y)
    scroll_bar.config(command=text_area.yview)
    text_area.config(yscrollcommand=scroll_bar.set)


def fontColor(color):
    global text_area
    g = text_area.get(1.0, END)
    text_area.destroy()
    text_area = Text(root, font=("calibre", 12), fg=color)
    text_area.pack(fill=BOTH, expand=True)
    text_area.insert(1.0, g)

    # setting scrollbar
    scroll_bar = Scrollbar(text_area)
    scroll_bar.pack(side=RIGHT, fill=Y)
    scroll_bar.config(command=text_area.yview)
    text_area.config(yscrollcommand=scroll_bar.set)


def about():
    try:
        new_root = Tk()
        new_root.geometry("400x300")
        new_root.title("About Notepad")
        text = Text(new_root, font=("calibre", 12))
        text.pack(fill=BOTH, expand=True)
        text.insert(1.0, summary("About Notepad", sentences=7))
    except Exception as e:
        messagebox.showerror("Error", "Check your internet connection")


def contactUs():
    messagebox.showinfo("contact", "What you want to know about us...\n\nplease google query")


def instructionToUse():
    try:
        new_root = Tk()
        new_root.geometry("400x300")
        new_root.title("About Notepad")
        text = Text(new_root, font=("calibre", 12))
        text.pack(fill=BOTH, expand=True)
        text.insert(1.0, summary("How to use Notepad"))
    except Exception as e:
        messagebox.showerror("Error", "Check your internet connection")


if __name__ == "__main__":
    # basic of tkinter
    root = Tk()
    root.title("Untitled-Notepad")
    root.iconbitmap("contract.png")
    root.geometry("800x500")

    file = None

    # creating text area
    text_area = Text(root, font=("calibre", 12))
    text_area.pack(fill=BOTH, expand=True)

    # setting scrollbar
    scroll_bar = Scrollbar(text_area)
    scroll_bar.pack(side=RIGHT, fill=Y)
    scroll_bar.config(command=text_area.yview)
    text_area.config(yscrollcommand=scroll_bar.set)

    # creating menus
    menu_bar = Menu(root)

    # creating file menu
    file_menu = Menu(menu_bar, tearoff=0)
    file_menu.add_command(label="New", command=newFile)
    file_menu.add_command(label="Open", command=openFile)
    file_menu.add_command(label="Save", command=saveFile)
    file_menu.add_command(label="Save As", command=saveAsFile)
    file_menu.add_separator()
    file_menu.add_command(label="Exit", command=exitApp)
    menu_bar.add_cascade(label="File", menu=file_menu)

    # creating edit menu
    edit_menu = Menu(menu_bar, tearoff=0)
    edit_menu.add_command(label="Cut", command=cut)
    edit_menu.add_command(label="Copy", command=copy)
    edit_menu.add_command(label="Paste", command=paste)
    edit_menu.add_separator()
    edit_menu.add_command(label="Select All", command=selectAll)
    menu_bar.add_cascade(label="Edit", menu=edit_menu)

    # creating Setting Menu
    setting_menu = Menu(menu_bar, tearoff=0)
    setting_menu.add_command(label="Font", command=font)
    setting_menu.add_command(label="Font Size", command=fontSize)
    #setting_menu.add_command(label="Background Color")
    # sub menu
    sub_menu = Menu(setting_menu, tearoff=0)
    setting_menu.add_cascade(label="Background Color", menu=sub_menu)
    sub_menu.add_command(label="green", command=lambda: backgroundColor("green"))
    sub_menu.add_command(label="blue", command=lambda: backgroundColor("blue"))
    sub_menu.add_command(label="red", command=lambda: backgroundColor("red"))
    #
    #setting_menu.add_command(label="Font color")
    # sub menu
    sub_menu = Menu(setting_menu, tearoff=0)
    setting_menu.add_cascade(label="Font Color", menu=sub_menu)
    sub_menu.add_command(label="green", command=lambda: fontColor("green"))
    sub_menu.add_command(label="blue", command=lambda: fontColor("blue"))
    sub_menu.add_command(label="red", command=lambda: fontColor("red"))
    #
    menu_bar.add_cascade(label="Setting", menu=setting_menu)

    # creating help menu
    help_menu = Menu(menu_bar, tearoff=0)
    help_menu.add_command(label="About", command=about)
    help_menu.add_command(label="Contact Us", command=contactUs)
    help_menu.add_command(label="Instructions to use", command=instructionToUse)
    help_menu.add_separator()
    help_menu.add_command(label="Exit", command=exitApp)
    menu_bar.add_cascade(label="Help", menu=help_menu)

    root.config(menu=menu_bar)
    mainloop()
    