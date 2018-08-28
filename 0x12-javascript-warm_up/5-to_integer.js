#!/usr/bin/node
const args = process.argv;
let result;
result = parseInt(args[2]);
if (isNaN(result)) {
  result = 'Not a number';
}
console.log('My number: ' + result);
