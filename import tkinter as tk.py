import tkinter as tk
import fnmatch
import os
from pygame import mixer

canvas=tk.Tk()
canvas.title("Music Player")
canvas.geometry("600×800")
canvas.config(bg="black")
rootpath="C:\\Users\saina\OneDrive\Desktop\My Music"
pattern="*.mp3"

prev_image = tk.PhotoImage(file="prev.png")
play_image=tk.PhotoImage(file="play.png")
pause_image=tk.PhotoImage(file="pause.png")
next_image=tk.PhotoImage(file="next.png")

listbox=tk.Listbox(canvas, fg="green",bg="violet",width=100,font=("bold", 15))

listbox.pack(padx=15,pady=15)

label=tk.Label(canvas,text='',bg="black",fg="yellow",font=("bold",15))
label.pack(pady=15)
top=tk.Frame(canvas, bg="black")
top.pack(padx=10,pady=5,anchor="center")

prevbutton=tk.Button(canvas,text="Previous",image= prev_image , bg="yellow",borderwidth=0)
prevbutton.pack(pady=15,in_=top,side="left")

playbutton=tk.Button(canvas,text="play",image= play_image ,bg="yellow",borderwidth=0)
playbutton.pack(pady=15,in_=top,side="left")

nextbutton=tk.Button(canvas,text="Next",image= next_image , bg="yellow",borderwidth=0)
nextbutton.pack(pady=15,in_=top,side="left")

pausebutton=tk.Button(canvas,text="Pause",image= pause_image , bg="yellow",borderwidth=0)
pausebutton.pack(pady=15,in_=top,side="left")




for root,dirs,files in os.walk(rootpath):
    for filename in fnmatch.filter(files,pattern):
        listbox.insert("end",filename)

canvas.mainloop()
