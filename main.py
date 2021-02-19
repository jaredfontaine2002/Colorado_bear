import pandas as pd
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

#df = pd.read_xlsx('Bears 2019_PII Removed.xlsx')
df = pd.read_csv('Bears 2019_PII Removed.csv')

# The Colorado Department of Wildlife said some info was classified so I dropped those columns

df.dropna(axis=1, how='all', inplace=True)

# clean City name column

#df['District'].split('-')[1].lstrip()
df['District2'] = df['District'].str.split('-').str[1]
df.drop(axis=1)

print(df['District2'])

#print(df[df['Complaint Type'].str.contains('Aggressive')])

county_count = df.groupby(df['County']).count()
print(county_count['Section 1 Header'])
df['Complaint Type'].apply(lambda x: x.str.contains('Aggressive'))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    df.head()