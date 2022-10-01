import os.path
import sys
sys.path.insert(0, '../../credit_card_approval_system/')
from src.utility import get_auc,get_recall,get_f1_score,dumpPickle,get_accuracy,get_precision
from src.config import MODEL_TRAINING_FILE , MODELS
from src.model_dispatcher import models
import pandas as pd
import warnings
import argparse

from sklearn.model_selection import train_test_split

def run(model):
    df=pd.read_csv(MODEL_TRAINING_FILE)
    x = ['Age', 'Debt', 'Ethnicity', 'Years Employed', 'Prior Default', 'Employed', 'Credit Score', 'Driving License',
         'Income']
    y = ['Approved']

    xTrain, xTest, yTrain, yTest = train_test_split(df[x], df[y], test_size=0.30,
                                                    random_state=2)
    model = models[model]
    model.fit(xTrain, yTrain)
    ypred = model.predict(xTest)

    print(f"{str(model)} Accuracy",get_accuracy(yTest,ypred))
    print(f"{str(model)} recall",get_recall(yTest,ypred))
    print(f"{str(model)} f-1",get_f1_score(yTest,ypred))
    print(f"{str(model)} precision",get_precision(yTest,ypred))

    dumpPickle(model,os.path.join(MODELS,str(model)))





if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--model",type=str)
    args = parser.parse_args()
    run(model=args.model)