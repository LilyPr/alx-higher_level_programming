#!/usr/bin/node
/* Prints the first arg if it can be converted */
const argv = parseInt(process.argv[2]);
if (Number.isNaN(argv)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + argv);
}
