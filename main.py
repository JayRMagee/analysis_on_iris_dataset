# import pandas, numpy and matplotlib.pyplot
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

## load data from csv
df = pd.read_csv('C:\\Users\\jayso\\Downloads\\IRIS.csv')

##mean of each column
sl_mean = np.mean(df['sepal_length'])
print('sepal_length_mean=', sl_mean)

sw_mean = np.mean(df['sepal_width'])
print('sepal_width_mean=', sw_mean)

pl_length = np.mean(df['petal_length'])
print('petal_length_mean=', pl_length)

pw_mean = np.mean(df['petal_width'])
print('petal_width_mean=', pw_mean)

##min of each column
sl_min = np.amin(df['sepal_length'])
#print(sl_min)

sw_min = np.amin(df['sepal_width'])
#print(sw_min)

pl_min = np.amin(df['petal_length'])
#print(pl_min)

pw_min = np.amin(df['petal_width'])
#print(pl_min)

##getting the stats of each individual species
#iris_setosa
df.sort_values('species', inplace=True)

# making boolean series for a team name
filter = df['species'] == 'Iris-setosa'

# filtering data
new = df.where(filter)

iris_setosa_sepal_length_total = new['sepal_length']
iris_setosa_sepal_length_total = new.dropna(how='any')
iris_setosa_sl_average = np.average(iris_setosa_sepal_length_total['sepal_length'])
print('iris_setosa_sl_average=', iris_setosa_sl_average)

## Iris-versicolor data
df.sort_values('species', inplace=True)

# making boolean series for a team name
filter1 = df['species'] == 'Iris-versicolor'

# filtering data
new1 = df.where(filter1)

Iris_versicolor_sepal_length_total = new1['sepal_length']
Iris_versicolor_sepal_length_total = new1.dropna(how='any')
iris_versicolor_sl_average = np.average(Iris_versicolor_sepal_length_total['sepal_length'])
print('iris_versicolor_sl_average=', iris_versicolor_sl_average)

## Iris-virginica data
df.sort_values('species', inplace=True)

# making boolean series for a team name
filter2 = df['species'] == 'Iris-virginica'

# filtering data
new2 = df.where(filter2)

Iris_virginica_sepal_length_total = new2['sepal_length']
Iris_virginica_sepal_length_total = new2.dropna(how='any')
Iris_virginica_sl_average = np.average(Iris_virginica_sepal_length_total['sepal_length'])
print('iris_virginica_sl_average=', Iris_virginica_sl_average)

## plot the data that has been found
plt.figure('Sepal_length averages between species')
x_axis = ['Iris-setosa', 'Iris-versicolor', 'Iris_virginica']
y_axis = [iris_setosa_sl_average, iris_versicolor_sl_average, Iris_virginica_sl_average]

plt.bar(x_axis, y_axis)
plt.title('Averages')
plt.xlabel('Species')
plt.ylabel('sl_average')
plt.show()

## calculate 25th and 75th percentile
iris_setosa_sepal_length_percentiles = np.percentile(iris_setosa_sepal_length_total['sepal_length'], [25, 75])
print(iris_setosa_sepal_length_percentiles)

iris_versicolor_sepal_length_percentiles = np.percentile(Iris_versicolor_sepal_length_total['sepal_length'], [25, 75])
print(iris_versicolor_sepal_length_percentiles)

iris_verginica_sepal_length_percentiles = np.percentile(Iris_virginica_sepal_length_total['sepal_length'], [25, 75])
print(iris_verginica_sepal_length_percentiles)
