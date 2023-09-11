#!/usr/bin/node
const numOccurrences = parseInt(process.argv[2]);
if (isNaN(numOccurrences)) {
  console.log('Missing number of occurences');
} else {
  for (let i = 0; i < numOccurrences; i++) {
    console.log('C is fun');
  }
}
