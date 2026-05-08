import java.util.Scanner;

public class Pajak {
    public static void main(String[] args) {
        System.out.println("Masukkan penghasilan: ");
        try (Scanner sc = new Scanner(System.in)) {
            long p = sc.nextLong(), s = p;
            double l1, l2 = 0, l3 = 0, l4 = 0;

            if (s > 500_000_000) { l4 = (s - 500_000_000) * 0.30; s = 500_000_000; }
            if (s > 250_000_000) { l3 = (s - 250_000_000) * 0.25; s = 250_000_000; }
            if (s > 50_000_000)  { l2 = (s - 50_000_000)  * 0.15; s = 50_000_000; }

            l1 = s * 0.05;
            double total = l1 + l2 + l3 + l4;

            System.out.println("Lapisan 1: " + l1);
            System.out.println("Lapisan 2: " + l2);
            System.out.println("Lapisan 3: " + l3);
            System.out.println("Lapisan 4: " + l4);
            System.out.println("Total Pajak: " + total);
        }
    }
}