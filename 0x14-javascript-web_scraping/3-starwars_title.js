#!/usr/bin/node

const args = process.argv;
let reqURL = 'http://swapi.co/api/films/' + args[2] + '/';
let request = require('request');
request(reqURL, function (error, response, body) {
  if (error) {
    console.log('error:', error); // Print the error if one occurred
  } else {
    let jso = JSON.parse(body);
    console.log(jso['title']);
  }
});
