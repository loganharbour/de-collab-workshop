import csv

data = [['foo', 'bar', 'baz', 'bang'],
        ['git', 'works', 'really', 'great']]

with open('cooldata.csv', 'w') as f:
  writer = csv.writer(f)
  writer.writerows(data)

