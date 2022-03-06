import getopt, sys
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

min = 0
max = 72435
random = 20000

try:
    opts, args = getopt.getopt(sys.argv[1:], "r:", ["min=", "max=", "random="])
except getopt.GetoptError as err:
    print(err)
    print("USAGE:\npython visualization_2.py [--min 0] [--max 72435] [-r --random 20000]")
    sys.exit(2)
for o, a in opts:
    if o == "--min":
        min = int(a)
    elif o == "--max":
        max = int(a)
    elif o in ("-r", "--random"):
        random = int(a) 
    else:
        assert False, "unhandled option"

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

df = df[df['engine size'] != 0]
df = df[df['tax'] != 0]

df = df[df['transmission'] != 'Other']
df = df[df['fuel type'] != 'Other']

df = df[(df['ID'] > min) & (df['ID'] < max)]

df = df.sample(random)

sns.scatterplot(x='mileage',
                y='price',
                data=df,
                hue='brand',
                size='engine size',
                sizes=(40, 400),
                alpha=.2)
plt.show()