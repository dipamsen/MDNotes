#!/usr/bin/env node

// Pandoc filter to convert all text to uppercase

const pandoc = require("pandoc-filter");
const mhchem = require("mhchemparser");

function action(elem, format, meta) {
  console.log(elem);
  return elem;
  // if (type === "Str") return Str(value.toUpperCase());
}

pandoc.stdio(action);
