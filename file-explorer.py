# from tkinter import *
# from tkinter import messagebox, filedialog
# import os
# import shutil
#
#
# root = Tk()
# root.geometry("900x550+100+30")
# root.title("file manager app")
# root.config(background="black")
#
#
# def open_file():
#     file = filedialog.askopenfilename()
#     os.startfile(file)
#     messagebox.showinfo('open file', file+" opened successfully")
#
#
# def delete_file():
#     file = filedialog.askopenfilename()
#     os.remove(file)
#     messagebox.showinfo('delete file', file+" deleted successfully")
#
#
# def rename_file():
#     global filename, file, f1, path
#     file = filedialog.askopenfilename()
#     path = os.path.abspath(file)
#     f1 = Frame(root, background="grey")
#     f1.grid(row=6, column=2)
#     Label(f1, text="Enter the file name").grid(row=0, column=1, padx=10, pady=10)
#     filename = Entry(f1)
#     filename.grid(row=1, column=1, padx=10, pady=10)
#     Button(f1, text='Rename file', command=change_name).grid(row=2, column=1, padx=10, pady=10)
#     Button(f1, text='cancel', command=f1.destroy).grid(row=2, column=2)
#     f1.mainloop()
#
#
#
# def change_name():
#     newName = filename.get()
#     dir = os.path.dirname(path)
#     renamed = os.path.join(dir,newName)
#     os.rename(path, renamed)
#     f1.destroy()
#     messagebox.showinfo('rename file', file + " renamed successfully")
#
#
# def deletefolder():
#     delFolder = filedialog.askdirectory()
#     os.rmdir(delFolder)
#     messagebox.showinfo('confirmation', "Folder Deleted !")
#
#
# def create_folder():
#     global name_entry, dir, f
#     dir = filedialog.askdirectory()
#     f = Frame(root, background="white")
#     f.grid(row=6,column=0)
#     Label(f, text="Enter the folder name",bg='white',font="bold").grid(row=0, column=0,padx=10,pady=10)
#     name_entry = Entry(f,bd=4,width=25,relief=SUNKEN)
#     name_entry.grid(row=1, column=0,padx=10,pady=10)
#     Button(f, text='create folder',font="bold",bg='dark green',fg='white', command=makeFolder).grid(row=2, column=0,padx=10,pady=10)
#     Button(f, text='cancel',font="bold",bg='red2',fg='white', command=f.destroy).grid(row=2, column=1)
#     f.mainloop()
#
#
# def makeFolder():
#     name = name_entry.get()
#     os.chdir(dir)
#     os.makedirs(name)
#     f.destroy()
#     messagebox.showinfo('create folder', " folder created successfully")
#
#
# def rename_folder():
#     global dir, folder_name, f1,path
#     dir = filedialog.askdirectory()
#     path = os.path.abspath(dir)
#     f1 = Frame(root, background="grey")
#     f1.grid(row=6, column=2)
#     Label(f1, text="Enter the folder name").grid(row=0, column=1, padx=10, pady=10)
#     folder_name = Entry(f1)
#     folder_name.grid(row=1, column=1, padx=10, pady=10)
#     Button(f1, text='Rename folder', command=change_folder).grid(row=2, column=1, padx=10, pady=10)
#     Button(f1, text='cancel', command=f1.destroy).grid(row=2, column=2)
#     f1.mainloop()
#
#
# def change_folder():
#     newName = folder_name.get()
#     dir = os.path.dirname(path)
#     renamed = os.path.join(dir,newName)
#     os.rename(path, renamed)
#     f1.destroy()
#     messagebox.showinfo('rename folder', path + " renamed successfully")
#
#
# def view_folder():
#     dir = filedialog.askdirectory()
#     f1=Frame(root)
#     f1.grid(row=5, column=2)
#     listbox = Listbox(f1,width=30)
#     listbox.grid(row=0,column=0)
#     files = os.listdir(dir)
#     for name in files:
#         listbox.insert('end', name)
#     exit_button = Button(f1, text='Ok', bg='dark green',fg='white',font="bold", command=f1.destroy)
#     exit_button.grid(row=1, column=0)
#
#
# def copy_move_file():
#     global sourceText, destinationText, destination_location, f1
#     f1 = Frame(root, width=350, height=300, background="lavender")
#     f1.grid(row=5, column=0, columnspan=4)
#
#     source_location = StringVar()
#     destination_location = StringVar()
#
#     link_Label = Label(f1, text="Select The File To Copy ", font="bold", bg='lavender')
#     link_Label.grid(row=0, column=0, pady=5, padx=5)
#
#     sourceText = Entry(f1, width=50, textvariable=source_location, font="12")
#     sourceText.grid(row=0, column=1, pady=5, padx=5)
#     source_browseButton = Button(f1, text="Browse",bg='cyan2', command=source_browse, width=15, font="bold")
#     source_browseButton.grid(row=0, column=2, pady=5, padx=5)
#
#     destinationLabel = Label(f1, text="Select The Destination", bg="lavender", font="bold")
#     destinationLabel.grid(row=1, column=0, pady=5, padx=5)
#
#     destinationText = Entry(f1, width=50, textvariable=destination_location, font=12)
#     destinationText.grid(row=1, column=1, pady=5, padx=5)
#     dest_browseButton = Button(f1, text="Browse", bg='cyan2', command=destination_browse, width=15, font="12")
#     dest_browseButton.grid(row=1, column=2, pady=5, padx=5)
#
#     copyButton = Button(f1, text="Copy File", bg='dark green',fg='white',command=copy_file, width=15, font=('bold',12))
#     copyButton.grid(row=2, column=0, pady=10, padx=10)
#
#     moveButton = Button(f1, text="Move File", bg='dark green',fg='white',command=move_file, width=15, font=('bold',12))
#     moveButton.grid(row=2, column=1, pady=10, padx=10)
#
#     cancelButton = Button(f1, text="Cancel",bg='red2',fg='white', command= f1.destroy, width=15, font=('bold',12))
#     cancelButton.grid(row=2, column=2, pady=10, padx=10)
#
#
# def source_browse():
#     global files_list
#     files_list = list(filedialog.askopenfilenames())
#     sourceText.insert('1', files_list)
#
#
# def destination_browse():
#     destinationdirectory = filedialog.askdirectory()
#     destinationText.insert('1', destinationdirectory)
#
#
# def copy_file():
#     dest_location = destination_location.get()
#     for f in files_list:
#         shutil.copy(f, dest_location)
#     messagebox.showinfo('copy file',"copied successfully")
#     f1.destroy()
#
#
# def move_file():
#     dest_location = destination_location.get()
#     for f in files_list:
#         shutil.move(f, dest_location)
#     messagebox.showinfo('move file',"moved file Successfully")
#     f1.destroy()
#
#
# lbl_heading = Label(root, text="File Manager App",font=("bold",18),fg="gold2",bg='black')
# lbl_heading.grid(row=1, column=1, pady=20, padx=20)
#
# open_btn = Button(root, text="Open File",command=open_file, width=15,font=('bold',14))
# open_btn.grid(row=2, column=0,pady=20, padx=20)
#
# delete_btn = Button(root, text="Delete File",command=delete_file, width=15,font=('bold',14))
# delete_btn.grid(row=2, column=1,pady=20, padx=20)
#
# rename_btn = Button(root, text="Rename File", command=rename_file, width=15,font=('bold',14))
# rename_btn.grid(row=2, column=2,pady=20, padx=20)
#
# copy_move_btn = Button(root, text="Copy/Move File", command=copy_move_file, width=15,font=('bold',14))
# copy_move_btn.grid(row=2, column=3,pady=20, padx=20)
#
# create_folder_btn = Button(root, text="Create folder", command=create_folder, width=15,font=('bold',14))
# create_folder_btn.grid(row=3, column=0, pady=20, padx=20)
#
# deletefolder_btn = Button(root, text="Delete folder", command=deletefolder, width=15,font=('bold',14))
# deletefolder_btn.grid(row=3, column=1, pady=20, padx=20)
#
# rename_folder_btn = Button(root, text="Rename Folder", command=rename_folder, width=15,font=('bold',14))
# rename_folder_btn.grid(row=3, column=2,pady=20, padx=20)
#
# view_btn = Button(root, text="View folder contents", command=view_folder, width=15,font=('bold',14))
# view_btn.grid(row=3, column=3, pady=20, padx=20)
#
# exit_btn = Button(root, text="Exit", command=root.destroy, width=12,font=('bold',14))
# exit_btn.grid(row=4, column=1, pady=20, padx=20)
#
# root.mainloop()

