#!/usr/bin/node
const args = process.argv;
let result;
if (typeof args[2] === 'undefined') {
  result = 'No argument';
} else {
  result = args[2];
}
console.log(result);
