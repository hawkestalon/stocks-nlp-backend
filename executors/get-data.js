'use strict';

const { spawnSync } = require('child_process');
const fs = require('fs/promises');
const path = require('path');


async function getData(body) {
  // const stockString = body.stocks;
  // const stocks = stockString.split(',');
  const stocks = body.stocks;
  console.log("Stocks --> ", stocks)
  const data = await runSentimentAnalysis(stocks);
  console.log('look at this cool data ', data);
  return {
    stocks: data
  }
}

async function runSentimentAnalysis(stocks) {
  const cwd = spawnSync('pwd', {encoding: 'utf-8'}).stdout.slice(0, -1);
  const python = spawnSync('python3', ['sentiment/main.py', stocks], {encoding: 'utf-8', cwd});
  console.log(python)
  return readDataFromJson(cwd, stocks);
}

async function readDataFromJson(dir, stockString) {
  const data = [];
  const stocks = stockString.split(',');
  console.log(stocks)
  for(let index in stocks) {
    const result = await fs.readFile(`${dir}/sentiment/data/${stocks[index]}.json`, {encoding: 'utf-8'})
    data.push(result);
  }
  return data;
}

module.exports = {
  getData
};
