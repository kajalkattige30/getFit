from pymongo import MongoClient as mongo
import bson

cluster = mongo("mongodb+srv://Janhavi:mongodb@projectcluster-azpnv.mongodb.net/test?retryWrites=true&w=majority")
db = cluster.ProjectDB
col = db.Search


# Appetizers - Veg
# colAppetizer = db.Appetizers
# vegAppetizers = colAppetizer.find_one({'category':'Veg'})
# vegRecipes = vegAppetizers['recipes']
# for recipe in vegRecipes:
#     item = dict()
#     print(recipe['recipe_name'])
#     nutritionFacts = recipe['nutrition_facts']
#     print(nutritionFacts['calories'])
#     item['recipe_name'] = recipe['recipe_name']
#     item['calories'] = recipe['nutrition_facts']['calories']
#     item['category'] = 'Veg'
#     item['collection'] = 'Appetizers'
#     item['_id'] = bson.objectid.ObjectId()
#     col.insert_one(item)


# colAppetizer = db.Appetizers
# nonvegAppetizers = colAppetizer.find_one({'category':'Non-Veg'})
# nonvegRecipes = nonvegAppetizers['recipes']
# for recipe in nonvegRecipes:
#     item = dict()
#     print(recipe['recipe_name'])
#     nutritionFacts = recipe['nutrition_facts']
#     print(nutritionFacts['calories'])
#     item['recipe_name'] = recipe['recipe_name']
#     item['calories'] = recipe['nutrition_facts']['calories']
#     item['category'] = 'Non-Veg'
#     item['collection'] = 'Appetizers'
#     item['_id'] = bson.objectid.ObjectId()
#     print(item)
#     col.insert_one(item)

# Indian Main Dish - Veg
# colMainDish = db.IndianMainDishes
# vegMainDish = colMainDish.find_one({'category':'Veg'})
# vegRecipes = vegMainDish['recipes']
# for recipe in vegRecipes:
#     item = dict()
#     print(recipe['recipe_name'])
#     nutritionFacts = recipe['nutrition_facts']
#     print(nutritionFacts['calories'])
#     item['_id'] = bson.objectid.ObjectId()
#     item['recipe_name'] = recipe['recipe_name']
#     item['calories'] = recipe['nutrition_facts']['calories']
#     item['category'] = 'Veg'
#     item['collection'] = 'IndianMainDishes'
#     print(item)
#     col.insert_one(item)

# colMainDish = db.IndianMainDishes
# vegMainDish = colMainDish.find_one({'category':'Non-Veg'})
# vegRecipes = vegMainDish['recipes']
# for recipe in vegRecipes:
#     item = dict()
#     print(recipe['recipe_name'])
#     nutritionFacts = recipe['nutrition_facts']
#     print(nutritionFacts['calories'])
#     item['_id'] = bson.objectid.ObjectId()
#     item['recipe_name'] = recipe['recipe_name']
#     item['calories'] = recipe['nutrition_facts']['calories']
#     item['category'] = 'Non-Veg'
#     item['collection'] = 'IndianMainDishes'
#     print(item)
#     col.insert_one(item)

# colIndianBread = db.IndianBreads.find()
# for recipe in colIndianBread:
#     item = dict()
#     print(recipe['recipe_name'])
#     item['_id'] = bson.objectid.ObjectId()
#     item['recipe_name'] = recipe['recipe_name']
#     item['calories'] = recipe['nutrition_facts']['calories']
#     if('Veg' in recipe['recipe_categories']):
#         item['category'] = 'Veg'
#     elif('Non-Veg' in recipe['recipe_categories']):
#         item['category'] = 'Non-Veg'
#     item['collection'] = 'IndianBreads'
#     print(item)
#     col.insert_one(item)

colIndianDesserts = db.IndianDesserts.find()
for recipe in colIndianDesserts:
    item = dict()
    print(recipe['recipe_name'])
    item['_id'] = bson.objectid.ObjectId()
    item['recipe_name'] = recipe['recipe_name']
    item['calories'] = recipe['nutrition_facts']['calories']
    if('Veg' in recipe['recipe_categories']):
        item['category'] = 'Veg'
    elif('Non-Veg' in recipe['recipe_categories']):
        item['category'] = 'Non-Veg'
    item['collection'] = 'IndianDesserts'
    print(item)
    col.insert_one(item)