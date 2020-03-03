from pymongo import MongoClient as mongo
import bson

cluster = mongo("mongodb+srv://Janhavi:mongodb@projectcluster-azpnv.mongodb.net/test?retryWrites=true&w=majority")

demoPost = {'_id':bson.objectid.ObjectId(),'recipe_name': 'Barbecued Beef', 'ratings': '4.65193367004395', 'ingredients': ['1 1/2 cups ketchup', '1/4 cup packed brown sugar', '1/4 cup red wine vinegar', '2 tablespoons prepared Dijon-style mustard', '2 tablespoons Worcestershire sauce', '1 teaspoon liquid smoke flavoring', '1/2 teaspoon salt', '1/4 teaspoon ground black pepper', '1/4 teaspoon garlic powder', '1 (4 pound) boneless chuck roast'], 'time_required': '10 h 20 m', 'directions': ['In a large bowl, combine ketchup, brown sugar, red wine vinegar, Dijon-style mustard, Worcestershire sauce, and liquid smoke. Stir in salt, pepper, and garlic powder.', 'Place chuck roast in a slow cooker. Pour ketchup mixture over chuck roast. Cover, and cook on Low for 8 to 10 hours.', 'Remove chuck roast from slow cooker, shred with a fork, and return to the slow cooker. Stir meat to evenly coat with sauce. Continue cooking approximately 1 hour.'], 'nutrition_facts': {'calories': '276', 'fat': '16.2', 'carbohydrates': '13.5', 'protein': '18.7', 'cholesterol': '65', 'sodium': '562'}, 'img_url': 'https://images.media-allrecipes.com/userphotos/560x315/416539.jpg', 'recipe_categories': ['Veg', 'Beef', 'Breakfast', 'Indian', 'Snacks']}

# post2 = {'Category':'Appetizers','Veg':[],'Non-Veg':[]}
post3 = {'category':'Veg','recipes':[]}
db = cluster.demoDB
# cluster['demoDB']
demoCol = db.demoCollection
print(demoCol)
# demoCol.insert_one(post3)
demoCol.update_one({'category':'Veg'},{'$push' : {'recipes' : demoPost}})
# demoCol['Veg'].insert_one(demoPost)

# results = demoCol.find({'recipe_name':'Barbecued Beef'})

# print(results)
# for item in results:
#     print(item)