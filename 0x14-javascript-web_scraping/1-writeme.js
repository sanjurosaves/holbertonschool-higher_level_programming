#!/usr/bin/node

const args = process.argv;

let fs = require('fs');
fs.writeFile(args[2], args[3], (err) => {
  if (err) {
    console.log(err);
  }
});
