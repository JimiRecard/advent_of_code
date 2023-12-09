const fs = require("fs");

fs.readFile("input.txt", "utf-8", (err, data) => {
  if (err) return;
  elf_list = [];
  elf_calories = 0;
  for (line of data.split("\n")) {
    if (line.match(/\d+/)) {
      elf_calories += parseInt(line);
    } else {
      elf_list.push(elf_calories);
      elf_calories = 0;
    }
  }
  console.log(Math.max(...elf_list)); // Answer: 69289
  elf_list.sort((a,b) => {return a-b});
  console.log(elf_list.at(-1) + elf_list.at(-2) + elf_list.at(-3)); // Answer: 205615
});
