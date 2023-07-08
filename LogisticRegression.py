import pandas as pd
import statistics

dataset = pd.read_csv("cleaned_LaptopDataset.csv")

t = statistics.median(dataset['latest_price'])

h = []

for x in dataset.latest_price:
    if (x >= t):
        h.append(1)
    else:
        h.append(0)

dataset['latest_price'] = h

from sklearn import preprocessing

le = preprocessing.LabelEncoder()
for col in dataset:
    dataset[col] = le.fit_transform(dataset[col])
dataset.head()

# input
x = dataset.drop(['latest_price', 'brand', 'processor_name', 'processor_brand', 'model', 'processor_gnrtn'], axis=1)

# output
y = dataset[["latest_price"]]

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size = 0.3, random_state = 0)
from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression(random_state = 0)
classifier.fit(X_train, y_train)
y_pred = classifier.predict(X_test)
from sklearn.metrics import confusion_matrix

cm = confusion_matrix(y_test, y_pred)

print("Confusion Matrix : \n", cm)
from sklearn.metrics import accuracy_score
print ("Accuracy : ", accuracy_score(y_test, y_pred))