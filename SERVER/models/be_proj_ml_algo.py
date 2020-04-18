# -*- coding: utf-8 -*-
"""BE Proj ML Algo.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1poeQOOgRa281ZNBINBq28bqz0hZpVuHM
"""

# Karl Pearson's Correlation 

#Importing all required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import csv
# from sklearn.neighbors import NearestNeighbors
# from scipy.sparse import csr_matrix
import random
from numpy.random import choice


#Importing dataset
# dataset = pd.read_csv("C:/Users/kkatt/Documents/BE_Project/getFit/DataSetScraping/dataset.csv", sep = ',', error_bad_lines=False,encoding='utf-8')
dataset = pd.read_csv("C:/Users/Janhavi Dubule/Desktop/BE Project/getFit/DataSetScraping/dataset.csv", sep = ',', error_bad_lines=False,encoding='utf-8')

#Creating PivotDatabase
def createPivotDatabase(categories):
  #C:/Users/kkatt/Documents/BE_Project/getFit/DataSetScraping/dataset.csv
  with open("C:/Users/Janhavi Dubule/Desktop/BE Project/getFit/DataSetScraping/dataset.csv",'r') as csv_file:
      csv_reader = csv.reader(csv_file)

      next(csv_reader)
      #C:/Users/kkatt/Documents/BE_Project/DataSetScraping/PivotDataset.csv
      with open("C:/Users/Janhavi Dubule/Desktop/BE Project/getFit/DataSetScraping/PivotDataset.csv",'w', newline = '', encoding='utf-8') as new_file:
        fieldnames = ['macronutrient','recipe_name','value']
        csv_writer = csv.DictWriter(new_file,fieldnames=fieldnames)
        csv_writer.writeheader()
        macros = ['calories','fat','carbohydrates','protein']
        for line in csv_reader:
          if(line[2] in categories):
            # print(line[0],line[6],line[7],line[8],line[9])
            for i in range(6,10):
              row = {
                'macronutrient' :macros[i-6],
                'recipe_name' : line[0],
                'value' : line[i]
              }
              csv_writer.writerow(row)

def getCorrelation(sample_fooditem):
  #C:/Users/kkatt/Documents/BE_Project/DataSetScraping/PivotDataset.csv
  pivotdataset = pd.read_csv("C:/Users/Janhavi Dubule/Desktop/BE Project/getFit/DataSetScraping/PivotDataset.csv", skiprows=0, sep = ',', error_bad_lines=False,encoding='utf-8')
  pivotdataset.drop_duplicates(keep = 'first', inplace = True)
  db_pivot = pivotdataset.pivot(index='macronutrient',columns='recipe_name').value
  macronutrient = db_pivot.index
  recipe_name = db_pivot.columns
  #C:/Users/kkatt/Documents/BE_Project/DataSetScraping/pivot_table.csv
  db_pivot.to_csv("C:/Users/Janhavi Dubule/Desktop/BE Project/getFit/DataSetScraping/pivot_table.csv")

  similar_fooditem = db_pivot.corrwith(sample_fooditem)
  corr_fooditem = pd.DataFrame(similar_fooditem,columns=['pearsonR']).sort_values('pearsonR',ascending=False).head(10)
  return corr_fooditem

# K-nearest Neighbors 
# def getKnn():
#   pivotdataset = pd.read_csv("C:/Users/kkatt/Documents/BE_Project/DataSetScraping/PivotDataset.csv", skiprows=0, sep = ',', error_bad_lines=False,encoding='utf-8')
#   pivotdataset.drop_duplicates(keep = 'first', inplace = True)
#   db_pivot = pivotdataset.pivot(index='recipe_name',columns='macronutrient', values = 'value')
#   db_features_matrix = csr_matrix(db_pivot.values)
#   model_knn = NearestNeighbors(metric = 'cosine', algorithm = 'brute')
#   query_index = np.random.choice(db_pivot.shape[0])
#   distance, indices = model_knn.kneighbors(db_pivot.iloc[query_index,:].values.reshape(1,-1), n_neighbors = 6)

