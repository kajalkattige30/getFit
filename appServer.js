const http = require('http');
const app = require('./app');
const port = process.env.PORT || 3000;
const server = http.createServer(app);
server.listen(port);


/*const mongoose = require("mongoose")

const MongoClient = require('mongodb').MongoClient;
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
      console.log("THis is the result :")
      var food = result[0].recipes[0]
      console.log(result[0].recipes[0]);
      db.close();
    });
  });
*/