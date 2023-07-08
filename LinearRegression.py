import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
dataset = pd.read_csv('cleaned_LaptopDataset.csv')

from sklearn import preprocessing
le = preprocessing.LabelEncoder()
for col in dataset:
        # if dataset[col].dtypes == object:
         dataset[col] = le.fit_transform(dataset[col])


x = dataset.drop('latest_price', axis=1)
y = dataset['latest_price']

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=24)

from sklearn.linear_model import LinearRegression
reg= LinearRegression()
reg.fit(x_train, y_train)
print("intercept", reg.intercept_)
print("cof", reg.coef_)
y_pred = reg.predict(x_test)

df= pd.DataFrame({'Actual': y_test, 'Predict': y_pred})
print(df)

from sklearn import metrics
from sklearn.metrics import r2_score
print('Mean Absolute Error:',metrics.mean_absolute_error(y_test, y_pred))
print('Mean Squared Error:',metrics.mean_squared_error(y_test, y_pred))
print('Root Mean Squared Error:',np.sqrt(metrics.mean_squared_error(y_test, y_pred)))

Accuracy=r2_score(y_test,y_pred)*100
print("Accuracy of the model is %.2f" %Accuracy)

plt.title('Actual vs Predicted')
plt.xlabel('Actual')
plt.ylabel('Predicted')
sns.regplot(x=y_test,y=y_pred,ci=None,color ='blue')
plt.show()















