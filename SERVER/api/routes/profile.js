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

        router.put('/:email', (req,res) => {
            const existingUser = {
                name : req.body.name,
                height : req.body.height,
                current_weight : req.body.current_weight,
                activity_level : req.body.activity_level,
                age : req.body.age,
                goal_weight : req.body.goal_weight,
                
            }
            console.log(existingUser)
            const query = {email : req.params.email}
            var updatedDetails = { $set: {height: existingUser.height,
                                          name : existingUser.name,
                                          current_weight : existingUser.current_weight,
                                          activity_level: existingUser.activity_level,
                                          age: existingUser.age,
                                          goal_weight: existingUser.goal_weight,
                                           

            }

            }
            collection.updateOne(query, updatedDetails, function(err,res){
                if(err) throw err;
                console.log("Details updated!")
            });
            
            res.status(200).send()

        })
        router.get('/:email',(req,res) =>{
            // const myDB = db.db('ProjectDB')
            // const collection = myDB.collection('user')
                // res.status(200).json({
                //     email : existingUser.email,
                //     name : existingUser.name,
                //     height :  existingUser.height,
                //     current_weight : existingUser.current_weight,
                //     activity_level : existingUser.activity_level,
                //     gender : existingUser.gender,
                //     age : existingUser.age,
                //     goal_weight : existingUser.goal_weight,
                //     bmi : existingUser.bmi,
                //     bmr : existingUser.bmr,
                //     calorieCount : existingUser.calorieCount

                // });

        const q = {email : req.params.email}
        collection.find(q, ).toArray(function(err, ans) {
            if(err) throw err;
            console.log(ans[0])
            const objToSend = {
                current_weight : ans[0].current_weight,
                height : ans[0].height,
                name : ans[0].name,
                age : ans[0].age,
                goal_weight : ans[0].goal_weight,
                activity_level : ans[0].activity_level
            }
            console.log(objToSend)
            res.status(200).send(JSON.stringify(objToSend))
            
        })
        
                
            
        });
    }
})
module.exports = router;

