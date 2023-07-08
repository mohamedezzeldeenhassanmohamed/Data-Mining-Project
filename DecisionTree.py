import pandas as pd
import statistics

from matplotlib import pyplot as plt
from sklearn.metrics import confusion_matrix
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report

def train_using_gini(x_train, y_train):

    clf_gini = DecisionTreeClassifier(criterion="gini",
random_state=100, max_depth=3, min_samples_leaf=5)

    # Performing training
    clf_gini.fit(x_train, y_train)
    return clf_gini


def tarin_using_entropy(x_train, y_train):
    # Decision tree with entropy
    clf_entropy = DecisionTreeClassifier(
        criterion="entropy", random_state=100,
        max_depth=3, min_samples_leaf=5)

    # Performing training
    clf_entropy.fit(x_train, y_train)
    return clf_entropy


def prediction(x_test, clf_object):
    # Predicton on test with giniIndex
    y_pred = clf_object.predict(x_test)
    # print("Predicted values:")
    # print(y_pred)
    return y_pred


def cal_accuracy(y_test, y_pred):
    print("Accuracy : ",
          accuracy_score(y_test, y_pred) * 100, "%")

    print("Confusion Matrix: ",
          confusion_matrix(y_test, y_pred))

    print("Report : ",
          classification_report(y_test, y_pred))


def main():

    df = pd.read_csv('cleaned_LaptopDataset.csv')
    t = statistics.median(df['latest_price'])
    h = []

    for x in df.latest_price:

        if (x >= t):
            h.append(1)
        else:
            h.append(0)
    df['latest_price'] = h

    from sklearn import preprocessing
    le = preprocessing.LabelEncoder()
    for col in df:
        df[col] = le.fit_transform(df[col])

    x = df.drop('latest_price', axis=1)
    y = df['latest_price']

    from sklearn.model_selection import train_test_split
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=100)

    clf_gini = train_using_gini(x_train, y_train)
    clf_entropy = tarin_using_entropy(x_train, y_train)

    print("Results Using Gini Index:")
    # Prediction using gini
    y_pred_gini = prediction(x_test, clf_gini)
    cal_accuracy(y_test, y_pred_gini)

    print("Results Using Entropy:")
    # Prediction using entropy
    y_pred_entropy = prediction(x_test, clf_entropy)
    cal_accuracy(y_test, y_pred_entropy)
    import six
    import sys
    from sklearn import tree
    import graphviz
    sys.modules['sklearn.externals.six'] = six
    from six import StringIO
    from IPython.display import Image
    from sklearn.tree import export_graphviz
    import pydotplus
    feature_col=['brand','model','processor_brand','processor_name','processor_gnrtn',
                               'ram_gb','ram_type','ssd','hdd','os','os_bit','graphic_card_gb',
                               'weight','display_size','warranty','Touchscreen',
                               'msoffice','latest_price','old_price','discount',
                               'star_rating']


    tree.plot_tree(clf_gini);
    fig, axes = plt.subplots(nrows=1, ncols=1, figsize=(4, 4), dpi=300)
    tree.plot_tree(clf_gini,
                   feature_names=feature_col,
                   class_names=["0","1"],
                   filled=True);
    fig.savefig('GiniTree.png')

    tree.plot_tree(clf_entropy);
    fig, axes = plt.subplots(nrows=1, ncols=1, figsize=(4, 4), dpi=300)
    tree.plot_tree(clf_entropy,
                   feature_names=feature_col,
                   class_names=["0", "1"],
                   filled=True);
    fig.savefig('EntropyTree.png')

# Calling main function
if __name__ == "__main__":
    main()