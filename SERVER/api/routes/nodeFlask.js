const express = require('express');
const router = express.Router();
const mongoClient = require('mongodb').MongoClient;
const request = require('request-promise');
const axios = require('axios')
const request2 = require('request')
const request3 = require('sync-request')
const fs = require('fs')

const url = "mongodb+srv://Janhavi:mongodb@projectcluster-azpnv.mongodb.net/test?retryWrites=true&w=majority";

mongoClient.connect(url, (err,db)=>{
    if(err){
        console.log('Error while connecting mongoClient')
    }
    else{
        const myDB = db.db('ProjectDB')
        const collection = myDB.collection('user')
        router.get('/:email',function(req,response){
            const query = {email : req.params.email}
            collection.find(query).toArray(function(err,result){
                if(err) throw err;
                const nodeToFlask = {
                        calorieCount : result[0].calorieCount
                    }
                var data = JSON.stringify(nodeToFlask)
                fs.writeFileSync('C:/Users/Janhavi Dubule/Desktop/BE Project/getFit/models/dataToMl.json',data)
                try{
                    axios
                    .post('http://127.0.0.1:5000/nodeFlask', nodeToFlask)
                    .then(res => {
                        console.log(`statusCode: ${res.statusCode}`)
                        // console.log(res)
                        var returndata = fs.readFileSync("C:/Users/Janhavi Dubule/Desktop/BE Project/getFit/models/recommendation.json");
                        var recommended_meals = JSON.parse(returndata);
                        //C:/Users/Janhavi Dubule/Desktop/BE Project/getFit/SERVER/api/recommendation.json
                        //C:/Users/kkatt/Documents/BE_Project/getFit/SERVER/api/recommendation.json
                        console.log(recommended_meals)
                        response.status(200).send(JSON.stringify(recommended_meals))
                    })
                    .catch(err => {
                        console.log(err)
                    })
                }
                catch(error){
                    console.log(error)
                }

        })
        })
    }
})


module.exports = router;