from tkinter import *
import os
import pathlib

root = Tk()
# set a title for our file explorer main window
root.title('File Explorer')

root.grid_columnconfigure(2, weight=1)
root.grid_rowconfigure(2, weight=1)


def pathChange(*event):
    # Get all Files and Folders from the given Directory
    directory = os.listdir(currentPath.get())
    # Clearing the list
    list.delete(0, END)
    # Inserting the files and directories into the list
    for file in directory:
        list.insert(0, file)


def changePathByClick(event=None):
    # Get clicked item.
    picked = list.get(list.curselection()[0])
    # get the complete path by joining the current path with the picked item
    path = os.path.join(currentPath.get(), picked)
    # Check if item is file, then open it
    if os.path.isfile(path):
        print('Opening: ' + path)
        # os.startfile(path) # for windows
        os.system("open " + path) # for mac
    # Set new path, will trigger pathChange function.
    else:
        currentPath.set(path)


def goBack(event=None):
    # get the new path
    newPath = pathlib.Path(currentPath.get()).parent
    # set it to currentPath
    currentPath.set(newPath)
    # simple message
    print('Going Back')


def open_popup():
    global top
    top = Toplevel(root)
    top.geometry("250x150")
    top.resizable(False, False)
    top.title("Child Window")
    top.columnconfigure(0, weight=1)
    Label(top, text='Enter File or Folder name').grid()
    Entry(top, textvariable=newFileName).grid(column=0, pady=10, sticky='NSEW')
    Button(top, text="Create", command=newFileOrFolder).grid(pady=10, sticky='NSEW')


