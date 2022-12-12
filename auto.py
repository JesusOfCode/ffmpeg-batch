import os
import subprocess

def convert(folder, format="mp4"):
    os.chdir(folder)
    try:
        os.mkdir("Converts")
    except FileExistsError:
        pass
    
    n = 0
    for i in os.listdir(folder):
        if os.path.isfile(i):
            subprocess.run(["ffmpeg", "-i", i, f".\Converts\out{n}.{format}"])
            n += 1

if __name__ == "__main__":
    n = 0
    for i in os.listdir():
        subprocess.run(["ffmpeg", "-i", i, f"out{n}.mp4"])
        n += 1
        