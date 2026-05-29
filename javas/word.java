import java.util.ArrayList;
import java.util.Arrays;
import java.util.Scanner;

public class word {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        ArrayList<String> keluarKalimat = new ArrayList<>(Arrays.asList("q", "quit", "exit", "keluar", "metu"));
        ArrayList<String> keluarKata = new ArrayList<>(Arrays.asList("q", "metu", "keluar", "exit"));

        while (true) {
            System.out.print("Masukkan kalimat (ketik q untuk keluar): ");
            String kal = sc.nextLine().toLowerCase();

            if (keluarKalimat.contains(kal)) {
                System.out.println("program selesai");
                break;
            }

            System.out.print("Masukkan Kata Terlarang (ketik q untuk keluar): ");
            String ter = sc.nextLine().toLowerCase();

            if (keluarKata.contains(ter)) {
                System.out.println("program selesai");
                break;
            }

            String[] kata = kal.split("\\s+");
            ArrayList<String> kataFiltered = new ArrayList<>();

            for (String katas : kata) {
                if (katas.contains("-")) {
                    kataFiltered.addAll(Arrays.asList(katas.split("-")));
                } else {
                    kataFiltered.add(katas);
                }
            }

            if (kataFiltered.contains(ter)) {
                System.out.println("Kalimat mengandung kata " + ter);
            } else {
                System.out.println("Kalimat TIDAK mengandung kata terlarang");
            }
        }

        sc.close();
    }
}
