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

        router.post('/',(req,res)=>{
            const query = {
                email: req.body.email,
                password: req.body.password
            }

            collection.findOne(query, (err,result)=>{
                if(result!=null){
                    const ObjToSend = {
                        name: result.name,
                        email: result.email
                    }
                    console.log('Registered User')
                    res.status(200).send(JSON.stringify(ObjToSend))
                }
                else{
                    res.status(400).send()
                }
            })
        })
   
    }

});
module.exports = router;