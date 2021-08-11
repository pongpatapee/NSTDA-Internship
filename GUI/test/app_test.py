import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
import sys
import sklearn 
from sklearn import model_selection, metrics, linear_model, neighbors
import joblib

def user_input_loop():
    is_train = True
    while True:
        user_input = input("Train or Test? ")
        if user_input.lower() == 'train':
            is_train = True
            break
        elif user_input.lower() == 'test':
            is_train = False
            break
        else:
            print("Error! Please enter Train or Test: ")

    return is_train
    
def train_logRegression(df):
    X = df.drop('target', axis=1)
    y = df['target']

    log_mod = linear_model.LogisticRegression(max_iter=1000)
    log_mod.fit(X, y)
    
    filename = 'logisticReg_mod'
    file_exe = '.joblib'
    #add os.getcwd()
    path = 'GUI/models/%s%s' % (filename, file_exe)
    unique = 1
    while os.path.isfile(path):
        path = 'GUI/models/%s_%d%s' % (filename, unique, file_exe)
        unique += 1

    joblib.dump(log_mod, path)

def train_knn(df):
    X = df.drop('target', axis=1)
    y = df['target']

    #implement getting best n_neighbors later
    #X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y, test_size=0.33, random_state=42)

    knn = neighbors.KNeighborsClassifier(n_neighbors=5)
    knn.fit(X, y)

    filename = 'knn_classifier'
    file_exe = '.joblib'
    path = 'GUI/models/%s%s' % (filename, file_exe)
    unique = 1
    while os.path.isfile(path):
        path = 'GUI/models/%s_%d%s' % (filename, unique, file_exe)
        unique += 1

    joblib.dump(knn, path)

    

def read_data(is_train):
    path = input("Enter file path: ")
    #check if path exist

    df = pd.read_csv(path)
    # if df == None:
    #     print("invalid file!")
    #     sys.exit()

    df.dropna()
    col_names = []
    for i in range(df.shape[1]):
        if i == df.shape[1] - 1 and is_train:
            col_names.append('target')
            break
        col_names.append(f's{i}')

    #if don't want to lose first datapoint
    #temp = pd.DataFrame(df.columns).transpose()
    df.columns = col_names
    return df

def main():
    is_train = user_input_loop()

    #implement crossvalidation at some point
    if is_train:
        pass

    df = read_data(is_train)
    # df.dropna()
    # print(df)
    # log_mod = linear_model.LogisticRegression(max_iter=1000)
    # X = df.drop('target', axis=1)
    # y = df['target']
    # log_mod.fit(X,y)
    # joblib.dump(log_mod, 'test.joblib')
    train_logRegression(df)
    


if __name__ == '__main__':
    main()