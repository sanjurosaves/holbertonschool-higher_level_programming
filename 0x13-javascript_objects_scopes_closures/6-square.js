#!/usr/bin/node
const Square = require('./5-square');

Square.prototype.charPrint = function (c) {
  if (c === undefined) {
    c = 'X';
  }

  let i;
  for (i = 0; i < this.height; i++) {
    console.log(c.repeat(this.width));
  }
};

module.exports = Square;
