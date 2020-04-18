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
        router.get('/:email',async function(req,res){
            const query = {email : req.params.email}
            collection.find(query).toArray(function(err,result){
                if(err) throw err;
                const nodeToFlask = {
                    calorieCount : result[0].calorieCount
                }
                res.status(200).send(JSON.stringify(nodeToFlask))

            })
          
        })

    }
})
