import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;
import java.util.Set;
import java.util.HashSet;

class Solution {
    public static void main(String[] args) {
        try {
            File input = new File("input.txt");
            Scanner reader = new Scanner(input);
            int score1 = 0;
            int score2 = 0;
            String line;
            Set<String> win1 = new HashSet<String>();
            win1.add("A Y");
            win1.add("B Z");
            win1.add("C X");
            Set<String> draw1 = new HashSet<String>();
            draw1.add("A X");
            draw1.add("B Y");
            draw1.add("C Z");

            while (reader.hasNextLine()) {
                line = reader.nextLine();

                // rule 1
                if (win1.contains(line)) {
                    score1 += 6;
                } else if (draw1.contains(line)) {
                    score1 += 3;
                }
                ;

                if (line.contains("X")) {
                    score1 += 1;
                } else if (line.contains("Y")) {
                    score1 += 2;
                } else if (line.contains("Z")) {
                    score1 += 3;
                }

                // rule 2
                switch (line.charAt(0)) {
                    case 'A':
                        if (line.contains("X")) {
                            score2 += 3;
                        } else if (line.contains("Y")) {
                            score2 += 4;
                        } else if (line.contains("Z")) {
                            score2 += 8;
                        }
                        break;
                    case 'B':
                        if (line.contains("X")) {
                            score2 += 1;
                        } else if (line.contains("Y")) {
                            score2 += 5;
                        } else if (line.contains("Z")) {
                            score2 += 9;
                        }
                        break;
                    case 'C':
                        if (line.contains("X")) {
                            score2 += 2;
                        } else if (line.contains("Y")) {
                            score2 += 6;
                        } else if (line.contains("Z")) {
                            score2 += 7;
                        }
                        break;
                }
            }
            reader.close();
            System.out.println(score1); // answer: 10941
            System.out.println(score2); // answer: 13071

        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }
    }
}