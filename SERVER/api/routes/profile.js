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

        router.put('/', (req,res) => {
            const existingUser = {
                email : req.body.email,
                name : req.body.name,
                height : req.body.height,
                current_weight : req.body.current_weight,
                activity_level : req.body.activity_level,
                gender : req.body.gender,
                age : req.body.age,
                goal_weight : req.body.goal_weight,
                bmi : req.body.bmi,
                bmr : req.body.bmr,
                calorieCount : req.body.calorieCount
            }
            console.log(existingUser)
            const query = {email : existingUser.email}
            var updatedDetails = { $set: {height: existingUser.height,
                                          current_weight : existingUser.current_weight,
                                          activity_level: existingUser.activity_level,
                                          gender: existingUser.gender,
                                          age: existingUser.age,
                                          goal_weight: existingUser.goal_weight,
                                           

            }

            }
            collection.updateOne(query, updatedDetails, function(err,res){
                if(err) throw err;
                console.log("Details updated!")
                db.close();
            });
            router.get('/:email',(req,res) =>{
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
            collection.find(q,function(err, ans) {
                if(err) throw err;
                console.log(ans)
                db.close();
            })
                    
                
            });
            res.status(200).send(JSON.stringify(existingUser))

        })
    }
})
module.exports = router;

