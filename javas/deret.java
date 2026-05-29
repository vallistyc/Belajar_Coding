import java.util.Scanner;
import java.util.ArrayList;
import java.math.BigInteger;

public class deret {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        BigInteger hasil = BigInteger.ZERO;
        ArrayList<String> strA = new ArrayList<>();

        while (true) {
            System.out.print("Masukkan jumlah deret (keluar ketik 'q') :");
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

            for (int i = 1; i <= n; i++) {
                BigInteger a = BigInteger.valueOf(5).pow(i);
                hasil = hasil.add(a);
                strA.add("5^" + i);
            }

            System.out.println("Deret yang dihitung:");
            System.out.println(String.join(" + ", strA) + " = " + hasil);
            System.out.println();
        }

        sc.close();
    }
}
