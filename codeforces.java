import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        long t = scanner.nextLong();

        while (t-- > 0) {
            long x = scanner.nextLong();
            long k = scanner.nextLong();
            long[] a = new long[(int) (x + 1)];
            a[0] = 0;

            for (long i = 1; i < x + 1; i++) {
                a[(int) i] = scanner.nextLong();
            }

            long maximum = 0;
            boolean flag = false;

            for (long i = 0; i < x; i++) {
                maximum = Math.max(maximum, (a[(int) (i + 1)] - a[(int) i]));
                flag = true;
            }

            if (flag) {
                long maximum2 = ((k - a[(int) x]) * 2);
                maximum = Math.max(maximum, maximum2);
            }

            System.out.println(maximum);
        }
    }
}
