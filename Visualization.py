

from pandas import read_csv
from matplotlib import pyplot
from seaborn import lineplot, distplot, scatterplot, boxplot


dataset = read_csv('cleaned_LaptopDataset.csv')

# lineplot(data=dataset.loc[:, {'old_price', 'latest_price'}])

# distplot(a=dataset.loc[:, {'old_price', 'latest_price'}])

# scatterplot(data=dataset.loc[:, {'old_price', 'latest_price'}])

boxplot(data=dataset.loc[:, {'old_price', 'latest_price'}])

# boxplot(data=dataset.loc[:, { 'graphic_card_gb'}])

pyplot.show()