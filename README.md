# Credit_Card_Approval_Classification
Application tool for predicting correct credit card customers ,the banks can maximize the profits.

Built Pilot model on  ['Gender', 'Age', 'Debt', 'Ethnicity', 'Years Employed', 'Prior Default', 'Employed', 'Credit Score', 'Driving License', 'Income']


Model Built : rforest and GB

Results:
RF



     precision    recall  f1-score   support

  precision    recall  f1-score   support

           0       0.93      0.83      0.88       102
           1       0.85      0.94      0.90       105

    accuracy                           0.89       207
   macro avg       0.89      0.89      0.89       207
weighted avg       0.89      0.89      0.89       207

CONFUSION MATRIX RF:

[[85 17]
 [ 6 99]]
 
 
GB

 precision    recall  f1-score   support

0       0.91      0.86      0.88       102
1       0.87      0.91      0.89       105

    accuracy                           0.89       207
   macro avg       0.89      0.89      0.89       207
weighted avg       0.89      0.89      0.89       207

[[88 14]
 [ 9 96]]
 
 
 
 LR:
    precision    recall  f1-score   support

           0       0.89      0.88      0.89       102
           1       0.89      0.90      0.89       105

    accuracy                           0.89       207
   macro avg       0.89      0.89      0.89       207
weighted avg       0.89      0.89      0.89       207

[[90 12]
 [11 94]]