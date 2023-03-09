from threading import Thread
from tkinter.ttk import *
from tkinter import *

from PIL import ImageTk, Image
from pygame import mixer

from datetime import datetime
from time import sleep

window = Tk()

window.geometry("930x556")
window.title('Alarm')
window.configure(bg="#f9dcce")
canvas = Canvas(
    window,
    bg="#f9dcce",
    height=556,
    width=930,
    bd=0,
    highlightthickness=0,
    relief="ridge")
canvas.place(x=0, y=0)

Top = PhotoImage(file="rbackground.png")
Label(window, image=Top, bg="#0f1a2b").pack()

name = Label(window, text="Alarm", height=1, font=('Ivy 64 bold'), bg='#ffffff')
name.place(x=600, y=53)

hr = Label(window, text="Hr", height=1, font=('Ivy 24 bold'), bg='#ffffff')
hr.place(x=540, y=166)

c_hour = Combobox(window, width=4, font=('arial 15'))
c_hour['values'] = ("00", "01", "02", "04", "05", "06", "07", "08", "09", "10", "11", "12")
c_hour.current(0)
c_hour.place(x=540, y=230)

min = Label(window, text="Min", height=1, font=('Ivy 24 bold'), bg='#ffffff')
min.place(x=640, y=166)

c_min = Combobox(window, width=4, font=('arial 15'))
c_min['values'] = (
    "00", "01", "02", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19",
    "20",
    "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35", "36", "37", "38", "39",
    "40",
    "41", "42", "43", "44", "45", "46", "47", "48", "49", "50", "51", "52", "53", "54", "55", "56", "57", "58", "59")
c_min.current(0)
c_min.place(x=640, y=230)

sec = Label(window, text="Sec", height=1, font=('Ivy 24 bold'), bg='#ffffff')
sec.place(x=740, y=166)

c_sec = Combobox(window, width=4, font=('arial 15'))
c_sec['values'] = (
    "00", "01", "02", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19",
    "20",
    "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35", "36", "37", "38", "39",
    "40",
    "41", "42", "43", "44", "45", "46", "47", "48", "49", "50", "51", "52", "53", "54", "55", "56", "57", "58", "59")
c_sec.current(0)
c_sec.place(x=740, y=230)

period = Label(window, text="Period", height=1, font=('Ivy 24 bold'), bg='#ffffff')
period.place(x=810, y=166)

c_period = Combobox(window, width=4, font=('arial 15'))
c_period['values'] = ("AM", 'PM')
c_period.current(0)
c_period.place(x=840, y=230)


def activated_alarm():
    t = Thread(target=alarm)
    t.start()


def deactivate_alarm():
    print('Deactivate alarm: ')
    mixer.music.stop()


selected = IntVar

img0 = PhotoImage(file=f"rimg0.png")
b0 = Button(
    image=img0,
    borderwidth=0,
    highlightthickness=0,
    command=activated_alarm,
    relief="flat")

b0.place(
    x=566, y=313,
    width=149,
    height=52)


def sound_alarm():
    mixer.music.load('alarm2.mp3')
    mixer.music.play()


img1 = PhotoImage(file=f"rimg1.png")
b1 = Button(
    image=img1,
    borderwidth=0,
    highlightthickness=0,
    command=deactivate_alarm,
    relief="flat")

b1.place(
    x=741, y=313,
    width=152,
    height=52)


def alarm():
    while True:
        control = 1
        print(control)
        alarm_hour = c_hour.get()
        alarm_minute = c_min.get()
        alarm_sec = c_sec.get()
        alarm_period = c_period.get()
        alarm_period = str(alarm_period).upper()

        now = datetime.now()

        hour = now.strftime("%I")
        minute = now.strftime("%M")
        second = now.strftime("%S")
        period = now.strftime("%p")

        if control == 1:
            if alarm_period == period:
                if alarm_hour == hour:
                    if alarm_minute == minute:
                        if alarm_sec == second:
                            print("alarm on !")
                            sound_alarm()
        sleep(1)


mixer.init()

window.resizable(False, False)
window.mainloop()
