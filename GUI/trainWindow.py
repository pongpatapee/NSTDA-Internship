from tkinter import *
from tkinter import filedialog,messagebox
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import model_selection, metrics, linear_model, neighbors
import joblib
from knnWindow import *
from trainResult import *

class TrainWindow:
    def __init__(self, master):
        self.master = master
        master.title("Train")
        master.geometry("400x200")
        
        self.filepath = ""

        self.label = Label(master, text="Training Model", font=('Helvetica 17 bold')).pack()

        self.upload_button = Button(master, text="Upload training data", command=self.upload_file).pack()
        self.plot_button = Button(master, text="Plot data (might take a while)", command=self.plot_data).pack()
        self.log_reg_button = Button(master, text="Logistic Regression", command=self.train_logRegression).pack()
        self.knn_button = Button(master, text="K Nearest Neighbors", command=self.train_knn).pack()
        self.close_button = Button(master, text="Quit", command=self.master.destroy).pack()

        self.filepath_label = Label(master, text="No file uploaded")
        self.filepath_label.pack()

    def upload_file(self):
        if(self.filepath == ""):
            self.filepath = filedialog.askopenfilename( initialdir = os.getcwd() ,
                 title = "select a csv file", filetypes = [("csv files", "*.csv")])
            
        else:
            self.filepath = filedialog.askopenfilename( initialdir=self.filepath,
                 title = "select a csv file", filetypes = [("csv files", "*.csv")])

        self.filepath_label.config(text=self.filepath) 
    
    def plot_data(self):
        if self.filepath == "":
            messagebox.showinfo('Error','No file uploaded')
        else:
            df = self.read_training_data()
            sns.pairplot(df, hue='target')
            plt.show()
    
    def read_training_data(self):
        df = pd.read_csv(self.filepath, header=None)

        df.dropna()
        col_names = []
        for i in range(df.shape[1]):
            if i == df.shape[1] - 1:
                col_names.append('target')
                break
            col_names.append(f's{i}')
        
        df.columns = col_names
        return df


    def train_logRegression(self):
        if self.filepath == "":
            messagebox.showinfo('Error','No file uploaded')
        else:
            df = self.read_training_data()
            X = df.drop('target', axis=1)
            y = df['target']

            X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y, test_size=0.3, random_state=42)

            log_mod = linear_model.LogisticRegression(max_iter=3000)
            log_mod.fit(X_train, y_train)

            y_pred = log_mod.predict(X_test)
            self.train_result_win = Toplevel(self.master)
            self.train_result_app = TrainResultWindow(self.train_result_win, log_mod, y_test, y_pred)
            

    def train_knn(self):
        if self.filepath == "":
            messagebox.showinfo('Error','No file uploaded')
        else:
            df = self.read_training_data()
            self.knn_window = Toplevel(self.master)
            self.knn_app = KnnWindow(self.knn_window, df)

if __name__ == "__main__":
    root = Tk()
    train_win = TrainWindow(root)
    train_win.filepath = 'data/training_df.csv'
    train_win.filepath_label.config(text=train_win.filepath)
    root.mainloop()