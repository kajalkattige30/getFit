#Scraping Appetizers

from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
from pymongo import MongoClient as mongo
import bson

def scrapData(my_url):
    recipe = ''
    #opening up connection and grabbing the page
    uClient = uReq(my_url)
    page_html = uClient.read()
    uClient.close()
    page_soup = soup(page_html,"html.parser")
    if(page_soup.find('h1',{'id':'recipe-main-content'})!=None):
        recipe = scrapDataType2(page_soup)
    else:
        recipe = scrapDataType1(page_soup)
    print(recipe)
    return recipe

def scrapDataType1(page_soup):

    recipe = {}
    recipe_categories = set()
    recipe_categories.add('Indian')
    recipe_categories.add('Indian Main Dishes')

    #scraping basic information
    recipe_name = page_soup.find('h1',{'class':'heading-content'}).text
    recipe['recipe_name'] = recipe_name
    recipe_name = recipe_name.lower()
    if('samosa' in recipe_name):
        recipe_categories.add('Samosa')
    if('vegan' in recipe_name):
        recipe_categories.add('Vegan')
    if('beef' in recipe_name):
        recipe_categories.add('Beef')
        recipe_categories.add('Non-Veg')
    print(recipe_name)
    ratings = page_soup.find('span',{'class':'review-star-text'}).text.split()[1]
    recipe['ratings'] = ratings
    print(ratings)
    time = page_soup.find('div',{'class':'two-subcol-content-wrapper'})
    items_list = time.findAll('div',{'class':'recipe-meta-item-body'})
    time_list = []
    for item in items_list:
        item_text = item.text.replace('\n',' ')
        time_list.append(item_text.strip(' '))
    print(time_list)
    recipe['time_required'] = time_list[2]
    ingredients_section = page_soup.find('ul',{'class':'ingredients-section'})
    ingredients_items = ingredients_section.findAll('li',{'class':'ingredients-item'})
    ingredients = []
    for item in ingredients_items:
        ingredient = item.text.strip().lower()
        if('beef' in ingredient):
            recipe_categories.add('Beef')
            recipe_categories.add('Non-Veg')
        if('chicken' in ingredient):
            recipe_categories.add('Non-Veg')
        if('egg' in ingredient):
            recipe_categories.add('Egg')
        ingredients.append(ingredient)
    print(ingredients)
    recipe['ingredients'] = ingredients

    instruction_section = page_soup.find('ul',{'class':'instructions-section'})
    instruction_items = instruction_section.findAll('li',{'class':'instructions-section-item'})
    directions = []
    for item in instruction_items:
        item_text = item.div.text.replace('\n',' ')
        directions.append(item_text.strip())
    print(directions)
    recipe['directions'] = directions

    nutrition_section = page_soup.find('div',{'class':'recipe-nutrition-section'})
    nutrition_facts_text = nutrition_section.find('div',{'class':'section-body'}).text
    nutrition_facts_list = nutrition_facts_text.replace('sodium.','sodium;').replace('total fat','fat').split(';')
    for i in range(len(nutrition_facts_list)):
        nutrition_facts_list[i] = nutrition_facts_list[i].strip().split()
    nutrition_facts_list.pop()
    print(nutrition_facts_list)
    recipe_nutrition = {}
    for item in nutrition_facts_list:
        # item = item.split()
        amount = item[0]
        recipe_nutrition[item[-1]] = amount 
    print(recipe_nutrition)
    recipe['nutrition_facts'] = recipe_nutrition

    img_container = page_soup.find('div',{'class':'image-container'})
    img_url = img_container.find('div',{'class':'lazy-image'})['data-src']
    print(img_url)
    recipe['img_url'] = img_url
    if('Non-Veg' not in recipe_categories and 'Egg' not in recipe_categories):
        recipe_categories.add('Veg')
    recipe['recipe_categories'] = list(recipe_categories)

    return recipe

