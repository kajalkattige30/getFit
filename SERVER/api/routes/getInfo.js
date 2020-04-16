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
        router.get('/calorieMacros', (req,res) => {
            const userCalorieInfo = {
                email: req.body.email,
                
            }
            console.log(userCalorieInfo)
            const query = {email: userCalorieInfo.email}
            var data = ""
            myDB.collection('user').find({query}).toArray(function(err,result){
                //if(err) throw err;
                data = result

                console.log(result)
                db.close();
            })
            res.status(200).send(JSON.stringify(data))

        })
        
        
        
    }
})
        

        
            




module.exports = router;