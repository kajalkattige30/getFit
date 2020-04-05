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

        router.post('/:email', (req,res) =>{
            const existingUser = {
                email = req.body.email,
                height = req.body.height,
                current_weight = req.body.current_weight,
                activity_level = req.body.activity_level,
                gender = req.body.gender,
                age = req.body.age,
                goal_weight = req.body.goal_weight
            }
            existingUser = user.findById(req.params.email)
            const addedDetails = {
                height = existingUser.height,
                current_weight = existingUser.current_weight,
                activity_level = existingUser.activity_level,
                gender = existingUser.gender,
                age = existingUser.age,
                goal_weight = existingUser.goal_weight
            }
            res.status(200).send(JSON.stringify(addedDetails))
            if(existingUser == null){
                console.log("User doesn't exist!")
                res.redirect('/')
            }

        })
    }
});
module.exports = router;