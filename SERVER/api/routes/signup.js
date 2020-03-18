const express = require('express');
const router = express.Router();
const MongoClient = require('mongodb').MongoClient;


const uri = "mongodb+srv://Janhavi:mongodb@projectcluster-azpnv.mongodb.net/test?retryWrites=true&w=majority";
const client = new MongoClient(uri, { useNewUrlParser: true, useUnifiedTopology: true });
client.connect(err => {
  const col = client.db("ProjectDB").collection("user");
  console.log(col)
  
  // perform actions on the collection object
  client.close();
});
MongoClient.connect(uri, function(err, db) {
    if (err) throw err;
    var dbo = db.db("ProjectDB");
    dbo.collection("user").toArray(function(err, result) {
      if (err) throw err;
      newUsers = result
      console.log(result[0]);
      db.close();
    });
  });

router.get('/', (req,res,next) => {

    res.status(200).json({
        message: 'Handling GET requests to /signup',
        
    });
});
var newUsers = ""
router.post('/', (req,res,next) => {
    res.status(201).json({
        message: 'Handling POST requests to /signup',
        
    });
});
module.exports = router;