#   for i in range(0, len(distance.flatten())):
#     if i == 0:
#       print('Recommendation for ',db_pivot.index[query_index])
#     else:
#       print(db_pivot.index[indices.flatten()[i]],distance.flatten()[i])

# getKnn()


#All required Variables
requiredCalories = 0

breakfastCals = 0
lunchCals = 0
dinnerCals = 0
bcarbs = 0
bfats = 0
bprotein = 0
lcarbs = 0
lfats = 0
lprotein = 0
dcarbs = 0
dfats = 0
dprotein = 0

breakfastmenu = []
lunchBreadMenu = []
lunchDishMenu = []
lunchRiceMenu = []
dinnerBreadMenu = []
dinnerDishMenu = []
dinnerRiceMenu = []

#Sample User - this user data to be fetched from nodejs Server - only required Calories and plan type.

def getReqCalories():
  global requiredCalories
  gender = 'female'
  age = 21
  height = 180
  weight = 80
  goal = 'gain-weight'
  pace = 'slow'
  if(gender == 'female'):
    requiredCalories = (height*6.25) + (weight*9.99) - (21*4.92) - 161
  else:
    requiredCalories = (height*6.25) + (weight*9.99) - (21*4.92) + 5

#Method 2
#Randomly dividing total Calories into Breakfast, Lunch and Dinner Cals 
#Giving more weightage to Lunch and Dinner
def Method2():

  global breakfastCals 
  global lunchCals 
  global dinnerCals 
  global bcarbs 
  global bfats 
  global bprotein 
  global lcarbs 
  global lfats 
  global lprotein 
  global dcarbs 
  global dfats 
  global dprotein 
  
  r1 = random.randint(20,40)
  r2 = random.randint(20,40)
  r3 = random.randint(20,40)
  r4 = random.randint(20,40)
  r5 = random.randint(20,40)
  sum = r1+r2+r3+r4+r5
  breakfastCals = (r1/sum)*requiredCalories
  lunchCals = ((r2+r3)/sum)*requiredCalories
  dinnerCals = ((r4+r5)/sum)*requiredCalories

  #Breakfast MacroNutrients -> Dividing Breakfast Cals into 45-60% carbs, 20-35% fats, remaining proteins 
  r1 = random.randint(450,600)/10
  r2 = random.randint(200,350)/10
  r3 = random.randint(100,350)/10
  sum = r1+r2+r3
  bcarbs = (r1/sum)*breakfastCals
  bfats = (r2/sum)*breakfastCals
  bprotein = (r3/sum)*breakfastCals

  #Lunch MacroNutrients -> Dividing Breakfast Cals into 45-60% carbs, 20-35% fats, remaining proteins 
  r1 = random.randint(450,600)/10
  r2 = random.randint(200,350)/10
  r3 = random.randint(100,350)/10
  sum = r1+r2+r3
  lcarbs = (r1/sum)*lunchCals
  lfats = (r2/sum)*lunchCals
  lprotein = (r3/sum)*lunchCals

  #Dinner MacroNutrients -> Dividing Breakfast Cals into 45-60% carbs, 20-35% fats, remaining proteins 
  r1 = random.randint(450,600)/10
  r2 = random.randint(200,350)/10
  r3 = random.randint(100,350)/10
  sum = r1+r2+r3
  dcarbs = (r1/sum)*dinnerCals
  dfats = (r2/sum)*dinnerCals
  dprotein = (r3/sum)*dinnerCals

