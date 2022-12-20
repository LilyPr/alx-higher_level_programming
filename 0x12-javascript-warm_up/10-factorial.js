#!/usr/bin/node
/* Computes and prints a factorial */
function factorial (a) {
  const number = parseInt(a);
  if (isNaN(number)) {
    return 1;
  }
  if (a === 0) {
    return 1;
  }
  return a * factorial(number - 1);
}
console.log(factorial(process.argv[2]));
