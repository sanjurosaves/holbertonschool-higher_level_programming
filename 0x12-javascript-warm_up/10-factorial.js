#!/usr/bin/node
const args = process.argv;
let a = parseInt(args[2]);
if (isNaN(a)) {
  console.log('1');
} else {
  console.log(factorial(a));
}

function factorial (n) {
  if (n === 0) {
    return (1);
  } else if (n < 0) {
    return (-1);
  }

  return (n * factorial(n - 1));
}
