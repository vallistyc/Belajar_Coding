import java.util.Scanner;

public class loop {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        while (true) {
            System.out.print("Masukkan jumlah perulangan (ketik q untuk keluar):");
            String input = sc.nextLine();

            if (input.equals("q")) {
                break;
            }

            int n;
            try {
                n = Integer.parseInt(input);
            } catch (NumberFormatException e) {
                System.out.println("Input tidak valid. Harap masukkan angka.");
                continue;
            }

            for (int line = 1; line <= n; line++) {
                for (int number = 1; number <= line; number++) {
                    System.out.print(number + " ");
                }
                System.out.println();
            }

            for (int line = n; line > 1; line--) {
                for (int number = 1; number < line; number++) {
                    System.out.print(number + " ");
                }
                System.out.println();
            }
        }

        sc.close();
    }
}
