#!/usr/bin/node

const args = process.argv;
let reqURL = 'http://swapi.co/api/films/' + args[2] + '/';
let request = require('request');
request(reqURL, function (error, response, body) {
  if (error) {
    console.log('error:', error);
  } else {
    let jso = JSON.parse(body);
    for (let i = 0; i < jso['characters'].length; i++) {
      request(jso['characters'][i], function (error, response, body) {
        if (error) {
          console.log('error:', error);
        } else {
          let cjso = JSON.parse(body);
          console.log(cjso['name']);
        }
      });
    }
  }
});
