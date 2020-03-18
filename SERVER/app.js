const express = require('express');
const app = express();
const morgan = require('morgan');
const bodyParser = require('body-parser');
// const mongoose = require("mongoose")

const MongoClient = require('mongodb').MongoClient;
const uri = "mongodb+srv://Janhavi:mongodb@projectcluster-azpnv.mongodb.net/test?retryWrites=true&w=majority";

app.use(express.json())

const client = new MongoClient(uri, { useNewUrlParser: true, useUnifiedTopology: true });
client.connect(err => {
  const collection = client.db("ProjectDB").collection("Appetizers");
  const col = client.db("ProjectDB").collection("user")
  console.log(collection)
  console.log(col)
  // perform actions on the collection object
  client.close();
});

const productRoutes = require('./api/routes/appetizer');
const userSignupRoutes = require('./api/routes/signup');
const userLoginRoutes = require('./api/routes/login');


app.use(morgan('dev'));
app.use(bodyParser.urlencoded({extended: false}));
app.use(bodyParser.json());
app.use('/appetizer',productRoutes);
app.use((req, res, next) => {
    const error = new Error('Not Found');
    error.status = 404;
    next(error);
});
app.use((error, req, res, next) => {
    res.status(error.status || 500);
    res.json({
        error: {
            message: error.message
        }
    });
});

app.use('/signup',(req,res) => {
    const newUser = {
        name: req.body.name,
        email: req.body.email,
        password: req.body.password
    }

    const query = {email: newUser.email }
    col.findOne(query, (err,result) => {
        if(result == null){
            col.insertOne(newUser, (err, result) => {
                res.status(200).send()
            })
        } else {
            res.status(400).send()
        }
    })
})

app.use('/login', (req,res) => {
    const query = {
        email: req.body.email,
        password: req.body.password
    }
    col.findOne(query, (err, result) => {
        if(result != null){
            const objToSend = {
                name: result.name,
                email: result.email
            }

            res.status(200).send(JSON.stringify(objToSend))
        } else{
            res.status(404).send()
        }

    })
})

module.exports = app;