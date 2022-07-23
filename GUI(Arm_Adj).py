import serial
import time
import tkinter
import customtkinter

customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

def quit():
    global tkTop
    tkTop.destroy()

def set_zero():
    global x
    global y
    global z
    x = 0
    y = 0
    z = 0
    varXLabel.set(x)
    varYLabel.set(y)
    varZLabel.set(z)

def set_buttonX_state():
    global x
    x += 1
    varXLabel.set(x)
    ser.write(bytes('X', 'UTF-8'))

def set_buttonx_state():
    global x
    x -= 1
    varXLabel.set(x)
    ser.write(bytes('x', 'UTF-8'))

def set_buttonY_state():
    global y
    y += 1
    varYLabel.set(y)
    ser.write(bytes('Y', 'UTF-8'))

def set_buttony_state():
    global y
    y -= 1
    varYLabel.set(y)
    ser.write(bytes('y', 'UTF-8'))

def set_buttonZ_state():
    global z
    z += 1
    varZLabel.set(z)
    ser.write(bytes('Z', 'UTF-8'))

def set_buttonz_state():
    global z
    z -= 1
    varZLabel.set(z)
    ser.write(bytes('z', 'UTF-8'))

ser = serial.Serial('com17', 9600)
print("Reset Arduino")
time.sleep(3)

tkTop = tkinter.Tk()
tkTop.geometry('300x300')
tkTop.title("test01")

tkTop.counter = 0
x = tkTop.counter
y = tkTop.counter
z = tkTop.counter

varXLabel = tkinter.IntVar()
tkXLabel = tkinter.Label(textvariable=varXLabel, ).place(x=70, y=20)
varYLabel = tkinter.IntVar()
tkYLabel = tkinter.Label(textvariable=varYLabel, ).place(x=140, y=20)
varZLabel = tkinter.IntVar()
tkZLabel = tkinter.Label(textvariable=varZLabel, ).place(x=210, y=20)

buttonXstate = tkinter.Button(tkTop, text="+X",fg = "black", bd = 5, activebackground='green',
                              command=set_buttonX_state).place(x=60, y=50, width=40, height=40)
buttonxstate = tkinter.Button(tkTop, text="-X",fg = "black", bd = 5, activebackground='red',
                              command=set_buttonx_state).place(x=60, y=100, width=40, height=40)
buttonYstate = tkinter.Button(tkTop, text="+Y",fg = "black", bd = 5, activebackground='green',
                              command=set_buttonY_state).place(x=130, y=50, width=40, height=40)
buttonystate = tkinter.Button(tkTop, text="-Y",fg = "black", bd = 5, activebackground='red',
                              command=set_buttony_state).place(x=130, y=100, width=40, height=40)
buttonZstate = tkinter.Button(tkTop, text="+Z",fg = "black", bd = 5, activebackground='green',
                              command=set_buttonZ_state).place(x=200, y=50, width=40, height=40)
buttonzstate = tkinter.Button(tkTop, text="-Z",fg = "black", bd = 5, activebackground='red',
                              command=set_buttonz_state).place(x=200, y=100, width=40, height=40)

tkButtonSetzero = tkinter.Button(tkTop, text="set zero", fg = "black", bd = 5, bg = 'green',
                              command=set_zero).place(x=110, y=160, width=80, height=30)

tkButtonQuit = tkinter.Button(tkTop, text="Quit", fg = "black", bd = 5, bg = 'yellow',
                              command=quit).place(x=110, y=200, width=80, height=30)

tkinter.mainloop()