#Method 1 - keeping calorie divide by 3 and random in nutrients ratio
#Considering nutrient ratio - 50%carbs, 30%fats and 20%protein
def Method1():

  global breakfastCals 
  global lunchCals 
  global dinnerCals 
  global bcarbs 
  global bfats 
  global bprotein 
  global lcarbs 
  global lfats 
  global lprotein 
  global dcarbs 
  global dfats 
  global dprotein 

  #Equally dividing calories for the three meals
  breakfastCals = (1/5)*requiredCalories;
  lunchCals = (2/5)*requiredCalories;
  dinnerCals = (2/5)*requiredCalories;
  # print(requiredCalories/3)

  #Randomly dividing macronutrients ratio
  r1 = random.randint(1,100)
  r2 = random.randint(1,100)
  r3 = random.randint(1,100)
  sum = r1+r2+r3
  bcarbs = (r1/sum)*0.5*requiredCalories
  lcarbs = (r2/sum)*0.5*requiredCalories
  dcarbs = (r3/sum)*0.5*requiredCalories

  r1 = random.randint(1,100)
  r2 = random.randint(1,100)
  r3 = random.randint(1,100)
  sum = r1+r2+r3
  bfats = (r1/sum)*0.3*requiredCalories
  lfats = (r2/sum)*0.3*requiredCalories
  dfats = (r3/sum)*0.3*requiredCalories

  r1 = random.randint(1,100)
  r2 = random.randint(1,100)
  r3 = random.randint(1,100)
  sum = r1+r2+r3
  bprotein = (r1/sum)*0.2*requiredCalories
  lprotein = (r2/sum)*0.2*requiredCalories
  dprotein = (r3/sum)*0.2*requiredCalories

  # print(bprotein)
  # print(lprotein)
  # print(dprotein)

#Breakfast Recommendation
def getBreakfast():
  global breakfastmenu

  bcarbs_g = bcarbs/4.1
  bfats_g = bfats/8.8
  bprotein_g = bprotein/4.1

  sample = np.array([breakfastCals,bcarbs_g,bfats_g,bprotein_g])
  s = pd.Series(sample,index=['calories','carbohydrates','fat','protein'],dtype='float64')
  # df.loc[df['column_name'] == some_value]
  createPivotDatabase(['Appetizers'])
  #Using Correlation
  corr = getCorrelation(s)

  for i in corr.index:
    if('chutney' not in i.lower() and 'dip' not in i.lower()):
      calories = (dataset.loc[dataset['recipe_name'] == i]['calories']).iloc[0]
      if(calories in range(int(round(breakfastCals))-50,int(round(breakfastCals))+50)):
        breakfastmenu.append([i,calories,"1 serving"])
      elif(calories in range(int(round(breakfastCals/2))-25,int(round(breakfastCals/2))+25)):
        breakfastmenu.append([i,calories,"2 servings"])

