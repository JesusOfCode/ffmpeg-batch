from tkinter import *
from tkinter.filedialog import *
import subprocess
import os

def conversion():
    dir = folder.get()
    if dir == "":
        print("No folder given")
        return None

    try:
        os.chdir(dir)
    except FileNotFoundError:
        print("Invalid folder")
        return None

    try:
        os.mkdir("Converts")
    except FileExistsError:
        pass

    for i in os.listdir(dir):
        if os.path.isfile(i):
            name = os.path.basename(i).split(".")[0]
            subprocess.run(["ffmpeg", "-i", i, f".\Converts\{name}.mp4"])

def select():
    dir = askdirectory()
    folderentry.delete(0, END)
    folderentry.insert(0, dir)

# Main screen
screen = Tk()
screen.title("Batch FFMPEG encode")
screen.geometry("400x100")

convert = Button(text = "Convert", command = conversion, font = ("Calibri", 12))
convert.place(x = 10, y = 40)

browse = Button(text = "Browse", command = select, font = ("Calibri", 12))
browse.place(x = 80, y = 40)

folder = StringVar()
folderentry = Entry(textvariable = folder, font = ("Calibri", 10), width = 50)
folderentry.insert(0, string="C:/")
folderentry.place(x = 10, y = 10)

screen.mainloop()
