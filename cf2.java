import java.util.Scanner;

public class MonocarpGame {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int t = scanner.nextInt();

        for (int i = 0; i < t; i++) {
            int n = scanner.nextInt();
            int[] sequence = new int[n];

            for (int j = 0; j < n; j++) {
                sequence[j] = scanner.nextInt();
            }

            int result = minTeleports(n, sequence);
            System.out.println(result);
        }
    }

    private static int minTeleports(int n, int[] sequence) {
        int minTeleportsCount = 0;
        int prevValue = 0;

        for (int i = 0; i < n; i++) {
            minTeleportsCount = Math.max(minTeleportsCount, sequence[i] - prevValue);
            prevValue = sequence[i];
        }

        return minTeleportsCount;
    }
}