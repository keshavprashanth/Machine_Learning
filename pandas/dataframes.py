import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

s = pd.Series([1,3,5,np.nan,6,8])

print(s)

# Creating a DataFrame by passing a NumPy array, with a datetime index and labeled columns:
dates = pd.date_range('20130101', periods=6)
print(dates)

df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))
print(df)


# Creating a DataFrame by passing a dict of objects that can be converted to series-like.
df2 = pd.DataFrame({ 'A': 1,
                     'B': pd.Timestamp('20130102'),
                     'C': pd.Series(1, index=list(range(4)), dtype='float32'),
                     'D': np.array([3]*4, dtype='int32'),
                     'E': pd.Categorical(["test", "train", "test", "train"]),
                     'F': 'foo'})
print(df2)

# The columns of the resulting DataFrame have different dtypes.
print(df2.dtypes)

# Viewing dataframes
print(df.head(1))
print(df.tail(2))

# Display the index, columns and undelying numpy data from a dataframe.
print(df.index)
print(df.columns)
print(df.values)

# describe() shows a quick statistic summary of your data.
print(df.describe())

# Transposing your data
print(df.T)

# Sorting by an axis
print(df.sort_index(axis=1, ascending=False))

# Sorting by values
print(df.sort_values(by='B'))

# Selecting a single column, which yields a Series, equivalent to df.A:
print(df['A'])

# Selecting via [], which slices the rows
print(df[0:3])
print(df['2013-01-01':'2013-01-03'])

# For getting a cross section using a label:
print(df.loc[dates[0]])
print(df.loc[dates[1]])

# Selecting on a multi-axis label
print(df.loc[:,['A','B']])
print(df.loc[:,['A','B','C']])
