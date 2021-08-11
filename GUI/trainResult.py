from tkinter import *
from tkinter import filedialog,messagebox
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import model_selection, metrics, linear_model, neighbors
import joblib

class TrainResultWindow:
    def __init__(self, master, clf, y_test, y_pred):
        self.master = master
        master.title("Training Results")
        self.clf = clf
        report = metrics.classification_report(y_test, y_pred)
        conf_mat = metrics.confusion_matrix(y_test, y_pred)
        result_title = Label(self.master, text="Training Results", font=('Helvetica 17 bold')).pack()
        report_lbl = Label(self.master, text=f"Classification Report:\n{report}").pack()
        conf_mat_lbl = Label(self.master, text=f"Confusion matrix:\n{conf_mat}").pack()

        entry_lbl = Label(self.master, text="Name your model to save it").pack()
        self.entry = Entry(self.master)
        self.entry.pack()

        self.save_btn = Button(self.master, text="Save Model", command=self.save_model).pack()
        self.close_button = Button(master, text="Quit", command=self.master.destroy).pack()

    def save_model(self):
        if not os.path.exists('models'):
            os.makedirs('models')
            print("Created 'models' directory")
            
        filename = self.entry.get()
        
        if filename == "":
            messagebox.showinfo('Error','Please name your model')
        else:
            file_exe = '.joblib'
            
            filepath = 'models/%s%s' % (filename, file_exe)
            unique = 1
            while os.path.isfile(filepath):
                filepath = 'models/%s_%d%s' % (filename, unique, file_exe)
                unique += 1

            joblib.dump(self.clf, filepath)