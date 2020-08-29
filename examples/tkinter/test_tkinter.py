from tkinter import *

class App:

    def __init__(self, window):

        frame = Frame(window)
        frame.pack()

        self.button = Button(
            frame, text="QUIT", fg="red", command=frame.quit
            )
        self.button.pack(side=LEFT)

        self.hi_there = Button(frame, text="Hello", command=self.say_hi)
        self.hi_there.pack(side=LEFT)

        self.show_label = Label(frame, text="World", font=("Arial Bold", 50))
        self.show_label.pack(side=LEFT)

    def say_hi(self):
        print("Hello Universe!")

root = Tk()

app = App(root)

root.mainloop()
root.destroy() # opcional
