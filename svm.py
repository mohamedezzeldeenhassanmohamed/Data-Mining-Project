import pandas as pd

from sklearn import svm

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
########Train-test Dataset#######
x = data.drop('latest_price', axis=1)
y = data['latest_price']
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3)
######## SVM Using Linear Kernel #######
classifiere = svm.SVC(kernel="linear", C=1, gamma=1)
classifiere.fit(x_train, y_train)
predictions = classifiere.predict(x_test)
########SVM Accuracy#######
from sklearn.metrics import accuracy_score
acc = accuracy_score(y_test, predictions)
print("accuracy of SVM " , acc*100,"%")
