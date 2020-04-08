from pymongo import MongoClient as mongo
import csv

cluster = mongo("mongodb+srv://Janhavi:mongodb@projectcluster-azpnv.mongodb.net/test?retryWrites=true&w=majority")

db = cluster.ProjectDB

itemsArr = []

#Appetizers-Veg
colAppetizers = db.Appetizers
vegAppetizers = colAppetizers.find_one({'category':'Veg'})
vegRecipes = vegAppetizers['recipes']
for recipe in vegRecipes:
    # print(recipe['recipe_name'])
    item = {
        'recipe_name' : recipe['recipe_name'],
        'recipe_type' : 'Veg',
        'category' : 'Appetizers',
        'ratings' : recipe['ratings'],
        'ingredients' : recipe['ingredients'],
        'time_required' : recipe['time_required'],
        'calories' : float(recipe['nutrition_facts']['calories']),
        'fat' : float(recipe['nutrition_facts']['fat']),
        'carbohydrates' : float(recipe['nutrition_facts']['carbohydrates']),
        'protein' : float(recipe['nutrition_facts']['protein']),
        'cholesterol' : float(recipe['nutrition_facts']['cholesterol']),
        'sodium' : float(recipe['nutrition_facts']['sodium']),
        'recipe_categories' : recipe['recipe_categories'] 
    }
    itemsArr.append(item)

print("Appetizers-Veg : " ,len(itemsArr))


# Appetizers-Non-Veg
colAppetizers = db.Appetizers
nonvegAppetizers = colAppetizers.find_one({'category':'Non-Veg'})
nonvegRecipes = nonvegAppetizers['recipes']
for recipe in nonvegRecipes:
    # print(recipe['recipe_name'])
    item = {
        'recipe_name' : recipe['recipe_name'],
        'recipe_type' : 'Non-Veg',
        'category' : 'Appetizers',
        'ratings' : recipe['ratings'],
        'ingredients' : recipe['ingredients'],
        'time_required' : recipe['time_required'],
        'calories' : float(recipe['nutrition_facts']['calories']),
        'fat' : float(recipe['nutrition_facts']['fat']),
        'carbohydrates' : float(recipe['nutrition_facts']['carbohydrates']),
        'protein' : float(recipe['nutrition_facts']['protein']),
        'cholesterol' : float(recipe['nutrition_facts']['cholesterol']),
        'sodium' : float(recipe['nutrition_facts']['sodium']),
        'recipe_categories' : recipe['recipe_categories'] 
    }
    itemsArr.append(item)


print("+ Appetizers-Non-Veg : " ,len(itemsArr))


#IndianMainDishes - Veg
col = db.IndianMainDishes
veg = col.find_one({'category':'Veg'})
recipes = veg['recipes']
for recipe in recipes:
    # print(recipe['recipe_name'])
    item = {
        'recipe_name' : recipe['recipe_name'],
        'recipe_type' : 'Veg',
        'category' : 'IndianMainDishes',
        'ratings' : recipe['ratings'],
        'ingredients' : recipe['ingredients'],
        'time_required' : recipe['time_required'],
        'calories' : float(recipe['nutrition_facts']['calories']),
        'fat' : float(recipe['nutrition_facts']['fat']),
        'carbohydrates' : float(recipe['nutrition_facts']['carbohydrates']),
        'protein' : float(recipe['nutrition_facts']['protein']),
        'cholesterol' : float(recipe['nutrition_facts']['cholesterol']),
        'sodium' : float(recipe['nutrition_facts']['sodium']),
        'recipe_categories' : recipe['recipe_categories'] 
    }
    itemsArr.append(item)

print("+ Indian Main Dishes Veg : " ,len(itemsArr))


#IndianMainDishes - Non-Veg
col = db.IndianMainDishes
nonveg = col.find_one({'category':'Non-Veg'})
recipes = nonveg['recipes']
for recipe in recipes:
    # print(recipe['recipe_name'])
    item = {
        'recipe_name' : recipe['recipe_name'],
        'recipe_type' : 'Non-Veg',
        'category' : 'IndianMainDishes',
        'ratings' : recipe['ratings'],
        'ingredients' : recipe['ingredients'],
        'time_required' : recipe['time_required'],
        'calories' : float(recipe['nutrition_facts']['calories']),
        'fat' : float(recipe['nutrition_facts']['fat']),
        'carbohydrates' : float(recipe['nutrition_facts']['carbohydrates']),
        'protein' : float(recipe['nutrition_facts']['protein']),
        'cholesterol' : float(recipe['nutrition_facts']['cholesterol']),
        'sodium' : float(recipe['nutrition_facts']['sodium']),
        'recipe_categories' : recipe['recipe_categories'] 
    }
    itemsArr.append(item)

print("+ Indian Main Dishes Non-Veg : " ,len(itemsArr))



#Indian Breads
col = db.IndianBreads
recipes = col.find()
for recipe in recipes:
    # print(recipe['recipe_name'])
    recipe_type = 'Veg'
    if('Non-Veg' in recipe['recipe_categories'] or 'Egg' in recipe['recipe_categories']):
        recipe_type = 'Non-Veg'
    item = {
        'recipe_name' : recipe['recipe_name'],
        'recipe_type' : recipe_type,
        'category' : 'IndianBreads',
        'ratings' : recipe['ratings'],
        'ingredients' : recipe['ingredients'],
        'time_required' : recipe['time_required'],
        'calories' : float(recipe['nutrition_facts']['calories']),
        'fat' : float(recipe['nutrition_facts']['fat']),
        'carbohydrates' : float(recipe['nutrition_facts']['carbohydrates']),
        'protein' : float(recipe['nutrition_facts']['protein']),
        'cholesterol' : float(recipe['nutrition_facts']['cholesterol']),
        'sodium' : float(recipe['nutrition_facts']['sodium']),
        'recipe_categories' : recipe['recipe_categories'] 
    }
    itemsArr.append(item)


print("+ Indian Breads : " ,len(itemsArr))

#Indian Desserts
col = db.IndianDesserts
recipes = col.find()
for recipe in recipes:
    # print(recipe['recipe_name'])
    recipe_type = 'Veg'
    if('Non-Veg' in recipe['recipe_categories'] or 'Egg' in recipe['recipe_categories']):
        recipe_type = 'Non-Veg'
    item = {
        'recipe_name' : recipe['recipe_name'],
        'recipe_type' : recipe_type,
        'category' : 'IndianDesserts',
        'ratings' : recipe['ratings'],
        'ingredients' : recipe['ingredients'],
        'time_required' : recipe['time_required'],
        'calories' : float(recipe['nutrition_facts']['calories']),
        'fat' : float(recipe['nutrition_facts']['fat']),
        'carbohydrates' : float(recipe['nutrition_facts']['carbohydrates']),
        'protein' : float(recipe['nutrition_facts']['protein']),
        'cholesterol' : float(recipe['nutrition_facts']['cholesterol']),
        'sodium' : float(recipe['nutrition_facts']['sodium']),
        'recipe_categories' : recipe['recipe_categories'] 
    }
    itemsArr.append(item)


print("+ Indian Desserts : " ,len(itemsArr))


with open('dataset.csv','w', newline='', encoding='utf-8') as f:
    fieldnames = ['recipe_name','recipe_type','category','ratings','ingredients','time_required','calories','fat','carbohydrates','protein','cholesterol','sodium','recipe_categories']

    thewriter = csv.DictWriter(f,fieldnames=fieldnames)

    thewriter.writeheader()
    thewriter.writerows(itemsArr)





