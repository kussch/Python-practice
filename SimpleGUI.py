from tkinter import Tk, Label, Button

class FirstGui:
    def __init__(self, master):
        self.master = master
        master.title("First GUI")

        self.label = Label(master, text="This is my first GUI!")
        self.label.pack()

        self.greet_button = Button(master, text="Hello, world!", command=self.greet)
        self.greet_button.pack()

        self.close_button = Button(master, text="Close/Exit", command=master.quit)
        self.close_button.pack()

    def greet(self):
        print("Thanks for click!=)")

root = Tk()
my_gui = FirstGui(root)
root.mainloop()
