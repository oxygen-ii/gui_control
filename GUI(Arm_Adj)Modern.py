import serial
import time
import tkinter
import customtkinter

customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

tkTop = customtkinter.CTk()
tkTop.geometry('300x300')
tkTop.title("test01")

def quit():
    global tkTop
    tkTop.destroy()

def button_function():
    print("button pressed")

# Use CTkButton instead of tkinter Button
buttonXstate = customtkinter.CTkButton(master=tkTop, text="+X", command=button_function).place(x=60, y=50, width=40, height=40)
buttonxstate = customtkinter.CTkButton(master=tkTop, text="-X", command=button_function).place(x=60, y=100, width=40, height=40)
buttonYstate = customtkinter.CTkButton(master=tkTop, text="+Y", command=button_function).place(x=130, y=50, width=40, height=40)
buttonystate = customtkinter.CTkButton(master=tkTop, text="-Y", command=button_function).place(x=130, y=100, width=40, height=40)
buttonZstate = customtkinter.CTkButton(master=tkTop, text="+Z", command=button_function).place(x=200, y=50, width=40, height=40)
buttonzstate = customtkinter.CTkButton(master=tkTop, text="+Z", command=button_function).place(x=200, y=100, width=40, height=40)

tkButtonQuit = customtkinter.CTkButton(master=tkTop, text="Quit", command=quit).place(x=110, y=200, width=80, height=30)

tkTop.mainloop()