def newFileOrFolder():
    # check if it is a file name or a folder
    if len(newFileName.get().split('.')) != 1:
        open(os.path.join(currentPath.get(), newFileName.get()), 'w').close()
    else:
        os.mkdir(os.path.join(currentPath.get(), newFileName.get()))
    # destroy the top
    top.destroy()
    pathChange()


top = ''

# String variables
newFileName = StringVar(root, "File.dot", 'new_name')
currentPath = StringVar(
    root,
    name='currentPath',
    value=pathlib.Path.cwd()
)
# Bind changes in this variable to the pathChange function
currentPath.trace('w', pathChange)

Button(root, text='Folder Up', command=goBack).grid(
    sticky='NSEW', column=0, row=0
)

# Keyboard shortcut for going up
root.bind("<Alt-Up>", goBack)

Entry(root, textvariable=currentPath).grid(
    sticky='NSEW', column=1, row=0, ipady=10, ipadx=10
)

# List of files and folder
list = Listbox(root)
list.grid(sticky='NSEW', column=1, row=2, ipady=10, ipadx=10)

# List Accelerators
list.bind('<Double-1>', changePathByClick)
list.bind('<Return>', changePathByClick)

# Menu
menubar = Menu(root)
# Adding a new File button
menubar.add_command(label="Add File or Folder", command=open_popup)
# Adding a quit button to the Menubar
menubar.add_command(label="Quit", command=root.quit)
# Make the menubar the Main Menu
root.config(menu=menubar)

# Call the function so the list displays
pathChange('')
# run the main program
root.mainloop()
