const express = require('express');
const router = express.Router();
const mongoClient = require('mongodb').MongoClient;
const request = require('request-promise');
const axios = require('axios')
const request2 = require('request')
const fs = require('fs')

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
                var data = JSON.stringify(nodeToFlask)
                fs.writeFileSync('dataToMl.json',data)

                axios
                .post('http://127.0.0.1:5000/nodeFlask'), nodeToFlask)
                .then(res => {
                    console.log(`statusCode: ${res.statusCode}`)
                    console.log(res)
                })
                .catch(err => {
                    console.log(err)
                })
                var returndata = fs.readFileSync("C:/Users/kkatt/Documents/BE_Project/getFit/SERVER/api/recommendation.json");
                var recommended_meals = JSON.parse(returndata);
                //C:/Users/kkatt/Documents/BE_Project/getFit/SERVER/api/recommendation.json
                console.log(recommended_meals)
                res.status(200).send(JSON.stringify(recommended_meals))
            })
        }
    }
})


                // request2.post(
                //     'http://127.0.0.1:5000/nodeFlask',
                //     {
                //         json : {
                //             calorieCount : result[0].calorieCount
                //         }
                        
                //     },
                // (err, res, parsedBody) => {
                //     if(err) {
                //         console.error(err)
                //         return 
                //     }
                //     console.log(parsedBody)
                //     console.log("Printing parsedBody")
                // })
                
                
            

   
        
                

                

                // var options = {
                //     method: 'POST',
                //     uri: 'http://127.0.0.1:5000/nodeFlask',
                //     body: nodeToFlask,
                //     json: true // Automatically stringifies the body to JSON
                // };

                // var returndata;
                // var recommended_meals;
                // var sendrequest = request(options,  function (error, response, parsedBody) {
                //     if(error) throw error
                //     // console.log(parsedBody); // parsedBody contains the data sent back from the Flask server
                //     returndata = parsedBody;
                //     console.log("This is Parsed Body")
                //     console.log(returndata)
                //     returndata = fs.readFileSync("C:/Users/kkatt/Documents/BE_Project/getFit/SERVER/api/recommendation.json");
                //     recommended_meals = JSON.parse(returndata);
                //     //C:/Users/kkatt/Documents/BE_Project/getFit/SERVER/api/recommendation.json
                //     console.log(recommended_meals)
                //     res.status(200).send(JSON.stringify(recommended_meals))
                //     // do something with this data, here I'm assigning it to a variable.
                
                   
                // })
                // .catch(function (err) {
                //     console.log(err);
                // });
                

            // })
          
        // })

//     }
// })
module.exports = router;
