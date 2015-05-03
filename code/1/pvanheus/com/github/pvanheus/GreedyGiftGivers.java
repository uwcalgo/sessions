package com.github.pvanheus;

import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.nio.charset.StandardCharsets;
import java.util.*;

/**
 * A solution for the Greedy Gift Givers problem
 * (http://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=55)
 */

public class GreedyGiftGivers implements Iterator<List<Map.Entry<String, String>>> {
    private Integer starting_line = 0;
    List<String> lines;

    public GreedyGiftGivers(String filename) throws java.io.IOException {
        Path input_path = Paths.get(filename);
        this.lines = Files.readAllLines(input_path, StandardCharsets.UTF_8);
        this.starting_line = 0;
    }

    public boolean hasNext() {
        return this.starting_line >= this.lines.size() ? false : true;
    }

    public List<Map.Entry<String, String>> next() {
        List<Map.Entry<String, String>> results = new ArrayList();
        Integer num_people = Integer.parseInt(lines.get(this.starting_line));
        List<String> people = Arrays.asList(lines.get(this.starting_line + 1).split("\\s"));
        Map<String, Integer> amounts = new HashMap<String, Integer>();
        Integer count = 0;
        while (count < num_people) {
            List<String> fields = Arrays.asList(lines.get(this.starting_line + 2 + count).split("\\s"));
            String name = fields.get(0);
            Integer amount_given = Integer.parseInt(fields.get(1));
            //System.out.println("name: " + name + " " + amount_given.toString());
            if (amount_given > 0) {
                Integer current_amount = amounts.containsKey(name) ? amounts.get(name) : 0;
                amounts.put(name, current_amount - amount_given);
                Integer num_receivers = Integer.parseInt(fields.get(2));
                Integer amount_per_receiver = amount_given / num_receivers;
                if (fields.size() > 2)
                    for (String receiver : fields.subList(3, fields.size())) {
                        //System.out.println("receiver: " + receiver + " " + amount_per_receiver.toString());
                        current_amount = amounts.containsKey(receiver) ? amounts.get(receiver) : 0;
                        amounts.put(receiver, current_amount + amount_per_receiver);
                    }
            }
            ++count;
        }
        // update starting point: one past the last line we processed
        this.starting_line = this.starting_line + 2 + count;
        for (String name : people) {
            results.add(new AbstractMap.SimpleEntry<String, String>(name, amounts.get(name).toString()));
        }
        return results;
    }

    public void remove() {
        throw new UnsupportedOperationException();
    }
}
