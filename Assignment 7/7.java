import java.util.*;
import java.util.concurrent.atomic.AtomicInteger;
import java.util.stream.Collectors;

class MedianOfMedians {

    public static int deterministic_median_of_medians(List<Integer> arr, int i) {
        System.out.println(arr.toString());
        AtomicInteger a = new AtomicInteger();
        List<List<Integer>> subArr = new ArrayList<List<Integer>>(arr.stream()
                                    .collect(Collectors.groupingBy(it -> a.getAndIncrement() / 5))
                                    .values());
        List<Integer> medians = new ArrayList<>();
        subArr.forEach(e ->{
            Collections.sort(e);
            medians.add(e.get(e.size() / 2));
        });
        Collections.sort(medians);
        int pivot;
        if(medians.size() <= 5)
            pivot = medians.get(medians.size() / 2);
        else 
            pivot = deterministic_median_of_medians(medians, medians.size()/2);

        List<Integer> low = new ArrayList<>();
        List<Integer> high = new ArrayList<>();

        arr.forEach(e -> {
            if(e < pivot) low.add(e);
            if(e >= pivot) high.add(e);
        });

        int k = low.size();

        if(i < k)
            return deterministic_median_of_medians(low, i);
        else if(i > k)
            return deterministic_median_of_medians(high, i - k);
        else 
            return pivot;

    }

    public static int monte_carlo_median(List<Integer> arr, Double delta) {
        Random random = new Random();
        int index = random.nextInt(arr.size() - 1);
        int predicted = arr.get(index);
        Collections.sort(arr);
        int i = arr.indexOf(predicted) + 1;
        int leftLimit = (int) Math.floor((0.5 - delta) * (arr.size() + 1));
        int rightLimit = (int) Math.ceil((0.5 + delta) * (arr.size() + 1));
        if(i >= leftLimit && i <= rightLimit) return predicted;
        else return -1;
    }

    public static int las_vegas_median_of_medians(List<Integer> arr) {
        while(true) {
            int res = monte_carlo_median(arr, 0.1);
            if(res != -1) return res;
        }
    }

    public static void main(String[] args) {
        Set<Integer> set = new HashSet<>();
        Random r = new Random();
        for(int i = 0; i< 10000; i++) {
            int mem = r.nextInt(10000);
            set.add(mem);
        }
        List<Integer> arr = new ArrayList<>(set);
        long time = System.currentTimeMillis();
        System.out.println("[RESULT]: " + deterministic_median_of_medians(arr, arr.size()/2));
        time = System.currentTimeMillis() - time;
        System.out.println("[TIME] Deterministic Algo: " + time + "ms");
        time = System.currentTimeMillis();
        System.out.println("[RESULT]: " + las_vegas_median_of_medians(arr));
        time = System.currentTimeMillis() - time;
        System.out.println("[TIME] Randomized Algorithm: " + time + "ms");
    }
}