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

        router.post('/', (req,res)=>{
            console.log('at signup')
            const newUser = {
                name: req.body.name,
                email: req.body.email,
                password: req.body.password
            }

            const query = { email: newUser.email }
            collection.findOne(query, (err,result)=>{
                if(result == null){
                    collection.insertOne(newUser,(err,result)=>{
                        res.status(200).send()
                        console.log('Sign up successful')
                    })
                }
                else{
                    console.log('Already Registered')
                    res.status(400).send()
                }
            })
        })

    }
})
module.exports = router;