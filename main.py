# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import pandas as pd
from src.config import TRAINING_FILE
from src.utility import plot_auc
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.
    print(pd.read_csv(TRAINING_FILE).shape[0])


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    print_hi(TRAINING_FILE)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
