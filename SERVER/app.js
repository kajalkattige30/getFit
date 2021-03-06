const express = require('express');
const app = express();
const request = require('request-promise');

const morgan = require('morgan');
const bodyParser = require('body-parser');
const methodOverride = require('method-override');
const productRoutes = require('./api/routes/appetizer');
const userSignupRoutes = require('./api/routes/signup');
const userLoginRoutes = require('./api/routes/login');
const userProfileRoutes = require('./api/routes/profile');
const userDetailRoutes = require('./api/routes/questionnaire');
const homeFragmentRoutes = require('./api/routes/getInfo');
const searchRoutes = require('./api/routes/search');
const addMealRoutes = require('./api/routes/addMeal');
const getMealRoutes = require('./api/routes/getMeal');
const nodeFlaskRoutes = require('./api/routes/nodeFlask');
const planRoutes = require('./api/routes/plan')

app.use(express.json())

app.use(morgan('dev'));
app.use(bodyParser.urlencoded({extended: false}));
app.use(bodyParser.json());
app.use(methodOverride('_method'));
app.use('/appetizer',productRoutes);
app.use('/signup',userSignupRoutes);
app.use('/login',userLoginRoutes);
app.use('/profile',userProfileRoutes);
app.use('/questionnaire',userDetailRoutes);
app.use('/getInfo',homeFragmentRoutes);
app.use('/search',searchRoutes);
app.use('/addMeal',addMealRoutes);
app.use('/getMeal',getMealRoutes);
app.use('/nodeFlask',nodeFlaskRoutes);
app.use('/plan',planRoutes);

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


module.exports = app;