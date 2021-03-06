'use strict';

const bodyParser = require('body-parser');
const express = require('express');
const { getData } = require('./executors/get-data');
const { pong } = require('./executors/pong');
const cors = require('cors');

const app = express();
const port = process.env.PORT || 8080;

// middleware goes here
app.use(express.urlencoded({ extended: false}));
app.use(express.json());
app.use(cors());

// routes go here
app.get('/ping', pingController);
app.post('/get-data', getDataController);


// "controller" functions go here
function pingController(req, res) {
  const response = pong();
  res.send(response);
}

async function getDataController(req, res) {
  try {
    const response = await getData(req.body);
    res.send(response);
  } catch (err) {
    console.error(err);
    res.statusCode = 500;
    res.send("Internal Error")
  }
}

module.exports = {
  app,
  port
};