def scrapDataType2(page_soup):
    recipe = {}

    recipe_categories = set()
    recipe_categories.add('Indian')
    recipe_categories.add('Indian Main Dishes')
    #scraping basic information
    recipe_name = page_soup.find('h1',{'id':'recipe-main-content'}).text
    recipe['recipe_name'] = recipe_name
    recipe_name = recipe_name.lower()
    if('samosa' in recipe_name):
        recipe_categories.add('Samosa')
    if('vegan' in recipe_name):
        recipe_categories.add('Vegan')
    if('beef' in recipe_name):
        recipe_categories.add('Beef')
        recipe_categories.add('Non-Veg')
    ratings = page_soup.find('div',{'class':'rating-stars'})["data-ratingstars"]
    recipe['ratings'] = ratings
    # submitter_description = page_soup.find('div',{'class':'submitter__description'}).text
    # ready_in_time = page_soup.find('span',{'class':'ready-in-time'}).text
    # calories = page_soup.find('span',{'class':'calorie-count'}).text
    print(recipe_name)
    print(ratings)
    # print(submitter_description)
    # print([ready_in_time,calories])
    # print(servings)

    # scraping ingredients

    ingredients_column_1 = page_soup.find('ul',{'id':"lst_ingredients_1"})
    # print(ingredients_column_1)
    list_1 = ingredients_column_1.findAll('li',{'class':'checkList__line'})
    ingredients = []
    for ingredient in list_1:
        ingredients.append(ingredient.span.text)
    ingredients_column_2 = page_soup.find('ul',{'id':"lst_ingredients_2"})
    # print(ingredients_column_2)
    list_2 = ingredients_column_2.findAll('li',{'class':'checkList__line'})
    for ingredient in list_2:
        text = ingredient.span.text.lower()
        if('beef' in text):
            recipe_categories.add('Beef')
            recipe_categories.add('Non-Veg')
        if('chicken' in text):
            recipe_categories.add('Non-Veg')
        if('egg' in text):
            recipe_categories.add('Egg') 
            recipe_categories.add('Non_Veg')      
        ingredients.append(text)

    ingredients.pop()
    print(ingredients)
    recipe['ingredients'] = ingredients
    # recipe_nutrition = page_soup.find('div',{'class':'ngdialog'})
    # print(recipe_nutrition)

    # prep_time = page_soup.find('time',{'itemprop':'prepTime'}).span.text
    # print(prep_time)

    # cook_time = page_soup.find('time',{'itemprop':'cookTime'}).span.text
    # print(cook_time)

    total_time = page_soup.find('time',{'itemprop':'totalTime'}).span.text
    print(total_time)
    recipe['time_required'] = total_time
    directions_html = page_soup.find('ol',{'class':'list-numbers recipe-directions__list'})
    directions_list_html = directions_html.findAll('li',{'class':'step'})
    directions = []

    for step in directions_list_html:
        directions.append(step.text.strip())

    print(directions)
    recipe['directions'] = directions
    recipe_nutrition = dict()

    #Scraping Nutritional Information
    nutrition_facts_html = page_soup.find('div',{'class':'nutrition-summary-facts'})

    recipe_nutrition['calories'] = nutrition_facts_html.find('span',{'itemprop':'calories'}).text.split(" ")[0]
    recipe_nutrition['fat'] = nutrition_facts_html.find('span',{'itemprop':'fatContent'}).text.split(" ")[0]
    recipe_nutrition['carbohydrates'] = nutrition_facts_html.find('span',{'itemprop':'carbohydrateContent'}).text.split(" ")[0]
    recipe_nutrition['protein'] = nutrition_facts_html.find('span',{'itemprop':'proteinContent'}).text.split(" ")[0]
    recipe_nutrition['cholesterol'] = nutrition_facts_html.find('span',{'itemprop':'cholesterolContent'}).text.split(" ")[0]
    recipe_nutrition['sodium'] = nutrition_facts_html.find('span',{'itemprop':'sodiumContent'}).text.split(" ")[0]

    print(recipe_nutrition)
    recipe['nutrition_facts'] = recipe_nutrition
    img_url = page_soup.find('img',{'class':'rec-photo'})['src']
    print(img_url)
    recipe['img_url'] = img_url
    if('Non-Veg' not in recipe_categories and 'Egg' not in recipe_categories):
        recipe_categories.add('Veg')
    recipe['recipe_categories'] = list(recipe_categories)
    return recipe

def dataIntoMongoDB(appetizers):
    cluster = mongo("mongodb+srv://Janhavi:mongodb@projectcluster-azpnv.mongodb.net/test?retryWrites=true&w=majority")
    db = cluster.ProjectDB
    col = db.IndianMainDishes
    Veg = {'category':'Veg','recipes':[]} 
    Non_Veg = {'category':'Non-Veg','recipes':[]}
    col.insert_one(Veg)
    col.insert_one(Non_Veg)
    for recipe in appetizers['Veg']:
        recipe['_id'] = bson.objectid.ObjectId()
        col.update_one({'category':'Veg'},{'$push' : {'recipes' : recipe}})
    for recipe in appetizers['Non-Veg']:
        recipe['_id'] = bson.objectid.ObjectId()
        col.update_one({'category':'Non-Veg'},{'$push' : {'recipes' : recipe}})
    # for recipe in recipes:
    #     recipe['_id'] = bson.objectid.ObjectId()
    #     if('Veg' in recipe['recipe_categories']):
    #         col.update_one({'category':'Veg'},{'$push' : {'recipes' : recipe}})
    #     else:
    #         col.update_one({'category':'Non-Veg'},{'$push' : {'recipes' : recipe}})


appetizers = {}
# appetizers['Category'] = 'Appetizers'
appetizers['Veg'] = []
appetizers['Non-Veg'] = []
for i in range(3):

    url = "https://www.allrecipes.com/recipes/17136/world-cuisine/asian/indian/main-dishes/?internalSource=hub%20nav&referringId=233&referringContentType=Recipe%20Hub&linkName=hub%20nav%20daughter&clickId=hub%20nav%202&page="+str(i+1)

    uClient = uReq(url)
    page_html = uClient.read()
    uClient.close()
    grid_page_soup = soup(page_html,"html.parser")
    grid_html = grid_page_soup.find('section',{'id':'fixedGridSection'})
    # print(grid_html)
    recipe_cards_html = grid_html.findAll('article',{'class':'fixed-recipe-card'}) 
    print(len(recipe_cards_html))
    for recipe_card in recipe_cards_html:
        try:
            link = recipe_card.find('div',{'class':'grid-card-image-container'}).a['href']
            print(link)
            data = scrapData(link)
            if('Beef' in data['recipe_categories']):
                continue
            if('Non-Veg' in data['recipe_categories']):
                appetizers['Non-Veg'].append(data)
            else:
                appetizers['Veg'].append(data)
            # recipes.append(scrapData(link))
        except:
            continue

dataIntoMongoDB(appetizers)

# url = "https://www.allrecipes.com/recipe/14646/barbecued-beef/?internalSource=hub%20recipe&referringContentType=Search&clickId=cardslot%205"
# scrapData(url)

