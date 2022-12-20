#!/usr/bin/node
/* Executes x times a function */
exports.callMeMoby = function (x, theFunction) {
  let a;
  for (a = 0; a < x; a++) {
    theFunction();
  }
};
