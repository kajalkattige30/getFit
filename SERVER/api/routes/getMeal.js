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

        router.get('/:email/:mealType',(req,res) =>{
            const query = {email : req.params.email}
            // const data = {
            //     recipeName : req.body.recipeName,
            //     caloriesCount : req.body.caloriesCount
            // }
            const mealType = req.params.mealType
            console.log(query)
            let dataToSend = ""
            collection.find(query,{projection: {_id:0,breakfastMeals:1 , lunchMeals:1, dinnerMeals:1}}).toArray((err,result)=>{
                // data = result
                console.log(result[0])
                let newvalues = ""
                if(mealType == 'Breakfast'){

                    dataToSend = result[0].breakfastMeals;
                }
                else if(mealType == 'Lunch'){
                    dataToSend = result[0].lunchMeals;
                }
                else{
                    dataToSend = result[0].dinnerMeals;
                }

                res.status(200).send(JSON.stringify(dataToSend))

            })  

        })

    }
})


module.exports = router; 