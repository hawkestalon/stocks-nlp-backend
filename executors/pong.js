'use strict';

/** 
 * This is where the logic of an endpoint will be executed
 * There will be a separate "controller" function that will get
 * the payload and pass it to the logic here.
 */

function pong() {
  return 'pong';
}

/**
 * Even though we only need to export a single function
 * exporting it inside an object can help with testing
 * if we decide to add tests
 */
module.exports = {
  pong
};
