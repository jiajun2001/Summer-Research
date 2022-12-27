public class scriptToTest {

    // Task 1-a
    public static int middleOfThree(int x, int y, int z) {
        if (((y <= x) && (x <= z)) || ((z <= x) && (x <= y))) {
            return x;
        } else if (((x <= y) && (y <= z)) || ((z <= y) && (y <= x))) {
            return y;
        } else {
            return z;
        }
    }

    // Task 1-b
    public static int middleOfThree(int x, int y, int z) {
        int min = x < y ? x : y;
        min = min < z ? min : z;
    
        int max = x > y ? x : y;
        max = max > z ? max : z;
        int middle = x + y + z - min - max;
    
        return middle;
    }

    // Task 1-c
    public static int middleOfThree(int x, int y, int z) {
        if (x < y) {
            if (z < x) {
                return x;
            } else if (z < y) {
                return z;
            } else {
                return y;
            }
        } else {
            if (z < y) {
                return y;
            } else if (z < x) {
                return z;
            } else {
                return x;
            }
        }
    }

    // Task 1-d
    public static int middleOfThree(int x, int y, int z) {
        int lower = x;
        int higher = y;
    
        if (x > y) {
            lower = y;
            higher = x;
        }
        if (z < lower) {
            return lower;
        }
        if (z > higher) {
            return higher;
        }
        return z;
    }

    // Task 1-e
    public static int middleOfThree(int x, int y, int z) {
        if ((x - y) * (x - z) <= 0) {
            return x; 
        } else if ((y - x) * (y - z) <= 0) {
            return y;
        } else {
            return z;
        }
    }

    // Task 2-a
    public static int lunchTime(int branch, int rest, int leaf) {
        int count = 0; 
        for (int i = 0; i <= branch; i = i + 1) {
            if ((i % rest == 0) && (i % leaf == 0)) {
                count = count + 1;
            }
        }
        return count;
    }

    // Task 2-b
    public static int lunchTime(int branch, int rest, int leaf) {
        int gcd = leaf, div = rest; 
        while (div > 0) { // greatest common divisor
            int rem = gcd % div;
            gcd = div;
            div = rem;
        }
        int lcm = (leaf * rest) / gcd; // least common multiple
        return (branch / lcm) + 1;
    }

    // Task 2-c
    public static int lunchTime(int branch, int rest, int leaf) {
        int count = 0; 
        for (int i = 0; i <= branch; i = i + rest) {
            if (i % leaf == 0) {
                count = count + 1; 
            }
        }
        return count;
    }

    // Task 2-d
    public static int lunchTime(int branch, int rest, int leaf) {
        int commonMultiples = branch * gcd(leaf, rest) / (leaf * rest);
        return commonMultiples + 1; // +1: leaf at position 0
    }

    private static int gcd(int x, int y) { // greatest common divisor
        if (y == 0) {
            return x;
        } else {    
            return gcd(y, x % y);
        }
    }

    // Task 2-e
    public static int lunchTime(int branch, int rest, int leaf) {
        int eats = 0;
        int pos = 0, nextLeaf = 0;
        while (pos <= branch) {
            if (pos < nextLeaf) { // next leaf or next rest
                pos = pos + rest;
            } else if (nextLeaf < pos) {
                nextLeaf = nextLeaf + leaf;
            } else { // pos == nextLeaf
                eats = eats + 1;
                pos = pos + rest;
                nextLeaf = nextLeaf + leaf;
            }
        }
        return eats;
    }

    // Task 3-a
    public static double[] closestPair(double[] v) {
        double x = -Double.MAX_VALUE;
        double y = Double.MAX_VALUE;
        for (int i = 0; i < v.length; i = i + 1) {
            for (int j = 0; j < v.length; j = j + 1) {
                if ((i != j) && (v[i] <= v[j]) && (v[j] - v[i] < y - x)) {
                    x = v[i];
                    y = v[j];
                }
            }
        }
        return new double[] {x, y};
    }

    // Task 3-b
    public static double[] closestPair(double[] v) {
        int m = 0;
        int n = 1;
        double near = Math.abs(v[1] - v[0]);
        for (int i = 0; i < v.length; i = i + 1) {
            for (int j = i + 1; j < v.length; j = j + 1) {
                if (Math.abs(v[j] - v[i]) < near) {
                    near = Math.abs(v[j] - v[i]);
                    m = i;
                    n = j;
                }
            }
        }
        if (v[m] < v[n]) {
            return new double[] {v[m], v[n]};
        } else {
            return new double[] {v[n], v[m]};
        }
    }

    // Task 3-c
    public static double[] closestPair(double[] v) {
        double[] sorted = new double[v.length];
        sorted[0] = v[0]; // sorts the numbers
        for (int i = 1; i < v.length; i = i + 1) {
            int j = i;
            while ((j > 0) && (v[i] < sorted[j - 1])) {
                sorted[j] = sorted[j - 1];
                j = j - 1;
            }
            sorted[j] = v[i];
        }
        double x = sorted[0];
        double y = sorted[1];
        for (int i = 2; i < sorted.length; i = i + 1) {
            if (sorted[i] - sorted[i - 1] < y - x) {
                x = sorted[i - 1];
                y = sorted[i];
            }
        }
        return new double[] {x, y};
    }

    // Task 3-d
    public static double[] closestPair(double[] v) {
        double[] sorted = sort(v, 0, v.length); // sorts the numbers
        double x = sorted[0];
        double y = sorted[1];
        for (int i = 2; i < sorted.length; i = i + 1) {
            if (sorted[i] - sorted[i - 1] < y - x) {
                x = sorted[i - 1];
                y = sorted[i];
            }
        }
        return new double[] {x, y};
    }

    private static double[] sort(double[] v, int b, int t) {
        int m = (b + t) / 2;
        double[] x;
        if (b + 1 == m) {
            x = new double[] {v[b]};
        } else {
            x = sort(v, b, m);
        }
        double[] y;
        if (m + 1 == t) {
            y = new double[] {v[m]};
        } else {
            y = sort(v, m, t);
        }
        double[] sorted = new double[t - b];
        int i = 0;
        int j = 0;
        for (int k = 0; k < sorted.length; k = k + 1) {
            if ((j == y.length) || ((i < x.length) && (x[i] < y[j]))) {
                sorted[k] = x[i];
                i = i + 1;
            } else {
                sorted[k] = y[j];
                j = j + 1;
            }
        }
        return sorted;
    }

    // Task 3-e
    public static double[] closestPair(double[] v) {
        int n = 0;
        double near = 0;
        for (int i = 0; i < v.length - 1; i = i + 1) {
            double dist = Math.abs(v[i + 1] - v[i]);
            int k = i + 1;
            for (int j = i + 2; j < v.length; j = j + 1) {
                if (Math.abs(v[j] - v[i]) < dist) {
                    dist = Math.abs(v[j] - v[i]);
                    k = j;
                }
            }
            if ((i == 0) || (dist < near)) {
                near = dist;
                n = ((v[i] < v[k]) ? i : k);
            }
        }
        return new double[] {v[n], v[n] + near};
    }

    // Task 4-a
    public static boolean symmetricalMatrix(double[][] q) {
        int n = q.length;
        for (int i = 0; i < n; i = i + 1) {
            for (int j = 0; j < n; j = j + 1) {
                if (q[i][j] != q[j][i]) {
                    return false;
                }
            }
        }
        return true;
    }

    // Task 4-b
    public static boolean symmetricalMatrix(double[][] q) {
        int n = q.length;
        for (int i = 0; i < n; i = i + 1) {
            for (int j = i + 1; j < n; j = j + 1) {
                if (q[i][j] != q[j][i]) {
                    return false;
                }
            }
        }
        return true;
    }

    // Task 4-c
    public static boolean symmetricalMatrix(double[][] q) {
        int n = q.length;
        boolean check = true;
        for (int i = 1; (check && i < n); i = i + 1) {
            for (int j = 0; (check && j < i); j = j + 1) {
                if (q[i][j] != q[j][i]) {
                    check = false;
                }
            }
        }
        return check;
    }

    // Task 4-d
    public static boolean symmetricalMatrix(double[][] q) {
        int n = q.length;
        boolean check = true;
        int i = 0;
        int j = 1;
        while (i < n) {
            if (q[i][j] != q[j][i]) {
                check = false;
                break;
            } else if (j + 1 < n) {
                j = j + 1;
            } else {
                i = i + 1;
                j = 0;
            }
        }
        return check;
    }

    // Task 4-e
    public static boolean symmetricalMatrix(double[][] q) {
        int n = q.length;
        int i = 1; // proceeds along diagonals
        int j = 0;
        while (i + j < 2 * n - 2) {
            if (q[i][j] != q[j][i]) { // diagonal: i+j is invariant
                return false;
            } else if ((i - 1 > 0) && (j + 1 < n)) {
                i = i - 1;
                j = j + 1;
            } else {
                int k = i + j + 1;
                i = Math.min(k, n - 1);
                j = k - i;
            }
        }
        return true;
    }

}