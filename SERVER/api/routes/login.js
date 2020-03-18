const express = require('express');
const router = express.Router();
const MongoClient = require('mongodb').MongoClient;
var users = ""
const uri = "mongodb+srv://Janhavi:mongodb@projectcluster-azpnv.mongodb.net/test?retryWrites=true&w=majority";
const client = new MongoClient(uri, { useNewUrlParser: true, useUnifiedTopology: true });
client.connect(err => {
  const collection = client.db("ProjectDB").collection("user");
  console.log(collection)
  
  // perform actions on the collection object
  client.close();
});
MongoClient.connect(uri, function(err, db) {
    if (err) throw err;
    var dbo = db.db("ProjectDB");
    dbo.collection("user").toArray(function(err, output) {
      if (err) throw err;
      console.log(output);
      db.close();
    });
  });

router.get('/', (req,res,next) => {

    res.status(200).json({
        message: 'Handling GET requests to /login',
    
    });
});
router.post('/', (req,res,next) => {
    res.status(201).json({
        message: 'Handling POST requests to /login',
      
    });
});
module.exports = router;