const fs = require("fs");

fs.readFile("input.txt", "utf-8", (err, data) => {
  if (err) return;
  let dupPriorities = 0;
  let badgePriorities = 0;
  const letter_values = ' abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ';
  let group_sacks = [];

  const lines = data.split("\n")
  for (let i = 0; i < lines.length; i++) {
    let line = lines[i]
    let div = parseInt(line.length/2)
    let left = line.slice(0, div);
    let right = line.slice(div);
    let set1 = Set(left)
  }
});
