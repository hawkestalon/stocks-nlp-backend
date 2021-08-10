# Stocks NLP Backend

This is the backend for the Stocks Natural Language Final Project, USU - CS5890
Front end is [here](https://github.com/austinGENEreeve/stock-front-end)

## Running the project

1. npm install
2. npm start
3. Use a tool like postman to make requests

## Routes

There are currently two routes

1. GET /ping
   * Returns pong (basic functionality test)
2. POST /get-data
   * Takes a comma separated list of stocks ie ({ "stocks": "AMZN, GME"})
   * Returns sentiment analysis for each stock (I think)

there will be more to come... :D
