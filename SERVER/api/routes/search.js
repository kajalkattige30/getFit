const express = require('express');
const router = express.Router();
const mongoClient = require('mongodb').MongoClient;

const url = "mongodb+srv://Janhavi:mongodb@projectcluster-azpnv.mongodb.net/test?retryWrites=true&w=majority";

mongoClient.connect(url, (err,db)=>{
    if(err){
        console.log('Error while connecting mongoClient')
    }
    else{
        const myDB = db.db('ProjectDB')
        const collection = myDB.collection('user')
        const Search = myDB.collection('Search')
        
        router.get('/',(req,res)=>{
            let foodItems = []
            Search.find().toArray((err,result)=>{
                if(err){
                    console.log('Error fetching Search data')
                }
                else{
                    console.log(result)
                    res.status(200).send(result)
                }
            })
        })


        .get('/:collection/:category/:foodItem',(req,res)=>{
            let collection = req.params.collection
            let foodcategory = req.params.category
            let foodItem = req.params.foodItem
            console.log(collection)
            console.log(foodcategory)
            console.log(foodItem)
            const db = myDB.collection(collection)
            let recipe_details = {
                    recipe_name : foodItem,
                    collection : collection,
                    category : foodcategory
            }
            if(collection == "IndianBreads" || collection == "IndianDesserts"){
                
                console.log(db)

                db.find({recipe_name:foodItem}).toArray((err,result)=>{
                    if(err){
                        console.log('Error fetching Bread and Dessert data')
                    }
                    // console.log(result)
                    // res.status(200).send(result)
                    recipe_details.calories = result[0].nutrition_facts.calories
                    recipe_details.carbohydrates = result[0].nutrition_facts.carbohydrates
                    recipe_details.fats = result[0].nutrition_facts.fats
                    recipe_details.protein = result[0].nutrition_facts.protein
                    recipe_details.img_url = result[0].img_url
                    res.status(200).send(recipe_details)
                })
            } else if(collection == "Appetizers" || collection == "IndianMainDishes"){
                db.find({category:foodcategory}).toArray((err,result)=>{
                    if(err){
                        console.log('Error fetching Appetizers and Main Dish data')
                    }
                    foodArray = result[0]
                    recipes = foodArray['recipes']
                    recipes.forEach(recipe =>{
                        if(foodItem == recipe.recipe_name){
                            recipe_details.calories = recipe.nutrition_facts.calories
                            recipe_details.carbohydrates = recipe.nutrition_facts.carbohydrates
                            recipe_details.fats = recipe.nutrition_facts.fats
                            recipe_details.protein = recipe.nutrition_facts.protein    
                            recipe_details.img_url = recipe.img_url                       
                        }
                    })
                    res.status(200).send(recipe_details)
                })
            }

        })

        

    }
})

module.exports = router;