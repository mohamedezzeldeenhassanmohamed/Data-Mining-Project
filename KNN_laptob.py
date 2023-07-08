import pandas as pd
import statistics
df = pd.read_csv('cleaned_LaptopDataset.csv')
t = statistics.median(df['latest_price'])

h = []

for x in df.latest_price:

    if (x >= t):
        h.append(1)
    else:
        h.append(0)
df['latest_price'] = h

########Encoder Data#######
from sklearn import preprocessing
le = preprocessing.LabelEncoder()
for col in df:
        df[col] = le.fit_transform(df[col])
########Train-test Dataset#######
x = df.drop('latest_price', axis=1)
y = df['latest_price']
from sklearn.model_selection import train_test_split
x_train, x_test ,y_train ,y_test = train_test_split(x,y,test_size=0.3)
######## KNN Using k=7 #######
from sklearn.neighbors import KNeighborsClassifier
knn=KNeighborsClassifier(n_neighbors=7)
knn.fit(x_train,y_train)
y_predict = knn.predict(x_test)
########KNN Accuracy#######
from sklearn.metrics import accuracy_score
acc = accuracy_score(y_test,y_predict)
print("accuracy of KNN " , acc*100,"%")

# print(le.inverse_transform(y_test),"\n predicted\n",le.inverse_transform(y_predict))
