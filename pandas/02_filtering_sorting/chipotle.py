import pandas as pd

pd.set_option('display.expand_frame_repr', False)

url = "https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv"

# Assign it to a variable called chipo.
chipo = pd.read_csv(url, sep='\t')

# Clean item_price column and transform it into a float
prices = [float(value[1:-1]) for value in chipo.item_price]

# Reassign the item_price column with cleaned prices.
chipo.item_price = prices
print(chipo.head())

# What is the price of each item?
print(chipo[['item_name', 'item_price']])

# Sort by the name of the item
print(chipo.sort_values('item_name'))

# What was the quantity of the most expensive item ordered?
print(chipo.sort_values("item_price", ascending=False))

# How many times were a Veggie Salad Bowl ordered?
chipo_salad = chipo[chipo.item_name == "Veggie Salad Bowl"]
print(len(chipo_salad))

# How many times people ordered more than one Canned Soda?
chipo_soda = chipo[(chipo.item_name == "Canned Soda") & (chipo.quantity > 1)]
print(len(chipo_soda))

# delete the duplicates in item_name and quantity
chipo_nodup = chipo.drop_duplicates(["item_name", "quantity"])
print(chipo_nodup)

# select only the products with quantity equals to 1
chipo_quantity_1 = chipo[chipo.quantity == 1]
print(chipo_quantity_1)