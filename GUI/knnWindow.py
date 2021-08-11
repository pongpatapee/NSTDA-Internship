from tkinter import *
import pandas as pd
import numpy as np
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import seaborn as sns
from sklearn import model_selection, metrics, linear_model, neighbors
from trainResult import *

class KnnWindow:
    def __init__(self, master, df):
        self.master = master
        master.title("KNN")
        #master.geometry("400x200")

        self.df = df
        self.filepath = ""

        self.label = Label(master, text="K Nearest Neighbors", font=('Helvetica 17 bold')).pack()
        self.plot_score()

        entry_lbl = Label(self.master, text="Enter a value for num_neighbors (default = 5)").pack()
        self.entry = Entry(self.master)
        self.entry.pack()
        self.num_neighbors = 5
        self.get_neihbors_btn = Button(self.master, text="Submit and train", command=self.train).pack()
        self.isdigit_lbl = Label(self.master, text="")
        self.isdigit_lbl.pack()

        
        self.close_button = Button(master, text="Quit", command=self.master.destroy).pack()


    def train(self):
        if not self.entry.get().isdigit():
            self.isdigit_lbl.config(text="That is not an integer, try again")
        else:
            num_n = int(self.entry.get())
            X = self.df.drop('target', axis=1)
            y = self.df['target']
            X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y, test_size=0.3, random_state=42)
            knn = neighbors.KNeighborsClassifier(n_neighbors=num_n)
            knn.fit(X_train, y_train)
            y_pred = knn.predict(X_test)

            self.train_result_win = Toplevel(self.master)
            self.train_result_app = TrainResultWindow(self.train_result_win, knn, y_test, y_pred)
            
        

    def plot_score(self):
        X = self.df.drop('target', axis=1)
        y = self.df['target']
        X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y, test_size=0.3, random_state=42)
        
        k_range = range(1, 40)
        score = [] 
        for i in k_range:
            knn = neighbors.KNeighborsClassifier(n_neighbors=i)
            knn.fit(X_train, y_train)
            y_pred = knn.predict(X_test)
            score.append(metrics.accuracy_score(y_test, y_pred))
        
        fig = Figure(figsize=(6, 4))
        
        a = fig.add_subplot(111)
        a.plot(k_range, score, '-o')
        a.set_title("Accuracy score")
        a.set_ylabel("Accuracy")
        a.set_xlabel("Num Neighbors")

        canvas = FigureCanvasTkAgg(fig, master=self.master)
        canvas.get_tk_widget().pack()
        canvas.draw()