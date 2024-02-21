import pandas as pd
import numpy as np

df=pd.read_csv('/content/BL-Flickr-Images-Book (1).csv')
df.head()

df.shape

type(df)

for col in df:
  print(col)

to_drop = ["Edition Statement",
           'Corporate Author',
           'Corporate Contributors',
           'Former owner',
           'Engraver',
           'Contributors',
           'Issuance type',
           'Shelfmarks']

df.drop(to_drop, inplace = True,axis=1)
df.head()

df.shape

print(df.to_markdown())

df.drop_duplicates(inplace=True)
df.head()

# prompt: code to remove unwanted values

df = df[~df['Place of Publication'].isin(['London', 'Paris'])]
df.head()

unwanted_characters = ['[', ',', '-']

def clean_dates(item):
    dop= str(item.loc['Date of Publication'])

    if dop == 'nan' or dop[0] == '[':
        return np.NaN

    for character in unwanted_characters:
        if character in dop:
            character_index = dop.find(character)
            dop = dop[:character_index]

    return dop

df['Date of Publication'] = df.apply(clean_dates, axis = 1)
df.head(100)

def clean_title(title):

    if title == 'nan':
        return 'NaN'

    if title[0] == '[':
        title = title[1: title.find(']')]

    if 'by' in title:
        title = title[:title.find('by')]
    elif 'By' in title:
        title = title[:title.find('By')]

    if '[' in title:
        title = title[:title.find('[')]

    title = title[:-2]


df['Title'] = df['Title'].apply(clean_title)
df.head()

df.head(100)

def clean_dates(item):
  dop= str(item.loc['Date of Publication'])
if dop == 'nan' or dop[0] == '[':
    return np.NaN
for character in unwanted_characters:
    if character in dop:
        character_index = dop.find(character)
        dop = dop[:character_index]
    return dop
df['Date of Publication'] = df.apply(clean_dates, axis = 1)
