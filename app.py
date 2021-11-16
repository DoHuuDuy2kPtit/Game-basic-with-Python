import tkinter as tk
from tkinter import Button, Label, StringVar, filedialog, Entry
import os
import json

dirname = ''

def choose_folder():
    print('Choosing file')
    dirname = filedialog.askdirectory(parent=root,initialdir="/",title='Please select a directory')
    print(dirname)
    dir_text.config(text="{}".format(dirname))

def gen_code():
    print('Gen code')
    path = dir_text.cget("text")
    os.chdir(path)
    os.mkdir("{}/project".format(path))
    os.chdir("{}/project".format(path))
    print(os.getcwd())
    foldersApp = ["enums", "helpers", "http", "models", "routes", "view"]
    os.mkdir("{}/project/app".format(path))
    os.chdir("{}/project/app".format(path))
    for folder in foldersApp:
        os.mkdir(folder)
    
    foldersDB = ["migrations", "seeds"]
    os.chdir("{}/project".format(path))
    os.mkdir("{}/project/database".format(path))
    for folder in foldersDB:
        os.mkdir("{}/project/database/{}".format(path, folder))
    os.chdir("{}/project".format(path))
    fIndex = open('index.js', 'a')
    info = {
        "name": "",
        "version": "1.0.0",
        "description": "",
        "main": "index.js",
        "script": {
            "start": "node index.js",
        },
        "author": "",
        "private": True,
        "dependencies": {   
        },
        "devDependencies": {
        }
    }
    json_object = json.dumps(info, indent = 2)
    with open("package.json", "w") as outfile:
        outfile.write(json_object)
    open('package-lock.json', 'a')


root = tk.Tk()
root.title = 'APP'
root.geometry('700x250')

project_text = StringVar()
project_label = Label(root, text='Project Name', font=('bold', 14), pady=20)
project_label.grid(row=0, column=0)
project_entry = Entry(root, textvariable=project_text)
project_entry.grid(row=0, column=1)

add_btn = Button(root, text='Choose folder', width=12, command=choose_folder)
add_btn.grid(row=2, column=2, pady=20)

gen_btn = Button(root, text='Gen code', width=12, command=gen_code)
gen_btn.grid(row=3, column=2, pady=20)

dir_text = Label(root, text="Folder", font=('bold', 14))
dir_text.grid(row=2, column=4)

root.mainloop()
