'use strict';


function getData(body) {
  const stockString = body.stocks;
  const stocks = stockString.split(',');
  const sentimentStocks = stocks.map(stock => {
    return sentimentAnalysis(stock);
  }); 
  return {
    stocks: sentimentStocks
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

module.exports = {
  getData
};
