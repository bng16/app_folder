#!/usr/bin/python3
from tkinter import *
from datetime import datetime
import pytz
import time
import psutil
import threading
import os
import webbrowser

white = '#FFFFFF'
black = '#000000'

ist = pytz.timezone('Asia/Kolkata')


def alarm():
    threading.Thread(target=os.system('python alarm_main.py')).start()


def calculator():
    threading.Thread(target=os.system('python calc.py')).start()


def stopwatch():
    threading.Thread(target=os.system('python stopwatch.py')).start()


def pomodoro():
    threading.Thread(target=os.system('python snake_main.py')).start()


def screen():
    threading.Thread(target=os.system('python music.py')).start()


def about():
    threading.Thread(target=webbrowser.open(
        "https://whimsical.com/utility-tool-Au4PaYtbsVWFqEdjkSLxqk@2Ux7TurymMpdtcjf6eEy")).start()


window = Tk()

window.geometry("1000x600")
window.title("Utilities")
window.configure(bg="#ffffff")
canvas = Canvas(
    window,
    bg="#ffffff",
    height=600,
    width=1000,
    bd=0,
    highlightthickness=0,
    relief="ridge")
canvas.place(x=0, y=0)

# Time:....

label_time_now = Label(text="00:00", fg=black, bg=white, font=('Digital Numbers', 128))
label_time_now.place(x=100, y=15)

label_sec_now = Label(text="00:00", fg=black, bg=white, font=('Digital Numbers', 32))
label_sec_now.place(x=553, y=152)

label_p_now = Label(text="--", fg=black, bg=white, font=('Digital Numbers', 32))
label_p_now.place(x=553, y=48)

label_cpu = Label(text='0% CPU', fg=black, bg=white, font=('Courier Prime', 13))
label_cpu.place(x=887, y=199)

label_ram = Label(text="0% RAM", fg=black, bg=white, font=('Courier Prime', 13))
label_ram.place(x=887, y=169)

background_img = PhotoImage(file=f"background.png")
background = Label(image=background_img)
background.place(x=-1, y=235)

img0 = PhotoImage(file=f"img0.png")
b0 = Button(
    image=img0,
    borderwidth=0,
    highlightthickness=0,
    command=alarm,
    relief="flat")

b0.place(
    x=53, y=341,
    width=132,
    height=132)

img1 = PhotoImage(file=f"img1.png")
b1 = Button(
    image=img1,
    borderwidth=0,
    highlightthickness=0,
    command=calculator,
    relief="flat")

b1.place(
    x=237, y=341,
    width=132,
    height=132)

img2 = PhotoImage(file=f"img2.png")
b2 = Button(
    image=img2,
    borderwidth=0,
    highlightthickness=0,
    command=stopwatch,
    relief="flat")

b2.place(
    x=421, y=341,
    width=132,
    height=132)

img3 = PhotoImage(file=f"img3.png")
b3 = Button(
    image=img3,
    borderwidth=0,
    highlightthickness=0,
    command=pomodoro,
    relief="flat")

b3.place(
    x=618, y=341,
    width=141,
    height=132)

img4 = PhotoImage(file=f"img4.png")
b4 = Button(
    image=img4,
    borderwidth=0,
    highlightthickness=0,
    command=screen,
    relief="flat")

b4.place(
    x=822, y=341,
    width=139,
    height=132)

img5 = PhotoImage(file=f"img5.png")
b5 = Button(
    image=img5,
    borderwidth=0,
    highlightthickness=0,
    command=about,
    relief="flat")

b5.place(
    x=912, y=535,
    width=75,
    height=55)


def update():
    raw_ts = datetime.now(ist)
    time_now = raw_ts.strftime('%H:%M')
    sec_now = raw_ts.strftime('%S')
    p_now = raw_ts.strftime('%p')

    label_time_now.config(text=time_now)
    label_sec_now.config(text=f':{sec_now}')
    label_p_now.config(text=p_now)
    label_time_now.after(1000, update)


def usage():
    while True:
        cpu = psutil.cpu_percent()
        ram = psutil.virtual_memory().percent
        time.sleep(1)
        label_cpu.config(text=f'{cpu}% CPU')
        label_ram.config(text=f"{ram}% RAM")


threading.Thread(target=usage).start()
update()

window.resizable(False, False)
window.mainloop()
