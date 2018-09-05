#!/usr/bin/node

const args = process.argv;

let fs = require('fs');
let request = require('request');
let reqURL = args[2];
request(reqURL, function (error, response, body) {
  if (error) {
    console.log('error:', error);
  } else {
    fs.writeFile(args[3], body, 'utf8', (err) => {
      if (err) {
        console.log(err);
      }
    });
  }
});
