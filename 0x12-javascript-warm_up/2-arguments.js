#!/usr/bin/node
const args = process.argv;
let result;
if (args.length === 2) {
  result = 'No argument';
} else if (args.length === 3) {
  result = 'Argument found';
} else {
  result = 'Arguments found';
}
console.log(result);
