import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;
import java.util.ArrayList;
import java.util.Collections;

class Solution {
    public static void main(String[] args) {
        try {
            File input = new File("input.txt");
            Scanner reader = new Scanner(input);
            ArrayList<Integer> elf_list = new ArrayList<Integer>();
            int partSum = 0;
            String line;
            while (reader.hasNextLine()) {
                line = reader.nextLine();
                if (line != "") {
                    partSum += Integer.parseInt(line);
                } else {
                    elf_list.add(partSum);
                    partSum = 0;
                }
            }
            reader.close();
            System.out.println(Collections.max(elf_list)); // Answer: 69289
            elf_list.sort(null);
            int len = elf_list.size();
            System.out.println(elf_list.get(len - 1) + elf_list.get(len - 2) + elf_list.get(len - 2)); // Answer: 205931

        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }
    }
}