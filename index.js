'use strict'

const express = require('express')
const { app, port } = require('./server')

function main() {
  app.listen(port, () => {console.log(`Listening on port ${port}`)});
}

main();