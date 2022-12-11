from tkinter import *
import auto
import os

pwd = os.getcwd()

def bruh():
    dir = folder.get()
    auto.convert(dir, "mp4")

# Main screen
screen = Tk()
screen.title("Batch FFMPEG encode")
screen.geometry("400x100")

convert = Button(text = "Convert files in folder", command=bruh, font=("Calibri", 12))
convert.place(x = 10, y = 40)

folder = StringVar()
folderentry = Entry(textvariable = folder, font=("Calibri", 10), width=50)
folderentry.insert(0, 'C:\\Users\\aanon\\Documents\\')
folderentry.place(x = 10, y = 10)

screen.mainloop()