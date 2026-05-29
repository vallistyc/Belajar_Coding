import java.util.Scanner;

public class Beasiswa {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Masukkan total dana beasiswa (Rp): ");
        double totalDana = sc.nextDouble();

        System.out.print("Masukkan persentase beasiswa unggulan (contoh: 15): ");
        double persenUnggulan = sc.nextDouble();

        System.out.print("Masukkan penyebut pecahan tiap beasiswa prestasi (contoh: 10): ");
        double penyebutPrestasi = sc.nextDouble();

        // a) Beasiswa Unggulan
        double unggulan = (persenUnggulan / 100) * totalDana;

        // Sisa setelah unggulan
        double sisa1 = totalDana - unggulan;

        // b) Tiap Beasiswa Prestasi (ada 4, masing-masing 1/penyebut dari sisa1)
        double tiapPrestasi = (1 / penyebutPrestasi) * sisa1;
        double totalPrestasi = 4 * tiapPrestasi;

        // Sisa setelah prestasi
        double sisa2 = sisa1 - totalPrestasi;

        // 6 Beasiswa Bantuan dengan rasio 7:5:4:3:2:1, total rasio = 22
        double satuBagian = sisa2 / 22;

        double bantuan1 = 7 * satuBagian;
        double bantuan2 = 5 * satuBagian;
        double bantuan3 = 4 * satuBagian;
        double bantuan4 = 3 * satuBagian;
        double bantuan5 = 2 * satuBagian;
        double bantuan6 = 1 * satuBagian;

        // c) Unggulan + 1 Prestasi
        double gabungan = unggulan + tiapPrestasi;

        System.out.println("a) Dana beasiswa unggulan: Rp " + unggulan);
        System.out.println("b) Dana tiap beasiswa prestasi: Rp " + tiapPrestasi);
        System.out.println("c) Dana unggulan + 1 prestasi: Rp " + gabungan);
        System.out.println("Detail beasiswa bantuan:");
        System.out.println("   Bantuan 1: Rp " + bantuan1);
        System.out.println("   Bantuan 2: Rp " + bantuan2);
        System.out.println("   Bantuan 3: Rp " + bantuan3);
        System.out.println("   Bantuan 4: Rp " + bantuan4);
        System.out.println("   Bantuan 5: Rp " + bantuan5);
        System.out.println("   Bantuan 6: Rp " + bantuan6);

        sc.close();
    }
}