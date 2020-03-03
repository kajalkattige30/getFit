const express = require('express');
const router = express.Router();
const MongoClient = require('mongodb').MongoClient;

var food = ""
const uri = "mongodb+srv://Janhavi:mongodb@projectcluster-azpnv.mongodb.net/test?retryWrites=true&w=majority";
const client = new MongoClient(uri, { useNewUrlParser: true, useUnifiedTopology: true });
client.connect(err => {
  const collection = client.db("ProjectDB").collection("Appetizers");
  console.log(collection)
  
  // perform actions on the collection object
  client.close();
});
MongoClient.connect(uri, function(err, db) {
    if (err) throw err;
    var dbo = db.db("ProjectDB");
    dbo.collection("Appetizers").find({category:"Veg"}).toArray(function(err, result) {
      if (err) throw err;
      console.log("THis is the food inside get result :")
      food = result[0]
      console.log(result[0]);
      db.close();
    });
  });

router.get('/', (req,res,next) => {

    res.status(200).json({
        message: 'Handling GET requests to /appetizer',
        recipes : food
    });
});
var food = ""
router.post('/', (req,res,next) => {
    // MongoClient.connect(uri, function(err, db) {
    //     if (err) throw err;
    //     var dbo = db.db("ProjectDB");
    //     dbo.collection("Appetizers").find({category:"Veg"}).toArray(function(err, result) {
    //       if (err) throw err;
    //       console.log("THis is the food :")
    //       food = result[0].recipes[0]
    //       console.log(food);
    //       db.close();
    //     });
    //   });
    res.status(201).json({
        message: 'Handling POST requests to /appetizer',
        createdAppetizer: food
    });
});
module.exports = router;