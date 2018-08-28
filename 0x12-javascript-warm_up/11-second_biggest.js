#!/usr/bin/node
const args = process.argv;
if (args.length < 4) {
  console.log('0');
} else {
  const l = args.length;
  let arr = [];
  for (let i = 3; i <= l; i++) {
    arr.push(parseInt(args[i - 1]));
  }
  arr.sort();
  while (arr[arr.length - 1] === arr[arr.length - 2]) {
    arr.pop();
  }
  console.log(arr[arr.length - 2]);
}
