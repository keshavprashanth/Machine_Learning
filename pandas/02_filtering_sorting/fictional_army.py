import pandas as pd

pd.set_option('display.expand_frame_repr', False)

# Create an example dataframe about a fictional army
raw_data = {'regiment': ['Nighthawks', 'Nighthawks', 'Nighthawks', 'Nighthawks', 'Dragoons', 'Dragoons', 'Dragoons', 'Dragoons', 'Scouts', 'Scouts', 'Scouts', 'Scouts'],
            'company': ['1st', '1st', '2nd', '2nd', '1st', '1st', '2nd', '2nd','1st', '1st', '2nd', '2nd'],
            'deaths': [523, 52, 25, 616, 43, 234, 523, 62, 62, 73, 37, 35],
            'battles': [5, 42, 2, 2, 4, 7, 8, 3, 4, 7, 8, 9],
            'size': [1045, 957, 1099, 1400, 1592, 1006, 987, 849, 973, 1005, 1099, 1523],
            'veterans': [1, 5, 62, 26, 73, 37, 949, 48, 48, 435, 63, 345],
            'readiness': [1, 2, 3, 3, 2, 1, 2, 3, 2, 1, 2, 3],
            'armored': [1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1],
            'deserters': [4, 24, 31, 2, 3, 4, 24, 31, 2, 3, 2, 3],
            'origin': ['Arizona', 'California', 'Texas', 'Florida', 'Maine', 'Iowa', 'Alaska', 'Washington', 'Oregon', 'Wyoming', 'Louisana', 'Georgia']}

# Create a dataframe and assign it to a variable called army.
army = pd.DataFrame(raw_data)

# Set the 'origin' colum as the index of the dataframe
army = army.set_index('origin')
print(army)

#  Print only the column veterans
print(army['veterans'])
print(army[['veterans']])

# Print the columns 'veterans' and 'deaths'
print(army[['veterans', 'deaths']])

# Print the name of all the columns
print(army.info())
print(army.columns)

# Select the 'deaths', 'size' and 'deserters' columns from Maine and Alaska
print(army.loc[['Maine', 'Alaska'], ['deaths', 'size', 'deserters']])
print(army.loc[['Iowa'], ['size']])   # --> df.loc[] for selection by labels.

#Select the rows 3 to 7 and the columns 3 to 6
print(army.iloc[2:7, 1:5])   # --> df.iloc[] for selection by location.

# Select every row after the fourth row
print(army.iloc[3:])

# Select every row up to the 4th row
print(army.iloc[:4])

# Select the 3rd column up to the 7th column
print(army.iloc[:, 2:7])

# Select rows where df.deaths is greater than 50
print(army[army.deaths > 50])

#Select rows where df.deaths is greater than 500 or less than 50
print(army[(army['deaths'] > 500) | (army['deaths'] < 50)])

# Select all the regiments not named "Dragoons"
print(army[army.regiment != 'Dragoons'])

# Select the rows called Texas and Arizona
print(army.loc[['Texas', 'Arizona']])

# Select the third cell in the row named Arizona
print(army.loc[['Arizona']].iloc[:, 2])
print(army.loc[['Arizona'], ['deaths']])

# Select the third cell down in the column named deaths
print(army.iloc[[2]].loc[:, 'deaths'])