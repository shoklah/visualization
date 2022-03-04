import plotly.express as px
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df = pd.read_csv('data.csv')

price_Q1 = df['price'].quantile(0.25)
price_Q3 = df['price'].quantile(0.75)
price_IQR = price_Q3 - price_Q1
df = df[~((df['price'] < (price_Q1 - 1.5 * price_IQR)) | (df['price'] > (price_Q3 + 1.5 * price_IQR)))]

mpg_Q1 = df['mpg'].quantile(0.25)
mpg_Q3 = df['mpg'].quantile(0.75)
mpg_IQR = mpg_Q3 - mpg_Q1
df = df[~((df['mpg'] < (mpg_Q1 - 1.5 * mpg_IQR)) | (df['mpg'] > (mpg_Q3 + 1.5 * mpg_IQR)))]

df = df[df['mileage'] < df['mileage'].quantile(0.999)]

df = df[df['engineSize'] != 0]
df = df[df['tax'] != 0]

df = df[df['transmission'] != 'Other']
df = df[df['fuelType'] != 'Other']

fig = plt.figure(figsize=(16,4))
plt.subplot(1,3,1)
sns.violinplot(x = 'transmission', y = 'price', data = df, palette = "winter")
plt.subplot(1,3,2)
sns.violinplot(x = 'fuelType', y = 'price', data = df, palette = "winter")
plt.subplot(1,3,3)
sns.violinplot(x = 'Brand', y = 'price', data = df, palette = "winter")
plt.tight_layout()
plt.show()