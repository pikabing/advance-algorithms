import java.util.*;
import java.io.*;

class Point {
    int x, y;
    Point(int x, int y) {
        this.x = x;
        this.y = y;
    }
}

class Hull {

    public static int orientation(Point p, Point q, Point r) {

        // to calculate orientation we calculate slope
        // also, if three points are collinear, area of triangle formed is 0, by matrix formula, value of orientation will be ero
        // to check if trio is clockwise or a right turn, we use slope. check the following link:
        // https://www.geeksforgeeks.org/orientation-3-ordered-points/
        // clockwise -> positive result of difference between slopes
        // counter-clockwise -> negative result of difference between slopes

        int orient = ((q.y-p.y) * (r.x-q.x)) - ((r.y-q.y) * (q.x-p.x));
        if (orient == 0) {
            return 0;
        }

        return (orient > 0) ? 1 : 2;
    }

    // set of n points
    public static ArrayList<Point> computeHull(Point points[], int n) {

        ArrayList<Point> hull = new ArrayList<Point>();

        if (n < 3) return hull;

        int l=0;
        // starting from 1, coz k's initial value is already 0
        // rightmost point
        for(int i=1; i< n; i++) {
            if(points[i].x > points[l].x)
                l = i;
        }

        int p=l, q;
        do {

            hull.add(points[p]);
            q = (p + 1) % n;
            for (int i =0; i<n; i++) {
                if (orientation(points[p],points[i], points[q])==1) {
                    q = i;
                }
            }

            p = q;

        } while(p != l);

        printHull(hull);
        String fileName = "output.txt";
        try {

            BufferedWriter writer = new BufferedWriter(new FileWriter(fileName));
            writer.write("The points in the Convex Hull are as follows:" + System.lineSeparator());
            for(Point str: hull) {
                writer.write("(" + str.x + ", " + str.y + ")" + System.lineSeparator());
            } 
            writer.close();

        } catch(Exception e) {

            e.printStackTrace();

        }

        findPockets(hull, points);
        return hull;
    }

    public static int findIndex(Point arr[], Point t) 
        { 
    
            // if array is Null 
            if (arr == null) { 
                return -1; 
            } 
    
            // find length of array 
            int len = arr.length; 
            int i = 0; 
    
            // traverse in the array 
            while (i < len) { 
    
                // if the i-th element is t 
                // then return the index 
                if (arr[i] == t) { 
                    return i; 
                } 
                else { 
                    i = i + 1; 
                } 
            } 
            return -1; 
        } 

    public static void findPockets(ArrayList<Point> hull, Point points[]) {

        ArrayList<Point> result = new ArrayList<Point>(Arrays.asList(points));
        for (Point i : points) {
            for (Point j : hull) {
                if((i.x == j.x) && (i.y==j.y))                     
                    result.remove(i);
            }
        }

        for (Point i : points) {
         if (result.contains(i)) {
                int idx1 = findIndex(points, i) - 1;
                if(hull.contains(points[idx1])) {
                    int idx2 = hull.indexOf(points[idx1]) + 1;
                    idx2 = idx2 % hull.size();
                    System.out.println("There is pocket between points " + points[idx1].x + ", " 
                    + points[idx1].y +" and " + hull.get(idx2).x + ", " + hull.get(idx2).y);
                    String fileName = "pockets.txt";
                    try {
                        BufferedWriter writer = new BufferedWriter(new FileWriter(fileName));
                        for(Point str: hull) {
                            writer.write("There is pocket between points " + points[idx1].x + ", " 
                            + points[idx1].y +" and " + hull.get(idx2).x + ", " + hull.get(idx2).y
                            + System.lineSeparator());
                        } 
                        writer.close();

                    } catch(Exception e) {

                        e.printStackTrace();

                    }
                }
            }   
        }

    }

    public static void printHull(ArrayList<Point> hull) {

        System.out.println("The points in the Convex Hull are as follows:");
        for (Point point : hull) {
            System.out.println("(" + point.x + ", " + 
                                point.y + ")");
            }

    }

    public static void readFile() {
        File file = new File("input.txt"); 
        int n = 0;
        try {
            BufferedReader br = new BufferedReader(new FileReader(file)); 
            n = Integer.parseInt(br.readLine());
            Point points[] = new Point[n];
            for (int i = 0; i < n; i++) 
            {
                String line = br.readLine();
                StringTokenizer t = new StringTokenizer(line, " ");

                int x = Integer.parseInt(t.nextToken());
                int y = Integer.parseInt(t.nextToken());
                points[i] = new Point(x, y);
            }
            computeHull(points, n);  
        } catch(Exception e) {
                e.printStackTrace();
        }  
    }

    public static void main(String[] args) {
        readFile();
    } 
}