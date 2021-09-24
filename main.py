import youtube_dl
import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

dir = str(filedialog.asksaveasfilename(defaultextension= ".mp4", filetypes=[("mp4 files", '*.mp4')]))
saveLoc = dir + '/%(title)s.%(ext)s'

ydlOPTs = {'outtmpl': saveLoc}
ydl = youtube_dl.YoutubeDL(ydlOPTs)
url = simpledialog.askstring(title = "input", prompt = "Enter a valid youtube url")


with ydl:
    result = ydl.download([url])


root.mainloop()