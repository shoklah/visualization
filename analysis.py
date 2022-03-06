import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

quant = ["year", "price", "mileage", "tax", "mpg", "engine size"]
df = pd.read_csv('data.csv')
fig, axs = plt.subplots(6,2, figsize=(20, 10))

for index, col in enumerate(quant):
    sns.distplot(df[col], ax=axs[index, 0]).set_title(f"Original data for {col}")

tax_Q1 = df['tax'].quantile(0.25)
tax_Q3 = df['tax'].quantile(0.75)
tax_IQR = tax_Q3 - tax_Q1
df = df[~((df['tax'] < (tax_Q1 - 1.5 * tax_IQR)) | (df['tax'] > (tax_Q3 + 1.5 * tax_IQR)))]

price_Q1 = df['price'].quantile(0.25)
price_Q3 = df['price'].quantile(0.75)
price_IQR = price_Q3 - price_Q1
df = df[~((df['price'] < (price_Q1 - 1.5 * price_IQR)) | (df['price'] > (price_Q3 + 1.5 * price_IQR)))]

mpg_Q1 = df['mpg'].quantile(0.25)
mpg_Q3 = df['mpg'].quantile(0.75)
mpg_IQR = mpg_Q3 - mpg_Q1
df = df[~((df['mpg'] < (mpg_Q1 - 1.5 * mpg_IQR)) | (df['mpg'] > (mpg_Q3 + 1.5 * mpg_IQR)))]

df = df[df['mileage'] < df['mileage'].quantile(0.999)]

df = df[df['engine size'] != 0]

for index, col in enumerate(quant):
    sns.distplot(df[col], ax=axs[index, 1]).set_title(f"Cleaned data for {col}")


fig = plt.figure(figsize=(16,4))
plt.subplot(1,3,1)
sns.violinplot(x='transmission',
               y='price',
               data=df,
               palette="winter")
plt.subplot(1,3,2)
sns.violinplot(x='fuel type',
               y='price',
               data=df,
               palette="winter")
plt.subplot(1,3,3)
sns.violinplot(x='brand',
               y='price',
               data=df,
               palette="winter")
plt.tight_layout()

df = df[df['transmission'] != 'Other']
df = df[df['fuel type'] != 'Other']

df_quant = df[quant]
corr = df_quant.corr()
f, ax = plt.subplots(figsize = (8, 6))

sns.heatmap(corr,
            cmap="winter",
            vmax=.3,
            center=0,
            square=True,
            linewidths=.5,
            cbar_kws={"shrink": .5},
            annot=True)
plt.show()