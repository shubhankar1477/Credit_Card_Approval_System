from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import GradientBoostingClassifier


models= {
    "Logsitic": LogisticRegression(random_state = 0),
    "GB":GradientBoostingClassifier(random_state=0)
}