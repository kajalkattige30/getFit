# -*- coding: utf-8 -*-
"""BE Proj Kmeans.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1VWEumKWprlfnFoATwtxf6oP1jibevAa3
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#from google.colab import drive
import warnings
warnings.filterwarnings('ignore')
#drive.mount('/content/drive')
dataset = pd.read_csv("C:/Users/kkatt/Documents/BE_Project/getFit/DataSetScraping/dataset.csv", sep = ',', error_bad_lines=False,encoding='utf-8')
#print(dataset)

# df = pd.DataFrame({
#     'x' : [5,6,7,8],
#     'y' : [1,2,3,4]
# })

maxCarbs = dataset['carbohydrates'].max()
minCarbs = dataset['carbohydrates'].min()
maxFat = dataset['fat'].max()
minFat = dataset['fat'].min()
df = dataset[['carbohydrates','fat','protein','recipe_name']]
k = 4
# centroids = {
#     i+1: [np.random.randint(0,80),np.random.randint(0,80)]
#     for i in range(k)
# }
# print(centroids)
centroids = {
      1: [maxCarbs-50,maxFat-30],
      2: [maxCarbs,minFat],
      3: [minCarbs,maxFat],
      4: [minCarbs,minFat]
  }
print(centroids)

fig = plt.figure(figsize=(5,5))
# plt.scatter(df['carbohydrates'],df['fat'],df['protein'],color='k')
plt.scatter(df['carbohydrates'],df['fat'],color='k')

colmap = { 1: 'r', 2: 'g' , 3: 'b', 4: 'y'}

plt.xlabel('carbohydrates')
plt.ylabel('fat')
# plt.zlabel('protein')

for i in centroids:
  plt.scatter(*centroids[i],color=colmap[i])

plt.show()

def assignment(df,centroids):
  for i in centroids:
    df['distance_from_{}'.format(i)] = (
        np.sqrt(
            (df['carbohydrates'] - centroids[i][0]) ** 2
            + (df['fat'] - centroids[i][1]) ** 2
        )
    )
    # print(df['distance_from_{}'.format(i)])
  
  centroid_distance_cols = ['distance_from_{}'.format(i) for i in centroids]
  # print(centroid_distance_cols)
  df['closest'] = df.loc[:, centroid_distance_cols].idxmin(axis = 1)
  # print(df['closest'])
  df['closest'] = df['closest'].map(lambda x: int(x.lstrip('distance_from_')))
  df['color'] = df['closest'].map(lambda x: colmap[x])
  # print(df['closest'])
  return df

df = assignment(df,centroids)
print(df.tail(20))

fig = plt.figure(figsize=(5,5))
plt.scatter(df['carbohydrates'],df['fat'],color=df['color'],alpha=0.5,edgecolor='k')
for i in centroids:
  plt.scatter(*centroids[i],color=colmap[i])

plt.xlabel('carbohydrates')
plt.ylabel('fat')
plt.show()

import copy

old_centroids = copy.deepcopy(centroids)

def update(k):
  for i in centroids:
    centroids[i][0] = np.mean(df[df['closest']==i]['carbohydrates'])
    centroids[i][1] = np.mean(df[df['closest']==i]['fat'])
  return k

centroids = update(centroids)
print(centroids)

# {1: [148.9, 82.3], 2: [148.9, 0.1], 3: [0.0, 82.3], 4: [0.0, 0.1]}

# Repeat Assignment 

df = assignment(df,centroids)
centroids = update(centroids)
fig = plt.figure(figsize=(5,5))
plt.scatter(df['carbohydrates'],df['fat'],color=df['color'],alpha=0.5,edgecolor='k')
for i in centroids:
  plt.scatter(*centroids[i],color=colmap[i])

plt.xlabel('carbohydrates')
plt.ylabel('fat')
plt.show()

# print(df[['recipe_name','closest']])
# colmap = { 1: 'r', 2: 'g' , 3: 'b', 4: 'y'}
# df.loc[df['closest'] == 1]
print(df.loc[df['closest'] == 1]) #High Carbs, High Fat
print(df.loc[df['closest'] == 2]) #High Carbs, Low Fat
print(df.loc[df['closest'] == 3]) #Low Carbs, High Fat
print(df.loc[df['closest'] == 4]) #Low Carbs, Low Fat

maxCarbs = dataset['carbohydrates'].max()
minCarbs = dataset['carbohydrates'].min()
maxFat = dataset['fat'].max()
minFat = dataset['fat'].min()
maxProtein = dataset['protein'].max()
minProtein = dataset['protein'].min()
df = dataset[['carbohydrates','fat','protein','recipe_name']]
k = 4
# centroids = {
#     i+1: [np.random.randint(0,80),np.random.randint(0,80)]
#     for i in range(k)
# }
# print(centroids)
# centroids = {
#       1: [maxCarbs-50,maxFat-30],
#       2: [maxCarbs,minFat],
#       3: [minCarbs,maxFat],
#       4: [minCarbs,minFat]
#   }

centroids = dict()
macros = ['carbohydrates','fat','protein']
x = ['high','low']

for i in range(8):
  s = format(i, '03b')
  l = []
  for j in range(3):
    # centroids[i] = [dataset[macro[j]].[x[int(s[j])]
    if(int(s[j]) == 0):
      l.append(dataset[macros[j]].max())
    else:
      l.append(dataset[macros[j]].min())
  centroids[i+1] = l



# print(format(0, '03b'))

print(centroids)

from mpl_toolkits import mplot3d

# fig = plt.figure(figsize=(5,5))
# plt.scatter(df['carbohydrates'],df['fat'],df['protein'],color='k')
colmap = { 1: 'r', 2: 'g' , 3: 'b', 4: 'y', 5: 'm', 6: 'c', 7: '#afeeee', 8: 'burlywood'}

# plt.xlabel('carbohydrates')
# plt.ylabel('fat')
# plt.zlabel('protein')

# plt.show()

fig = plt.figure(figsize=(7,7))
ax = plt.axes(projection='3d')
# z = np.linspace(0, 1, 100)
# x = z * np.sin(20 * z)
# y = z * np.cos(20 * z)
# c = x + y
ax.scatter(df['carbohydrates'], df['fat'], df['protein'], 'gray')

for i in centroids:
  ax.scatter(*centroids[i],color=colmap[i])

ax.xlabel('carbohydrates')
ax.ylabel('fat')
ax.zlabel('protein')
ax.set_title('3d Scatter plot')
plt.show()

def assignment3d(df,centroids):
  for i in centroids:
    df['distance_from_{}'.format(i)] = (
        np.sqrt(
            (df['carbohydrates'] - centroids[i][0]) ** 2
            + (df['fat'] - centroids[i][1]) ** 2
        )
    )
    # print(df['distance_from_{}'.format(i)])
  
  centroid_distance_cols = ['distance_from_{}'.format(i) for i in centroids]
  # print(centroid_distance_cols)
  df['closest'] = df.loc[:, centroid_distance_cols].idxmin(axis = 1)
  # print(df['closest'])
  df['closest'] = df['closest'].map(lambda x: int(x.lstrip('distance_from_')))
  df['color'] = df['closest'].map(lambda x: colmap[x])
  # print(df['closest'])
  return df

df = assignment3d(df,centroids)
print(df.tail(20))