#Lunch Recommendation 
def getLunch():
  global lunchBreadMenu 
  global lunchDishMenu 
  global lunchRiceMenu 
  # lunchRiceMenu = []
  # prob_bread_curry = 0.5
  # prob_rice_dish = 0.5
  # lunch_meal_type = choice(['bread curry','rice dish'],p=[prob_bread_curry,prob_rice_dish])
  lunch_meal_type = 'bread curry'

  lcarbs_g = lcarbs/4.1
  lfats_g = lfats/8.8
  lprotein_g = lprotein/4.1

  if(lunch_meal_type == "bread curry"):

      #Get Bread
      breadCals = (1/3)*lunchCals
      createPivotDatabase(['IndianBreads'])
      sample = np.array([breadCals,lcarbs_g,lfats_g,lprotein_g])
      s = pd.Series(sample,index=['calories','carbohydrates','fat','protein'],dtype='float64')

      #Using Correlation
      corr = getCorrelation(s)
      for i in corr.index:
        calories = (dataset.loc[dataset['recipe_name'] == i]['calories']).iloc[0]
        if(calories in range(int(round(breadCals))-50,int(round(breadCals))+50)):
          lunchBreadMenu.append([i,calories,"1 serving"])
        elif(calories in range(int(round(breadCals/2))-25,int(round(breadCals/2))+25)):
          lunchBreadMenu.append([i,calories,"2 servings"])

      #Get Dish
      DishCals = (2/3)*lunchCals
      createPivotDatabase(['IndianMainDishes'])
      sample = np.array([DishCals,lcarbs_g,lfats_g,lprotein_g])
      s = pd.Series(sample,index=['calories','carbohydrates','fat','protein'],dtype='float64')

      #Using Correlation
      corr = getCorrelation(s)
      for i in corr.index:
        calories = (dataset.loc[dataset['recipe_name'] == i]['calories']).iloc[0]
        if(calories in range(int(round(DishCals))-50,int(round(DishCals))+50)):
          lunchDishMenu.append([i,calories,"1 serving"])
        elif(calories in range(int(round(DishCals/2))-25,int(round(DishCals/2))+25)):
          lunchDishMenu.append([i,calories,"2 servings"])

  elif(lunch_meal_type == "rice dish"):

      RiceCals = lunchCals
      createPivotDatabase(['IndianMainDishes'])
      sample = np.array([RiceCals,lcarbs_g,lfats_g,lprotein_g])
      s = pd.Series(sample,index=['calories','carbohydrates','fat','protein'],dtype='float64')
      
      #Using Correlation
      corr = getCorrelation(s)

      for i in corr.index:
        if('rice' in i.lower()):
          calories = (dataset.loc[dataset['recipe_name'] == i]['calories']).iloc[0]
          if(calories in range(int(round(RiceCals))-50,int(round(RiceCals))+50)):
            lunchDishMenu.append([i,calories,"1 serving"])
          elif(calories in range(int(round(RiceCals/2))-25,int(round(RiceCals/2))+25)):
            lunchRiceMenu.append([i,calories,"2 servings"])



#Dinner Recommendation 
def getDinner():
  global dinnerBreadMenu
  global dinnerDishMenu
  global dinnerRiceMenu
  # prob_bread_curry = 0.5
  # prob_rice_dish = 0.5

  # dinner_meal_type = choice(['bread curry','rice dish'],p=[prob_bread_curry,prob_rice_dish])
  dinner_meal_type = 'bread curry'

  dcarbs_g = dcarbs/4.1
  dfats_g = dfats/8.8
  dprotein_g = dprotein/4.1

  if(dinner_meal_type == "bread curry"):

      #Get Bread
      breadCals = (1/3)*dinnerCals
      createPivotDatabase(['IndianBreads'])
      sample = np.array([breadCals,dcarbs_g,dfats_g,dprotein_g])
      s = pd.Series(sample,index=['calories','carbohydrates','fat','protein'],dtype='float64')
      
      #Using Correlation
      corr = getCorrelation(s)
      for i in corr.index:
        calories = (dataset.loc[dataset['recipe_name'] == i]['calories']).iloc[0]
        if(calories in range(int(round(breadCals))-50,int(round(breadCals))+50)):
          dinnerBreadMenu.append([i,calories,"1 serving"])
        elif(calories in range(int(round(breadCals/2))-25,int(round(breadCals/2))+25)):
          dinnerBreadMenu.append([i,calories,"2 servings"])

      #Get Dish
      DishCals = (2/3)*dinnerCals
      createPivotDatabase(['IndianMainDishes'])
      sample = np.array([DishCals,dcarbs_g,dfats_g,dprotein_g])
      s = pd.Series(sample,index=['calories','carbohydrates','fat','protein'],dtype='float64')
      
      #Using Correlation
      corr = getCorrelation(s)
 
      for i in corr.index:
        calories = (dataset.loc[dataset['recipe_name'] == i]['calories']).iloc[0]
        if(calories in range(int(round(DishCals))-50,int(round(DishCals))+50)):
          dinnerDishMenu.append([i,calories,"1 serving"])
        elif(calories in range(int(round(DishCals/2))-25,int(round(DishCals/2))+25)):
          dinnerDishMenu.append([i,calories,"2 servings"])

  elif(dinner_meal_type == "rice dish"):

      RiceCals = dinnerCals
      createPivotDatabase(['IndianMainDishes'])
      sample = np.array([RiceCals,dcarbs_g,dfats_g,dprotein_g])
      s = pd.Series(sample,index=['calories','carbohydrates','fat','protein'],dtype='float64')

      #Using Correlation
      corr = getCorrelation(s)

      for i in corr.index:
        if('rice' in i.lower()):
          calories = (dataset.loc[dataset['recipe_name'] == i]['calories']).iloc[0]
          if(calories in range(int(round(RiceCals))-50,int(round(RiceCals))+50)):
            dinnerDishMenu.append([i,calories,"1 serving"])
          elif(calories in range(int(round(RiceCals/2))-25,int(round(RiceCals/2))+25)):
            dinnerRiceMenu.append([i,calories,"2 servings"])


