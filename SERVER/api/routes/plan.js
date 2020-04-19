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

        router.get('getPlan/:email',(req,res) =>{
            const query = {email : req.params.email}
            const mealType = req.params.mealType
            console.log(query)
            collection.find(query,{projection: {_id:0,plan : 1}}).toArray((err,result)=>{
                // data = result
                console.log(result[0])
                dataToSend = { plan : result[0].plan}
                res.status(200).send(JSON.stringify(dataToSend))

            })  

        })

        router.get('setPlan/:email',(req,res) =>{
            const query = {email : req.params.email}
            newvalues = { $set: {plan : req.body.plan } };
            const mealType = req.params.mealType
            console.log(query)
            collection.updateOne(query, newvalues, function(err, resultUpdate) {
                if (err) throw err;
                console.log("plan status updated");
                res.status(200).send(JSON.stringify({ plan : req.body.plan}))
            });

        })

    }
})


module.exports = router; 