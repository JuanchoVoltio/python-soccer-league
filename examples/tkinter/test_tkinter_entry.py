import tkinter as tk  
from functools import partial  
   
   
def call_result(label_result, n1, n2):  
    num1 = (n1.get())  
    num2 = (n2.get())
    result_message = None
    try:
        result = int(num1)+int(num2)
        result_message = "Result = %d" % result
        label_result.config(fg="black")
    except:
        result_message = "ERROR: Please check the numbers,\n must be a non-empty base 10 value"
        label_result.config(fg="red")

    label_result.config(text=result_message) #Actualizar el label de resultado 
    return  
   
window = tk.Tk()
window_x_pos = 100
window_y_pos = 200
window_geometry = ("430x200+%d+%d" % (window_x_pos, window_y_pos))
window.geometry(window_geometry)  
window.title('Calculator')  
   
number1 = tk.StringVar()  
number2 = tk.StringVar()  

#Definimos los label a mostrar 
label_num1 = tk.Label(window, text="A").grid(row=1, column=0)   
label_num2 = tk.Label(window, text="B").grid(row=2, column=0)   
label_result = tk.Label(window)  
label_result.grid(row=7, column=2)  

#Establecemos los campos a llenar  
entry_num1 = tk.Entry(window, textvariable=number1).grid(row=1, column=2)  
entry_num2 = tk.Entry(window, textvariable=number2).grid(row=2, column=2)  
  
call_result = partial(call_result, label_result, number1, number2) # Determinamos una ejecución parcial del método  
  
button_calculate = tk.Button(window, text="Calculate", command=call_result).grid(row=3, column=0)  
  
window.mainloop()  
