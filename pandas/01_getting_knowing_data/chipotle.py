import pandas as pd

pd.set_option('display.expand_frame_repr', False)

url = "https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv"

chipo = pd.read_csv(url, sep='\t')

# See the first 10 entries
print(chipo.head(10))

# What is the number of observations in the dataset? (Number of rows)
# What is the number of columns in the dataset?
print(chipo.info())
print(chipo.shape)

# Print the name of all columns
print(chipo.columns)
# How is the dataset indexed?
print(chipo.index)

# Which was the most-ordered item?
# For the most-ordered item, how many items were ordered?
grouped = chipo.groupby('item_name').sum().sort_values(['quantity'], ascending=False)
print(grouped.head(1))

#  What was the most ordered item in the choice_description column?
grouped_choice_description = chipo.groupby('choice_description').sum().sort_values(['quantity'], ascending=False)
print(grouped_choice_description.head(1))

# how many items were ordered in total?
print(chipo.quantity.sum())

#Turn the item price into a float
print(chipo.item_price.dtype)

# Create a lambda function and change the type of item price
dollarizer = lambda x: float(x[1:-1])
chipo.item_price = chipo.item_price.apply(dollarizer)

print(chipo.item_price.dtype)

# How much was the revenue for the period in the dataset?

revenue = (chipo['quantity'] * chipo['item_price']).sum()
print(revenue)

#How many orders were made in the period?
print(chipo.order_id.value_counts().count())

# What is the average revenue amount per order?
# Solution 1
chipo['revenue'] = chipo['quantity'] * chipo['item_price']

order_grouped = chipo.groupby(by=['order_id']).sum()
print(order_grouped.mean()['revenue'])

# Solution 2
print(chipo.groupby('order_id').sum().mean()['revenue'])

# How many different items are sold?
print(chipo.item_name.value_counts().count())