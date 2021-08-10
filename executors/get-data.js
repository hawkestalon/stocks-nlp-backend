'use strict';

const { spawnSync } = require('child_process');
const fs = require('fs/promises');
const path = require('path');


async function getData(body) {
  const stockString = body.stocks;
  const stocks = stockString.split(',');
  console.log("Stocks --> ", stocks)
  const data = await runSentimentAnalysis(stocks);
  console.log('look at this cool data ', data);
  return {
    stocks: JSON.parse(data)
  }
}

async function runSentimentAnalysis(stocks) {
  const cwd = spawnSync('pwd', {encoding: 'utf-8'}).stdout.slice(0, -1);
  const python = spawnSync('python', ['sentiment/main.py', cwd, ...stocks], {encoding: 'utf-8', cwd});
  console.log(python)
  console.log(python.stdin);
  return readDataFromJson(cwd, stocks);
}

async function readDataFromJson(dir, stocks) {
  const data = [];
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
