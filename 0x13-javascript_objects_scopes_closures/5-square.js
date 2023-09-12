#!/usr/bin/node
/* eslint-disable no-unused-vars */
const Rectangle = require('./4-rectangle');
class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
}
module.exports = Square;
