#!/usr/bin/node
const x = process.argv[2];

if (!parseInt(x)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < x; i++) {
    let j = 0;
    let mySymbol = '';

    while (j < x) {
      mySymbol = mySymbol + 'X';
      j++;
    }
    console.log(mySymbol);
  }
}
