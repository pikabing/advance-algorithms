import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Random;

class Sorting {

    public static boolean increasing(List<Integer> arr) {
        for(int i = 0; i<arr.size() - 2; i++) {
            if(arr.get(i+1) < arr.get(i)) return false;
        }
        return true;
    }

    public static void nonDeterministicSorting(List<Integer> arr) {
        long time = System.currentTimeMillis();
        Random r = new Random();
        List<Integer> sorted = new ArrayList<>();
        Map<Integer, Integer> visited = new HashMap<>();
        int count = 0;
        while(count < 20) {
            for(int i = 0; i < arr.size(); i++) {
                int index = r.nextInt(arr.size() - 1);
                if(!visited.containsKey(index)) {
                    visited.put(index, 1);
                    sorted.add(arr.get(index));
                }
            }
            if(increasing(arr)) break;
            count++;
        }
        time = System.currentTimeMillis() - time;
        // System.out.println(sorted);
        System.out.println("Non Deterministic time takes " + time + "ms");
    }

    public static void deterministicSorting(List<Integer> arr) {
        long time = System.currentTimeMillis();
        Collections.sort(arr);
        time = System.currentTimeMillis() - time;
        // System.out.println(arr);
        System.out.println("Deterministic time takes " + time + "ms");
    }

    public static void main(String[] args) {
        List<Integer> l = new ArrayList<>();
        List<Integer> l1 = new ArrayList<>();
        Random r = new Random();
        for(int i = 0; i< 100; i++) {
            l.add(r.nextInt(100));
            l1.add(r.nextInt(100));
        }
        deterministicSorting(l);
        nonDeterministicSorting(l1);
    }
}