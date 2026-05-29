import java.util.Scanner;

public class kelas {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // Data mk kro kelas, ditaruh di luar loop biar tidak dibuat ulang terus.
        String[][] data = {
            {"MK101", "A"},
            {"MK101", "B"},
            {"MK202", "A"},
            {"MK203", "C"},
            {"MK304", "B"}
        };

        while (true) {
            System.out.print("Masukkan kode matkul (ketik q untuk keluar) :");
            String mk = sc.nextLine();

            if (isExit(mk)) {
                System.out.println("Program Selesai");
                break;
            }

            System.out.print("Masukkan kelas (ketik q untuk keluar) :");
            String kls = sc.nextLine();

            if (isExit(kls)) {
                System.out.println("Program Selesai");
                break;
            }

            boolean tersedia = false;
            for (int i = 0; i < data.length; i++) {
                if (data[i][0].equals(mk) && data[i][1].equals(kls)) {
                    tersedia = true;
                    break;
                }
            }

            if (tersedia) {
                System.out.println("Kelas tersedia untuk matkul " + mk + " kelas " + kls);
            } else {
                System.out.println("Kelas tidak tersedia untuk matkul " + mk + " kelas " + kls);
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
