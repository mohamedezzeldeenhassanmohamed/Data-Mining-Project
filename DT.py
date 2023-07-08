import pandas as pd
import numpy as np # for array operations
import matplotlib.pyplot as plt # for data visualization

from sklearn.metrics import mean_squared_error # for calculating the cost function
from sklearn.tree import DecisionTreeRegressor # for building the model
df = pd.read_csv('cleaned_LaptopDataset.csv')

from sklearn import preprocessing

le = preprocessing.LabelEncoder()
for col in df:
    if col != "latest_price":
     df[col] = le.fit_transform(df[col])

x = df.drop('latest_price', axis=1)
y = df['latest_price']

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=100)

from sklearn.tree import DecisionTreeRegressor
model = DecisionTreeRegressor(criterion="squared_error",random_state = 0, max_depth=7, min_samples_leaf=5)

model.fit(x_train, y_train)

y_pred = model.predict(x_test)

# RMSE (Root Mean Square Error)
rmse = float(format(np.sqrt(mean_squared_error(y_test, y_pred)), '.3f'))
print("\nRMSE: ", rmse)
accuracy = model.score(x_test,y_test)
print("With decsion tree we got --->",(accuracy*(100)).round(2),"Accuracy")
import six
import sys
from sklearn import tree
sys.modules['sklearn.externals.six'] = six
feature_col=['brand','model','processor_brand','processor_name','processor_gnrtn',
                           'ram_gb','ram_type','ssd','hdd','os','os_bit','graphic_card_gb',
                           'weight','display_size','warranty','Touchscreen',
                           'msoffice','latest_price','old_price','discount',
                           'star_rating']


tree.plot_tree(model);
fig, axes = plt.subplots(nrows=1, ncols=1, figsize=(10, 10), dpi=400)
tree.plot_tree(model,
               feature_names=feature_col,
               filled=True);
fig.savefig('RegressorTree.png')
