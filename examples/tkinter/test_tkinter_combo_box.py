import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
  
window = Tk()  
  
window.geometry("200x100")

def show_selected():  
    label_result.config(fg=selected.get())  

selected = tkinter.StringVar() 

label_result = tkinter.Label(window, text="Hello World!!")

button_ok = tkinter.Button(window, text="Ok", command=show_selected) 

combo_box = ttk.Combobox(window, textvariable=selected)
combo_box['values']= ("yellow", "red", "blue", "green", "white") #Usar una tupla para establecer valores
combo_box.current(1) #Elemento seleccionado por omisión
  
combo_box.pack(side = TOP)
button_ok.pack(side = BOTTOM)
label_result.pack(side = RIGHT)
  
window.mainloop()
