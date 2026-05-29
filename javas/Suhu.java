import java.util.Scanner;

public class Suhu {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        while (true) {
            System.out.print("Masukkan suhu dalam Celsius (ketik 'q' untuk keluar): ");
            String input = sc.nextLine();

            if (isExit(input)) {
                System.out.println("Selesai.");
                break;
            }

            double suhu;
            try {
                suhu = Double.parseDouble(input);
            } catch (NumberFormatException e) {
                System.out.println("Masukkan angka yang valid atau ketik 'q' untuk keluar.");
                continue;
            }

            if (suhu > 0 && suhu < 100) {
                System.out.println("Cair");
            } else if (suhu >= 100) {
                System.out.println("Uap (Gas)");
            } else {
                System.out.println("Beku (Padat)");
            }
        }

        sc.close();
    }

    public static boolean isExit(String input) {
        String text = input.toLowerCase();
        return text.equals("q")
            || text.equals("quit")
            || text.equals("exit")
            || text.equals("keluar");
    }
}
