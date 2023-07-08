import inline as inline
import matplotlib
from sklearn.cluster import KMeans
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from matplotlib import pyplot as plt
# %matplotlib inline
df = pd.read_csv("cleaned_LaptopDataset.csv")
df.head()
labtop_brand = df[["brand"]]
labtop_brand.head(10)
from sklearn.preprocessing import OrdinalEncoder

ordinal_encoder = OrdinalEncoder()
labtop_brand_encoded = ordinal_encoder.fit_transform(labtop_brand)
labtop_brand_encoded[:10]
df['brand'] = labtop_brand_encoded
df.head()
plt.scatter(df.brand,df['latest_price'])
plt.xlabel('brand')
plt.ylabel('latest_price')
km = KMeans(n_clusters=5)
y_predicted = km.fit_predict(df[['brand','latest_price']])
y_predicted
df['cluster']=y_predicted
df.head()
km.cluster_centers_
df1 = df[df.cluster==0]
df2 = df[df.cluster==1]
df3 = df[df.cluster==2]
df4 = df[df.cluster==3]
df5 = df[df.cluster==4]
plt.scatter(df1.brand,df1['latest_price'],color='green')
plt.scatter(df2.brand,df2['latest_price'],color='red')
plt.scatter(df3.brand,df3['latest_price'],color='black')
plt.scatter(df4.brand,df4['latest_price'],color='blue')
plt.scatter(df5.brand,df5['latest_price'],color='yellow')
plt.scatter(km.cluster_centers_[:,0],km.cluster_centers_[:,1],color='purple',marker='*',label='centroid')
plt.xlabel('brand')
plt.ylabel('latest_price')
plt.legend()
scaler = MinMaxScaler()

scaler.fit(df[['latest_price']])
df['latest_price'] = scaler.transform(df[['latest_price']])

scaler.fit(df[['brand']])
df['brand'] = scaler.transform(df[['brand']])
plt.scatter(df.brand,df['latest_price'])
km = KMeans(n_clusters=5)
y_predicted = km.fit_predict(df[['brand','latest_price']])
y_predicted
df['cluster']=y_predicted
df.head()
km.cluster_centers_
df1 = df[df.cluster==0]
df2 = df[df.cluster==1]
df3 = df[df.cluster==2]
df4 = df[df.cluster==3]
df5 = df[df.cluster==4]
plt.scatter(df1.brand,df1['latest_price'],color='green')
plt.scatter(df2.brand,df2['latest_price'],color='red')
plt.scatter(df3.brand,df3['latest_price'],color='black')
plt.scatter(df4.brand,df4['latest_price'],color='blue')
plt.scatter(df5.brand,df5['latest_price'],color='yellow')
plt.scatter(km.cluster_centers_[:,0],km.cluster_centers_[:,1],color='purple',marker='*',label='centroid')
plt.legend()
plt.show()
sse = []
k_rng = range(1,10)
for k in k_rng:
    km = KMeans(n_clusters=k)
    km.fit(df[['brand','latest_price']])
    sse.append(km.inertia_)
plt.xlabel('K')
plt.ylabel('Sum of squared error')
plt.plot(k_rng, sse)
plt.show()