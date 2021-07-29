'use strict';

const { spawnSync } = require('child_process');
const fs = require('fs/promises');


async function getData(body) {
  const stockString = body.stocks;
  const stocks = stockString.split(',');
  const data = await runSentimentAnalysis(stocks);
  console.log('look at this cool data ', data);
  return {
    stocks: JSON.parse(data)
  }
}

function sentimentAnalysis(stock) {
  if(Math.random() * 100 < 50) {
    return {
      stock,
      sentiment: 'positive',
      numberOfPositiveTweets: Math.round(Math.random() * 100),
      numberOfNegativeTweets: Math.round(Math.random() * 100), 
    }
  } else {
    return {
      stock,
      sentiment: 'negative',
      numberOfPositiveTweets: Math.round(Math.random() * 100),
      numberOfNegativeTweets: Math.round(Math.random() * 100),
    }
  }
}

async function runSentimentAnalysis(stocks) {
  const cwd = spawnSync('pwd', {encoding: 'utf-8'}).stdout.slice(0, -1);
  const python = spawnSync('python', ['executors/sentiment.py', cwd, ...stocks], {encoding: 'utf-8', cwd});
  return readDataFromJson(cwd);
}

async function readDataFromJson(dir) {
  const data = await fs.readFile(dir + '/executors/data.json', {encoding: 'utf-8'})
  return data;
}

module.exports = {
  getData
};
