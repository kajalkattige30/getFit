const express = require('express');
const router = express.Router();
const MongoClient = require('mongodb').MongoClient;
router.get('/', (req,res,next) => {
    res.status(200).json({
        message: 'Handling GET requests to /appetizer'
    });
});
router.post('/', (req,res,next) => {
    MongoClient.connect(uri, function(err, db) {
        if (err) throw err;
        var dbo = db.db("ProjectDB");
        dbo.collection("Appetizers").find({category:"Veg"}).toArray(function(err, result) {
          if (err) throw err;
          console.log("THis is the result :")
          var food = result[0].recipes[0]
          console.log(result[0].recipes[0]);
          db.close();
        });
      });
    res.status(201).json({
        message: 'Handling POST requests to /appetizer',
        createdAppetizer: appetizer
    });
});
module.exports = router;