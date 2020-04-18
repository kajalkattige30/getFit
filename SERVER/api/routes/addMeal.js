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
        
        router.post('/:email/:mealType',(req,res) =>{
            const query = {email : req.params.email}
            const data = {
                recipeName : req.body.recipeName,
                caloriesCount : req.body.caloriesCount,
                carbs : req.body.carbs,
                fats : req.body.fats,
                protein : req.body.protein
            }
            const mealType = req.params.mealType
            console.log(query)
            collection.find(query,{projection: {_id:0,breakfastMeals:1 , lunchMeals:1, dinnerMeals:1}}).toArray((err,result)=>{
                // data = result
                console.log(result[0])
                let newvalues = ""
                if(mealType == 'Breakfast'){
                    result[0].breakfastMeals.push({recipeName : data.recipeName, caloriesCount : data.caloriesCount, carbs : data.carbs, fats : data.fats, protein : data.protein})
                    newvalues = { $set: {breakfastMeals: result[0].breakfastMeals } };
                }
                else if(mealType == 'Lunch'){
                    result[0].lunchMeals.push({recipeName : data.recipeName, caloriesCount : data.caloriesCount, carbs : data.carbs, fats : data.fats, protein : data.protein})
                    newvalues = { $set: {lunchMeals: result[0].lunchMeals } };
                }
                else{
                    result[0].dinnerMeals.push({recipeName : data.recipeName, caloriesCount : data.caloriesCount, carbs : data.carbs, fats : data.fats, protein : data.protein})
                    newvalues = { $set: {dinnerMeals: result[0].dinnerMeals } };
                }

                
                collection.updateOne(query, newvalues, function(err, resultUpdate) {
                    if (err) throw err;
                    console.log("meal status updated");
                    res.status(200).send(JSON.stringify(data))
                });
            })  
            
        })

    }
})


module.exports = router;