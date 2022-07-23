import serial
import time
import tkinter

def set_button1_state():
        global b
        b += 1
        varLabel.set("LED ON ")
        ser.write(bytes('H', 'UTF-8'))
        varLabel2.set(b)
        print(b)

ser = serial.Serial('com5', 9600)
print("Reset Arduino")
time.sleep(3)

tkTop = tkinter.Tk()
tkTop.geometry('300x200')
tkTop.title("IoT24hours")

tkTop.counter = 0
b = tkTop.counter

varLabel = tkinter.IntVar()
tkLabel = tkinter.Label(textvariable=varLabel, )
tkLabel.pack()

varLabel2 = tkinter.IntVar()
tkLabel2 = tkinter.Label(textvariable=varLabel2, )
tkLabel2.pack()

button1state = tkinter.Button(tkTop,
    text="ON",
    command=set_button1_state,
    height = 4,
    fg = "black",
    width = 8,
    bd = 5,
    activebackground='green'
)
button1state.pack(side='top', ipadx=10, padx=10, pady=15)


tkinter.mainloop()