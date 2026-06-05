import java.util.Random;
import java.util.Scanner;

public class Rgb {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Random random = new Random();

        int r = random.nextInt(256);
        System.out.println(r);

        int maxGuess = 12;

        for (int i = 1; i <= maxGuess; i++) {
            System.out.print("Masukkan R:");
            int guess = sc.nextInt();

            if (guess == r) {
                System.out.println("BENAR");
                break;
            } else if (r - guess <= 10) {
                System.out.println("PANAS");
                System.out.println("Banyak percobaan:" + i);
            } else if (11 <= r - guess && r - guess <= 30) {
                System.out.println("HANGAT");
                System.out.println("Banyak percobaan:" + i);
            } else if (r - guess >= 31) {
                System.out.println("DINGIN");
                System.out.println("Banyak percobaan:" + i);
            }

            if (i == maxGuess) {
                System.out.println("KESEMPATAN MENEBAK HABIS");
                break;
            }
        }

        sc.close();
    }
}
