import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['figure.figsize'] = (10.0, 8.0)
import seaborn as sns
from scipy import stats
from scipy.stats import norm

pd.set_option('display.expand_frame_repr', False)

# loading data
train = pd.read_csv("C:/Users/Priya/Desktop/Learning/Machine Learning/data/houseprice/train.csv")
test = pd.read_csv("C:/Users/Priya/Desktop/Learning/Machine Learning/data/houseprice/test.csv")

#print(train.head(10))
#print(test.head(10))

print('The train data has {0} rows and {1} columns'.format(train.shape[0], train.shape[1]))
print('----------------')
print('The test data has {0} rows and {1} columns'.format(test.shape[0], test.shape[1]))
#print(train.info())
#print(test.info())

# Check if dataset has any missing values.
print(train.columns[train.isnull().any()])
#print(train.columns[train.isnull().any()])
#print(test.columns[test.isnull().any()])
miss= train.isnull().sum() / len(train)
miss= miss[miss > 0]
miss.sort_values(inplace=True)
print(miss)