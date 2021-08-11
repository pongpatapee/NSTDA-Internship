from tkinter import *
from trainWindow import *
from testWindow import *

class HomeWindow:
    def __init__(self, master):
        self.master = master
        master.title("Home")
        master.geometry("400x200")

        self.label = Label(master, text="Classification with SciKitLearn", font=('Helvetica 17 bold')).pack()

        self.train_button = Button(master, text="Train Model", command=self.new_train_window).pack()

        self.test_button = Button(master, text="Test Model", command=self.new_test_window).pack()

        self.close_button = Button(master, text="Quit", command=self.master.quit).pack()

    def new_train_window(self):
        self.train_window = Toplevel(self.master)
        self.train_window.title("Train")
        self.trainApp = TrainWindow(self.train_window)
        
    def new_test_window(self):
        self.test_window = Toplevel(self.master)
        self.test_window.title("Test")
        self.testApp = TestWindow(self.test_window)
    


