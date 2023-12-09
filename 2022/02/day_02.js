const fs = require("fs");

fs.readFile("input.txt", "utf-8", (err, data) => {
  if (err) return;
  let score1 = 0;
  let score2 = 0;
  const win1 = ["A Y", "B Z", "C X"];
  const draw1 = ["A X", "B Y", "C Z"];
  for (const line of data.split("\n")) {
    const play = line[0] + line[1] + line[2];
    // rule 1
    if (win1.includes(play)) {
      score1 += 6;
    } else if (draw1.includes(play)) {
      score1 += 3;
    }

    if (play.includes("X")) {
      score1 += 1;
    } else if (play.includes("Y")) {
      score1 += 2;
    } else if (play.includes("Z")) {
      score1 += 3;
    }

    // rule 2
    switch (line[0]) {
      case "A":
        if (play.includes("X")) {
          score2 += 3;
        } else if (play.includes("Y")) {
          score2 += 4;
        } else if (play.includes("Z")) {
          score2 += 8;
        }
        break;
      case "B":
        if (play.includes("X")) {
          score2 += 1;
        } else if (play.includes("Y")) {
          score2 += 5;
        } else if (play.includes("Z")) {
          score2 += 9;
        }
        break;
      case "C":
        if (play.includes("X")) {
          score2 += 2;
        } else if (play.includes("Y")) {
          score2 += 6;
        } else if (play.includes("Z")) {
          score2 += 7;
        }
        break;
    }
  }

  console.log(score1); // Answer: 10941
  console.log(score2); // Answer: 13071
});
