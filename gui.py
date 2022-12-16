from tkinter import *
from tkinter.filedialog import *
import subprocess
import os

def conversion():
    dir = folder.get()
    os.chdir(dir)
    try:
        os.mkdir("Converts")
    except FileExistsError:
        pass
    
    n = 0
    for i in os.listdir(dir):
        if os.path.isfile(i):
            subprocess.run(["ffmpeg", "-i", i, f".\Converts\out{n}.mp4"])
            n += 1

def select():
    dir = askdirectory()
    folderentry.delete(0, END)
    folderentry.insert(0, dir)

# Main screen
screen = Tk()
screen.title("Batch FFMPEG encode")
screen.geometry("400x100")

convert = Button(text = "Convert", command=conversion, font=("Calibri", 12))
convert.place(x = 10, y = 40)

browse = Button(text = "Browse", command=select, font=("Calibri", 12))
browse.place(x = 80, y = 40)

folder = StringVar()
folderentry = Entry(textvariable = folder, font=("Calibri", 10), width=50)
folderentry.place(x = 10, y = 10)

screen.mainloop()
