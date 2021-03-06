#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let i, j, string;
    for (i = 0; i < this.height; i++) {
      string = '';
      for (j = 0; j < this.width; j++) {
        string += 'X';
      }
      console.log(string);
    }
  }

  rotate () {
    let temp;
    temp = this.height;
    this.height = this.width;
    this.width = temp;
  }

  double () {
    this.height = 2 * this.height;
    this.width = 2 * this.width;
  }
}

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
}

module.exports = Square;
