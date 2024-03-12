#!/usr/bin/node

const dict = require('./101-data').dict;

const sortedDict = {};

for (const key in dict) {
  if (dict.hasOwnProperty(key)) {
    const value = dict[key];
    if (!sortedDict[value]) {
      sortedDict[value] = [];
    }
    sortedDict[value].push(key);
  }
}

console.log(sortedDict);

