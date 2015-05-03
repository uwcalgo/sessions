package com.github.pvanheus;

import java.util.List;
import java.util.Map;

public class Main {

    public static void main(String[] args) throws java.io.IOException {
        if (args.length == 1) {
            String filename = args[0];
            GreedyGiftGivers givers = new GreedyGiftGivers(filename);
            while (givers.hasNext()) {
                List<Map.Entry<String, String>> results = givers.next();
                for (Map.Entry<String, String> result : results)
                    System.out.println(result.getKey() + " " + result.getValue());
                System.out.println();
            }
        }
    }
}
