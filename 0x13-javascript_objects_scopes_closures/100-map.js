#!/usr/bin/node
// Imports an array and computes a new array
const list = require('./100-data').list;
console.log(list);
const newlist = list.map(function (num, index) {
  return num * index;
});
console.log(newlist);
