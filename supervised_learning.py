import pandas as pd
from sklearn.preprocessing import scale
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics

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

X = df.drop(['model', 'price', 'ID'], axis=1)
y = df['price']

cars_categorical = X.select_dtypes(include=['object'])
cars_dummies = pd.get_dummies(cars_categorical, drop_first=True)
X = X.drop(list(cars_categorical.columns), axis=1)
X = pd.concat([X, cars_dummies], axis=1)
cols = X.columns
X = pd.DataFrame(scale(X))
X.columns = cols
X_train, X_test, y_train, y_test = train_test_split(X,
                                                    y,
                                                    train_size=0.7,
                                                    test_size = 0.3,
                                                    random_state=100)
lm = LinearRegression().fit(X_train, y_train)
y_pred = lm.predict(X_test)
lr_r2= metrics.r2_score(y_test, y_pred)
lr_mae = metrics.mean_absolute_error(y_test, y_pred)
lr_mse = metrics.mean_squared_error(y_test, y_pred)

print("Coefficient of determination: ", lr_r2)
print("Target test mean: ", y_test.mean())
print("Mean absolute error: ", lr_mae)
print("Mean squared error: ", lr_mse)