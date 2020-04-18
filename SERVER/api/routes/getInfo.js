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
        router.get('/calorieMacros/:email', (req,res) => {
            const userCalorieInfo = {
                email: req.params.email,
            }
          
            console.log(userCalorieInfo)
            const query = {email: userCalorieInfo.email}
            var data = ""
            var carbs = ""
            var proteins = ""
            var fats = ""
            var carbsg = ""
            var proteinsg = ""
            var fatsg = ""
            var macros = ""
            var eatenCalories = 0
            var eatenCarbs = 0
            var eatenFats = 0
            var eatenProtein = 0
            myDB.collection('user').find(query, {projection: {_id:0,current_weight:1 , goal_weight:1, calorieCount:1,breakfastMeals : 1, lunchMeals : 1, dinnerMeals : 1}}).toArray(function(err,result){
                //if(err) throw err;
                
                data = Object.assign({},result[0])
                console.log(data)
                if(data.current_weight == data.goal_weight){
                    carbs = 0.55*data.calorieCount
                    proteins = 0.2*data.calorieCount
                    fats = 0.25*data.calorieCount
                    carbsg = carbs/4.1
                    proteinsg = proteins/4.1
                    fatsg = fats/8.8
                    macros = {
                        cal : data.calorieCount,
                        c : carbsg,
                        p : proteinsg,
                        f : fatsg
                    }
                    console.log(macros)

                }
                if(data.current_weight > data.goal_weight){
                    carbs = 0.4*data.calorieCount
                    proteins = 0.3*data.calorieCount
                    fats = 0.25*data.calorieCount
                    carbsg = carbs/4.1
                    proteinsg = proteins/4.1
                    fatsg = fats/8.8
                    macros = {
                        cal : data.calorieCount,

                        c : carbsg,
                        p : proteinsg,
                        f : fatsg
                    }
                    console.log(macros)
                }
                if(data.current_weight < data.goal_weight){
                    carbs = 0.6*data.calorieCount
                    proteins = 0.2*data.calorieCount
                    fats = 0.2*data.calorieCount
                    carbsg = carbs/4.1
                    proteinsg = proteins/4.1
                    fatsg = fats/8.8
                    macros = {
                        cal : data.calorieCount,

                        c : carbsg,
                        p : proteinsg,
                        f : fatsg
                    }
                    console.log(macros)

                }
                
                for(i=0;i<data.breakfastMeals.length;i++){
                    eatenCalories+=data.breakfastMeals[i].caloriesCount
                    eatenCarbs+=data.breakfastMeals[i].carbs
                    eatenFats+=data.breakfastMeals[i].fats
                    eatenProtein+=data.breakfastMeals[i].protein
                }
                for(i=0;i<data.lunchMeals.length;i++){
                    eatenCalories+=data.lunchMeals[i].caloriesCount
                    eatenCarbs+=data.lunchMeals[i].carbs
                    eatenFats+=data.lunchMeals[i].fats
                    eatenProtein+=data.lunchMeals[i].protein
                }
                for(i=0;i<data.dinnerMeals.length;i++){
                    eatenCalories+=data.dinnerMeals[i].caloriesCount
                    eatenCarbs+=data.dinnerMeals[i].carbs
                    eatenFats+=data.dinnerMeals[i].fats
                    eatenProtein+=data.dinnerMeals[i].protein
                }

                macros['eatenCalories'] = eatenCalories
                macros['eatenCarbs'] = eatenCarbs
                macros['eatenFats'] = eatenFats
                macros['eatenProtein'] = eatenProtein
                res.status(200).send(JSON.stringify(macros))

            })
            console.log(macros)


        })
        
    }
})


module.exports = router;