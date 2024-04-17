
from calendar import c
from tkinter.tix import Tree
import serial, time
from serial.tools import list_ports
import asyncio
import json
import tkinter as tk
from tkinter import *
from tkinter import ttk
import csv 
import threading

from sqlalchemy import null

main_text ="初期状態"
update = False

def main():

        global main_text
        try:
                msg =ser.readline()
                label.config(text=msg)
        
        except:
                null

        
        root.after(10,main)


if __name__ =="__main__":
        devices = [info.device for info in list_ports.comports()]
        ser =serial.Serial(devices[1], 9600)
        root = Tk()
        root.title("人間情報工学＿実験")
        root.geometry("500x500")

        label = ttk.Label(
        root,
        text = main_text,
        foreground = '#000000',
        padding = (100),
        font = ('Times New Roman',50),
        wraplength = 400,
        )
        label.pack()

        main()
        root.mainloop()
'''
devices = [info.device for info in list_ports.comports()]
print(devices)
print("Open Port")
ser =serial.Serial(devices[1], 9600)
while True:
        #a =ser.readline()
        #a = a.decode()
        #b =json.loads(a)
        #print(b["Time1"])
        #print(b["Time2"])
        ser.write(b'0')
        time.sleep(0.1)
        ser.write(b'1')
        time.sleep(0.1)
print("Close Port")
ser.close()
'''