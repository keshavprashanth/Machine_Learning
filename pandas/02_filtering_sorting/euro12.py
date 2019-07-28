import pandas as pd
pd.set_option('display.expand_frame_repr', False)

url = "https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/02_Filtering_%26_Sorting/Euro12/Euro_2012_stats_TEAM.csv"

euro12 = pd.read_csv(url)

# Select only the Goal column.
print(euro12[['Goals']])

# How many team participated in the Euro2012?
print('Number of teams participated in Euro 2012:', len(euro12[['Team']]))
print(euro12.shape[0])

# What is the number of columns in the dataset?
print(len(euro12.columns))
print(euro12.shape[1])
print(euro12.info())

# View only the columns Team, Yellow Cards and Red Cards and assign them to a dataframe called discipline
discipline = euro12[['Team', 'Yellow Cards', 'Red Cards']]
print(discipline)

# Sort the teams by Red Cards, then to Yellow Cards
print(discipline.sort_values('Red Cards'))
print(discipline.sort_values('Yellow Cards'))
print(discipline.sort_values(['Red Cards', 'Yellow Cards']))  # Multiples sort values must be in a list.

# Calculate the mean Yellow Cards given per Team
print(discipline[['Yellow Cards']].describe())
print(discipline[['Yellow Cards']].mean())

# Filter teams that scored more than 6 goals
print(euro12[euro12.Goals > 6])

# Select the teams that start with G
team_G = [val for val in euro12.Team if val.startswith('G')]
print(team_G)

print(euro12[euro12.Team.str.startswith('G')])

# Select the teams that ends with e
team_end_e = [val for val in euro12.Team if val.endswith('e')]
print(team_end_e)
print(euro12[euro12.Team.str.endswith('e')])

# Select team names that contain letter n
team_contains_n = [val for val in euro12.Team if 'n' in val]
print(team_contains_n)

# Select the first 7 columns
print(euro12[euro12.columns[range(7)]])
print(euro12.iloc[:, 0:7])

# Select all columns except the last 3.
print(euro12[euro12.columns[0: len(euro12.columns) - 3]])
print(euro12.iloc[:, :-3])

# Present only the Shooting Accuracy from England, Italy and Russia
print(euro12[['Team', 'Shooting Accuracy']][euro12.Team.isin(['England', 'Italy', 'Russia'])])