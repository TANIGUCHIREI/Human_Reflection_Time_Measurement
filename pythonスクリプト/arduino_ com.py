
from math import log2
from socket import timeout
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
import atexit
import os
import glob
os.chdir("/Users/taniguchirei/Desktop/人間情報工学実験結果")

atexit.register(exit)
main_text ="初期状態"
update = False
Active = True


name="aaa"
W =1 #センサの幅
D=1 #センサ間隔


def exit():
        global Active
        Active = False
        root.destroy()
        print("終了")
        
def arduino_and_csv():
        global main_text
        global update
        global Active
        count = 0
        files = glob.glob("*")
        key =""
        if 'Experiment_data.csv' in files:
                key ="a"
        else:
                key = "w"

        print(files)
        with open('Experiment_data_einaga.csv',key,encoding="shift-jis") as f:
                writer = csv.writer(f)
                if key=="w":
                        #新規書き込みか？
                        writer.writerows([["被験者名","センサ間隔(cm)","センサ幅(cm)","反応時間(s)","移動時間(s)","ID"]]) 

                devices = [info.device for info in list_ports.comports()]
                print(devices)
                print("Open Port")
                ser =serial.Serial(devices[1], 9600,timeout=0.01)
                while Active:
                        a =ser.readline()
                        a = a.decode()
                        if len(a)<1:
                                continue #何も入力されていなかったら待機状態に戻る。後ろの処理は行われない
                        print(a)
                        if "ERR" in a:
                                #print("失敗")
                                main_text="失敗"
                        else:
                                #print("成功")
                                b =json.loads(a)
                                #print(b["Time1"])
                                #print(b["Time2"])
                                Time1 = b["Time1"]/1000000
                                Time2 = b["Time2"]/1000000
                                main_text="反応時間: "+str(Time1) +"秒\n"+"移動時間: "+str(Time2) +"秒\n"
                                #ID = log2(2*float(D)/float(W))
                                writer.writerows([[name,D,W,Time1,Time2]]) 

def main():
        global update,label
        label.config(text=main_text)
        root.after(10,main)

def OK():
        global name,W,D,lnamel
        name = name_input.get()
        W = W_input.get()
        D = D_input.get()
        lnamel.config(text="被験者: " + name)
        lDl.config(text="センサ間隔: " +str(D)+ "cm")
        lWl.config(text='センサ幅: '+str(W)+ "cm")



lnamel = None
lDl =None
lWl =None
D_input =None
W_input =None
name_input =None

if __name__ =="__main__":
        root = Tk()
        root.title("人間情報工学＿実験")
        root.geometry("1000x2000")

        label = ttk.Label(
        root,
        text = main_text,
        #foreground = '#000000',
        padding = (100),
        font = ('Times New Roman',80),
        #wraplength = 400,
        )
        label.pack()

        lnamel = tk.Label(text="被験者: " +name)
        lnamel.place(x=50,y=600)
        name_input = tk.Entry(width=20)
        name_input.place(x=200,y=620)
        lDl = tk.Label(text="センサ間隔: " +str(D) + "cm")
        lDl.place(x=30, y=650)
        D_input = tk.Entry(width=20)
        D_input.place(x=30, y=670)

        lWl = tk.Label(text='センサ幅: '+str(W)+ "cm")
        lWl.place(x=250, y=650)
        W_input = tk.Entry(width=20)
        W_input.place(x=250, y=670)

        OK_button = tk.Button(
        root,
        text="OK",
        command=OK,
        width=20
        ).place(x=200,y=500)

        



        sub =threading.Thread(target=arduino_and_csv) #flaskをサブスレッドで動作させる
        sub.start()


        main()
        root.protocol("WM_DELETE_WINDOW", exit)
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