'''

Meal Recommendation Below

'''

getReqCalories()

print("Req Cal",requiredCalories)

#Dividing calories using method 1
Method2()

#get Breakfast Recommendation
getBreakfast()

#get Lunch Recommendation
getLunch()

#getDinnerRecommendation
getDinner()

# print(breakfastmenu)
# print(lunchBreadMenu)
# print(lunchDishMenu)
# print(dinnerBreadMenu)
# print(dinnerDishMenu)

#Breakfast
total = [0,0,0,0]
breakfastDetails = []
dinnerDetails = []
dinnerDetails = []
print("Meal Type\tRecommended Meal\t\t\tServings\tCalories\tCarbs\tFats\tProtein")

meal = dict()
meal['Breakfast'] = []
meal['Lunch'] = []
meal['Dinner'] = []

for item in breakfastmenu:
  itemDict = dict()
  temp = item[2].split()
  servings = int(temp[0])
  carbs = (dataset.loc[dataset['recipe_name'] == item[0]]['carbohydrates']).iloc[0]
  fats = (dataset.loc[dataset['recipe_name'] == item[0]]['fat']).iloc[0]
  protein = (dataset.loc[dataset['recipe_name'] == item[0]]['protein']).iloc[0]
  total[0]+=item[1]*servings
  total[1]+=carbs*servings
  total[2]+=fats*servings
  total[3]+=protein*servings

  itemDict['recipe_name'] = item[0]
  itemDict['servings'] = servings
  itemDict['calories'] = item[1]*servings
  itemDict['carbs'] = carbs*servings
  itemDict['fats'] = fats*servings
  itemDict['protein'] = protein*servings
  meal['Breakfast'].append(itemDict)

  print("Breakfast\t"+item[0]+"\t\t"+item[2]+"\t"+str(item[1]*servings)+"\t\t"+str(carbs*servings)+"\t"+str(fats*servings)+"\t"+str(protein*servings))
  break


for item in lunchBreadMenu:
  itemDict = dict()

  if("chapati" in item[0].lower() or "roti" in item[0].lower() or "naan" in item[0].lower()):
    temp = item[2].split()
    servings = int(temp[0])
    carbs = (dataset.loc[dataset['recipe_name'] == item[0]]['carbohydrates']).iloc[0]
    fats = (dataset.loc[dataset['recipe_name'] == item[0]]['fat']).iloc[0]
    protein = (dataset.loc[dataset['recipe_name'] == item[0]]['protein']).iloc[0]
    total[0]+=item[1]*servings
    total[1]+=carbs*servings
    total[2]+=fats*servings
    total[3]+=protein*servings

    itemDict['recipe_name'] = item[0]
    itemDict['servings'] = servings
    itemDict['calories'] = item[1]*servings
    itemDict['carbs'] = carbs*servings
    itemDict['fats'] = fats*servings
    itemDict['protein'] = protein*servings
    meal['Lunch'].append(itemDict)

    print("Lunch\t\t"+item[0]+"\t\t\t\t"+item[2]+"\t"+str(item[1]*servings)+"\t\t"+str(carbs*servings)+"\t"+str(fats*servings)+"\t"+str(protein*servings))
    break

