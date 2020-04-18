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
        router.get('/:email', function(req,res){
            const query = {email : req.params.email}
            collection.find(query).toArray(function(err,result){
                if(err) throw err;
                const nodeToFlask = {
                    calorieCount : result[0].calorieCount
                }
                console.log(nodeToFlask)

                var options = {
                    method: 'POST',
                    uri: 'http://localhost:3000/nodeFlask/demo@gmail.com',
                    body: nodeToFlask,
                    json: true // Automatically stringifies the body to JSON
                };

                var returndata;
                var sendrequest = request(options)
                .then(function (parsedBody) {
                    console.log(parsedBody); // parsedBody contains the data sent back from the Flask server
                    returndata = parsedBody; // do something with this data, here I'm assigning it to a variable.
                })
                .catch(function (err) {
                    console.log(err);
                });
                
                res.status(200).send(JSON.stringify(returndata))
                

            })
          
        })

    }
})
module.exports = router;