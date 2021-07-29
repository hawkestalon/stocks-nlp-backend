'use strict';

const bodyParser = require('body-parser');
const express = require('express');
const { getData } = require('./executors/get-data');
const { pong } = require('./executors/pong');

const app = express();
const port = 3001;

// middleware goes here
app.use(express.urlencoded({ extended: false}));
app.use(express.json());

// routes go here
app.get('/ping', pingController);
app.post('/get-data', getDataController);


// "controller" functions go here
function pingController(req, res) {
  const response = pong();
  res.send(response);
}

async function getDataController(req, res) {
  const response = await getData(req.body);
  res.send(response);
}

module.exports = {
  app,
  port
};