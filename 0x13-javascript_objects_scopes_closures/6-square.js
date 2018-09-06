#!/usr/bin/node
const OrigSquare = require('./5-square');

class Square extends OrigSquare {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }

    let i;
    for (i = 0; i < this.height; i++) {
      console.log(c.repeat(this.width));
    }
  }
}

module.exports = Square;
