from tkinter import *
from tkinter import filedialog,messagebox
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import model_selection, metrics, linear_model, neighbors
import joblib

class TestWindow:
    def __init__(self, master):
        self.master = master
        master.title("Test")
        master.geometry("400x200")
        
        self.model_filepath = ""
        self.data_filepath = ""

        self.label = Label(master, text="Testing Model", font=('Helvetica 17 bold')).pack()

        self.upload_model_button = Button(master, text="Upload model", command=self.upload_model).pack()
        self.upload_data_button = Button(master, text="Upload test data", command=self.upload_data).pack()
        self.test_model_button = Button(master, text="Test Model", command=self.model_predict).pack()
        self.close_button = Button(master, text="Quit", command=self.master.destroy).pack()

        self.model_filepath_label = Label(master, text="No model uploaded")
        self.model_filepath_label.pack()
        self.data_filepath_label = Label(master, text="No data uploaded")
        self.data_filepath_label.pack()

    def upload_model(self):
        if(self.model_filepath == ""):
            self.model_filepath = filedialog.askopenfilename( initialdir = os.getcwd() ,
                 title = "select a joblib file", filetypes = [("joblib files", "*.joblib")])
            
        else:
            self.model_filepath = filedialog.askopenfilename( initialdir=self.model_filepath,
                 title = "select a joblib file", filetypes = [("joblib files", "*.joblib")])

        self.model_filepath_label.config(text=self.model_filepath) 

    def upload_data(self):
        if(self.data_filepath == ""):
            self.data_filepath = filedialog.askopenfilename( initialdir = os.getcwd() ,
                 title = "select a csv file", filetypes = [("csv files", "*.csv")])
            
        else:
            self.data_filepath = filedialog.askopenfilename( initialdir=self.data_filepath,
                 title = "select a csv file", filetypes = [("csv files", "*.csv")])

        self.data_filepath_label.config(text=self.data_filepath)
    
    def model_predict(self):
        if(self.model_filepath == "" or self.data_filepath == ""):
            messagebox.showinfo('Error','Missing model or test file')
        else:
            clf = joblib.load(self.model_filepath)
            df = self.read_testing_data()
            
            pred = clf.predict(df)
            
            pred_dict = {}
            for p in pred:
                if p not in pred_dict.keys():
                    pred_dict[p] = 1
                else:
                    pred_dict[p] += 1
            
            max_num_pred = max(pred_dict, key=pred_dict.get)
            print(f"Predictions: {pred_dict}")
            print(f"most confident prediction is: {max_num_pred}")
            
            test_result_win = Toplevel(self.master)
            test_result_win.title("Results")
            result_title = Label(test_result_win, text="Test Results", font=('Helvetica 17 bold')).pack()
            pred_label = Label(test_result_win, text=f"Predictions: {pred_dict}").pack()
            confidence = Label(test_result_win, text=f"Most confident prediction is: '{max_num_pred}'").pack()
            close_btn = Button(test_result_win, text="Quit", command=test_result_win.destroy).pack()
            
    def read_testing_data(self):
        df = pd.read_csv(self.data_filepath, header=None)

        df.dropna()
        col_names = []
        for i in range(df.shape[1]):
            col_names.append(f's{i}')
        
        df.columns = col_names
        return df

if __name__ == "__main__":
    root = Tk()
    test_win = TestWindow(root)
    #test_win.data_filepath = "test_df.csv"
    test_win.data_filepath = "data/test_df.csv"
    test_win.data_filepath_label.config(text=test_win.data_filepath)
    test_win.model_filepath = "models/logisticReg_mod.joblib"
    test_win.model_filepath_label.config(text=test_win.model_filepath)
    root.mainloop()