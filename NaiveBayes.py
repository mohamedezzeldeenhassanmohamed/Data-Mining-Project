import pandas as pd

import statistics

data = pd.read_csv('cleaned_LaptopDataset.csv')

t = statistics.median(data['latest_price'])

h = []

from sklearn import preprocessing

le = preprocessing.LabelEncoder()

for x in data.latest_price:

    if (x >= t):
        h.append(1)
    else:
        h.append(0)

data['latest_price'] = h

for col in data:
    data[col] = le.fit_transform(data[col])

x = data.drop(
    ['latest_price', 'brand', 'model', 'processor_brand', 'processor_name', 'ram_type', 'ram_gb', 'os_bit', 'os',
     'weight',
     'display_size', 'warranty', 'Touchscreen', 'msoffice',
     'star_rating', 'discount'], axis=1)

y = data['latest_price']
from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

from sklearn.naive_bayes import GaussianNB

nv = GaussianNB()  # create a classifier

nv.fit(x_train, y_train)  # fitting the data

predictions = nv.predict(x_test)

from sklearn.metrics import accuracy_score

acc = accuracy_score(y_test, predictions)

print("accuracy ", acc * 100)


