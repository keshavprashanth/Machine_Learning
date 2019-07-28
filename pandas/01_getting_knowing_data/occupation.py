import  pandas as pd

pd.set_option('display.expand_frame_repr', False)


#  Import the dataset from this address
url = "https://raw.githubusercontent.com/justmarkham/DAT8/master/data/u.user"

# Assign it to a variable called users and use the 'user_id' as index
users = pd.read_csv(url, sep='|')
users = users.set_index('user_id')

# See the first 25 entries, see the last 10 entries
print(users.head(25))
print(users.tail(10))

#What is the number of observations in the dataset? (Number of rows)
print(users.shape)
print(users.shape[0])

# What is the number of columns in the dataset?
print(users.shape[1])

# Print the name of all the columns.
print(users.columns)

# How is the dataset indexed?
print(users.index)

# What is the data type of each column?
print(users.dtypes)

# Print only the occupation column
print(users['occupation'])

# How many different occupations there are in this dataset?
print(users['occupation'].value_counts().shape[0])
print(users.groupby('occupation').sum().shape[0])

# What is the most frequent occupation?
print(users.occupation.value_counts().head())

# Summarize the dataframe
print(users.describe())

# Summarize all the columns
print(users.describe(include="all"))

# Summarize only the occupation column
print(users.occupation.describe())

# What is the mean age of users?
print(users.age.mean())

# What is the age with least occurrence?
print(users.age.value_counts().tail())