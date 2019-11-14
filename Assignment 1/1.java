import java.util.ArrayList;
import java.util.List;

class ConvexHull {

    class Point {
        int x;
        int y;
        
        Point(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }

    public static int orientation(Point p, Point q, Point r) {

        int orient = ((q.y - p.y) * (r.x - q.x)) - ((r.y - q.y) * (q.x - p.x));

        if(orient == 0) return 0;

        return orient > 0 ? 1 : 2;
    }

    public static ArrayList<Point> computerHull(List<Point> points) {
        int n = points.size();
        ArrayList<Point> hull = new ArrayList<>();

        if(n < 3) return hull;

        int l = 0;
        for(int i = 1; i <n; i++) {
            if(points.get(i).x > points.get(l).x)
                l = i;
        }

        int p = 1, q;
        do {
            hull.add(points.get(p));
            q = (p + 1) % n;
            for(int i = 0; i< n; i++) {
                if(orientation(points.get(p), points.get(i), points.get(q)) == 1)
                    q = i;
            }
            p = q;
        } while(p != l);
        return hull;
    }

    public static void findPockets(List<Point> hull, List<Point> points) {

        List<Point> res = new List<>(points);
        for(Point p : points) {
            for(Point q : hull) {
                if(p.x == q.x && p.y == q.y) res.remove(p); 
            }
        }

        for(Point p : points) {

            if(res.contains(p)) {
                int i1 = points.indexOf(p) - 1;
                if(hull.contains(points.get(i1))) {
                    int i2 = hull.indexOf(i1) + 1;
                    i2 = i2 % hull.size();
                    System.out.println("There is pocket between points " + points.get(i1).x + ", " 
                    + points.get(i1).y +" and " + hull.get(i2).x + ", " + hull.get(i2).y);
                }
            }
        }
    }
    public static void main(String[] args) {
        List<Point> list = new List<>(
            new Point(0, 3),
            new Point(2, 3),
            new Point(1, 1),
            new Point(2, 1),
            new Point(3, 0),
            new Point(0, 0),
            new Point(3, 3)
        );
        ArrayList<Point> hull = computerHull(points).toString();
        System.out.println(hull.toString());
        findPockets(hull, list);
    }
}