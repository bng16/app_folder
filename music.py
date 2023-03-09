from tkinter import *
from tkinter import ttk, filedialog
from pygame import mixer
import os

root = Tk()
root.title("MUsic player")
root.geometry("809x378")
root.configure(bg="#0f1a2b")
root.resizable(False, False)

mixer.init()


def open_folder():
    path = filedialog.askdirectory()
    if path:
        os.chdir(path)
        songs = os.listdir(path)
        print(songs)
        for song in songs:
            if song.endswith(".mp3"):
                playlist.insert(END, song)


def play_song():
    music_name = playlist.get(ACTIVE)
    mixer.music.load(playlist.get(ACTIVE))
    mixer.music.play()
    music.config(text=music_name[0:-4])


# icon


Top = PhotoImage(file="music_bg.png")
Label(root, image=Top, bg="#0f1a2b").pack()

# button

play_button = PhotoImage(file="music_5.png")
Button(root, image=play_button, bg="#0f1a2b", bd=0, command=play_song).place(x=113, y=251)

stop_button = PhotoImage(file="music_2.png")
Button(root, image=stop_button, bg="#0f1a2b", bd=0, command=mixer.music.stop).place(x=25, y=139)

resume_button = PhotoImage(file="music_3.png")
Button(root, image=resume_button, bg="#0f1a2b", bd=0, command=mixer.music.unpause).place(x=222, y=139)

pause_button = PhotoImage(file="music_1.png")
Button(root, image=pause_button, bg="#0f1a2b", bd=0, command=mixer.music.pause).place(x=114, y=26)

# label

music = Label(root, text="Now playing :-", font=("arial", 15), fg="white", bg="#000000")
music.place(x=391, y=250)

music = Label(root, text="None", font=("arial", 15), fg="white", bg="#000000")
music.place(x=391, y=290)

# music

# Menu=PhotoImage(file="music_list.png")
# Label(root,image=Menu,bg="#0f1a2b").place(x=360,y=50)

music_frame = Frame(root, bd=2, relief=RIDGE)
music_frame.place(x=360, y=50, width=373, height=160)

folderb = PhotoImage(file="music_4.png")
Button(root, image=folderb, bg="#0f1a2b", bd=0, command=open_folder).place(x=683, y=239)

scroll = Scrollbar(music_frame)
playlist = Listbox(music_frame, width=100, font=("arial", 10), bg="#333333", fg="grey", selectbackground="lightblue",
                   cursor="hand2", bd=0, yscrollcommand=scroll.set)

scroll.config(command=playlist.yview)
scroll.pack(side=RIGHT, fill=Y)
playlist.pack(side=LEFT, fill=BOTH)

root.mainloop()
