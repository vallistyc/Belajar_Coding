import java.util.Scanner;

public class Nomor {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        boolean valid = false;

        while (!valid) {
            System.out.print("Masukkan nomor:");
            String num = sc.nextLine();

            if (num.contains(" ")) {
                System.out.println("Error: Nomor telepon tidak boleh mengandung spasi");
                continue;
            }

            String fltdNum;
            if (num.startsWith("+62")) {
                fltdNum = num.substring(3);
            } else if (num.startsWith("62")) {
                fltdNum = num.substring(2);
            } else if (num.startsWith("0")) {
                fltdNum = num.substring(1);
            } else {
                System.out.println("Error: format tidak valid");
                continue;
            }

            if (!fltdNum.matches("\\d+")) {
                System.out.println("Error: Input wajib berupa angka");
                continue;
            }

            if (fltdNum.length() < 10 || fltdNum.length() > 13) {
                System.out.println("Error: Panjang digit harus di range 10-13");
                continue;
            }

            int duaDigit = Integer.parseInt(fltdNum.substring(0, 2));

            if (duaDigit < 11 || duaDigit > 99) {
                System.out.println("Error: Dua digit awal (" + fltdNum.substring(0, 2) + ") tidak valid");
                continue;
            }

            valid = true;
            System.out.println("Valid! Nomor " + num + " memenuhi semua syarat.");
        }

        sc.close();
    }
}
