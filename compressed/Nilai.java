import java.util.Scanner;

public class Nilai {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n1 = 65, n2 = 68, n3 = 72, n4 = 75;
        int z = 65 + 22; // z = 87, dari selisih max - min = 22

        int x, y;

        // Input x dengan validasi
        while (true) {
            System.out.print("Masukkan nilai x: ");
            x = sc.nextInt();
            if (x > 0 && x < z) {
                break;
            }
            System.out.println("x harus bilangan bulat positif dan kurang dari " + z);
        }

        // Input y dengan validasi
        while (true) {
            System.out.print("Masukkan nilai y: ");
            y = sc.nextInt();
            if (y > x && y < z) {
                break;
            }
            System.out.println("y harus lebih besar dari " + x + " dan kurang dari " + z);
        }

        // Simpan semua nilai
        int[] nilai = {n1, n2, n3, n4, x, y, z};

        // Urutkan pakai bubble sort
        for (int i = 0; i < 7; i++) {
            for (int j = 0; j < 6 - i; j++) {
                if (nilai[j] > nilai[j + 1]) {
                    int temp = nilai[j];
                    nilai[j] = nilai[j + 1];
                    nilai[j + 1] = temp;
                }
            }
        }

        // Median = elemen ke-4 (index 3) dari 7 data terurut
        int median = nilai[3];

        // Hitung rata-rata
        int total = 0;
        for (int i = 0; i < 7; i++) {
            total = total + nilai[i];
        }
        double rataRata = (double) total / 7;

        // Output
        System.out.print("Nilai terurut: ");
        for (int i = 0; i < 7; i++) {
            System.out.print(nilai[i]);
            if (i < 6) System.out.print(", ");
        }
        System.out.println();
        System.out.println("Median: " + median);
        System.out.println("Rata-rata: " + rataRata);

        sc.close();
    }
}