for item in lunchDishMenu:
    

  temp = item[2].split()
  servings = int(temp[0])
  if(servings == 1):
    carbs = (dataset.loc[dataset['recipe_name'] == item[0]]['carbohydrates']).iloc[0]
    fats = (dataset.loc[dataset['recipe_name'] == item[0]]['fat']).iloc[0]
    protein = (dataset.loc[dataset['recipe_name'] == item[0]]['protein']).iloc[0]
    total[0]+=item[1]*servings
    total[1]+=carbs*servings
    total[2]+=fats*servings
    total[3]+=protein*servings

    itemDict = dict()
    itemDict['recipe_name'] = item[0]
    itemDict['servings'] = servings
    itemDict['calories'] = item[1]*servings
    itemDict['carbs'] = carbs*servings
    itemDict['fats'] = fats*servings
    itemDict['protein'] = protein*servings
    meal['Lunch'].append(itemDict)

    print("\t\t"+item[0]+"\t\t\t"+item[2]+"\t"+str(item[1]*servings)+"\t\t"+str(carbs*servings)+"\t"+str(fats*servings)+"\t"+str(protein*servings))
    break

for item in dinnerBreadMenu:
  if("chapati" in item[0].lower() or "roti" in item[0].lower() or "naan" in item[0].lower()):
    temp = item[2].split()
    servings = int(temp[0])
    carbs = (dataset.loc[dataset['recipe_name'] == item[0]]['carbohydrates']).iloc[0]
    fats = (dataset.loc[dataset['recipe_name'] == item[0]]['fat']).iloc[0]
    protein = (dataset.loc[dataset['recipe_name'] == item[0]]['protein']).iloc[0]
    total[0]+=item[1]*servings
    total[1]+=carbs*servings
    total[2]+=fats*servings
    total[3]+=protein*servings

    itemDict = dict()
    itemDict['recipe_name'] = item[0]
    itemDict['servings'] = servings
    itemDict['calories'] = item[1]*servings
    itemDict['carbs'] = carbs*servings
    itemDict['fats'] = fats*servings
    itemDict['protein'] = protein*servings
    meal['Dinner'].append(itemDict)

    print("Dinner\t\t"+item[0]+"\t\t"+item[2]+"\t"+str(item[1]*servings)+"\t\t"+str(carbs*servings)+"\t"+str(fats*servings)+"\t"+str(protein*servings))
    break

for item in dinnerDishMenu:
  temp = item[2].split()
  servings = int(temp[0])
  if(servings == 1):
    carbs = (dataset.loc[dataset['recipe_name'] == item[0]]['carbohydrates']).iloc[0]
    fats = (dataset.loc[dataset['recipe_name'] == item[0]]['fat']).iloc[0]
    protein = (dataset.loc[dataset['recipe_name'] == item[0]]['protein']).iloc[0]
    total[0]+=item[1]*servings
    total[1]+=carbs*servings
    total[2]+=fats*servings
    total[3]+=protein*servings


    itemDict = dict()
    itemDict['recipe_name'] = item[0]
    itemDict['servings'] = servings
    itemDict['calories'] = item[1]*servings
    itemDict['carbs'] = carbs*servings
    itemDict['fats'] = fats*servings
    itemDict['protein'] = protein*servings
    meal['Dinner'].append(itemDict)

    print("\t\t"+item[0]+"\t\t\t"+item[2]+"\t"+str(item[1]*servings)+"\t\t"+str(carbs*servings)+"\t"+str(fats*servings)+"\t"+str(protein*servings))
    break

print("Total : ")
print("Calories = ",total[0],)
print("Carbohydrates = ",total[1]," (",round((total[1]*4.1/total[0])*100),"%)")
print("Fats = ",total[2]," (",round((total[2]*8.8/total[0])*100),"%)")
print("Protein = ",total[3]," (",round((total[3]*4.1/total[0])*100),"%)")

print(meal)