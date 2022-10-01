import pandas as pd
import numpy as np
from IPython.display import  display,HTML
import seaborn as sns
from sklearn import metrics
from sklearn.metrics import confusion_matrix
from sklearn.metrics import precision_score, recall_score

import matplotlib.pyplot as plt



def plotValueCounts(df,listOfColumns):
    '''
    pass List of columns
    Dataframe to print plots
    '''
    for col in listOfColumns:
        display(HTML("<b>"+col+"</b>"))
        df[col].value_counts().sort_values().plot(kind = 'barh')
        plt.show()
        
def plotBoxPlots(df,columnList):
    '''
    pass List of columns
    Dataframe to print plots
    '''
    for col in columnList:
        display(HTML("<b>"+col+"</b>"))
        df.boxplot(column=[col])
        plt.show()
        

def get_confusion_matrix_values(y_true, y_pred):
    '''Get values for tp , tn , fn , fp'''
    cm = confusion_matrix(y_true, y_pred)
    return(cm[0][0], cm[0][1], cm[1][0], cm[1][1])


def get_precision(y_true, y_pred):
    return round(precision_score(y_true,y_pred) *100)

def get_recall(y_true, y_pred):
    return round(recall_score(y_true,y_pred) *100)

def get_accuracy(y_true, y_pred):
    return round(metrics.accuracy_score(yTest, ypred)*100)


def get_f1_score(y_true, y_pred):
    return round(metrics.f1_score)


def plot_auc(modelname,xTest,yTest):
    y_pred_proba = modelname.predict_proba(xTest)[::,1]
    fpr, tpr, _ = metrics.roc_curve(yTest,  y_pred_proba)
    auc = metrics.roc_auc_score(yTest, y_pred_proba)
    plt.plot(fpr,tpr,label=str(modelname)+" Clf, auc="+str(auc))
    plt.legend(loc=4)
    plt.show()
    