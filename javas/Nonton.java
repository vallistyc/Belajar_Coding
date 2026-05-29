import java.text.NumberFormat;
import java.util.Locale;
import java.util.Scanner;

public class Nonton {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        NumberFormat rupiah = NumberFormat.getNumberInstance(Locale.forLanguageTag("id-ID"));

        while (true) {
            System.out.println("Paket tersedia :");
            System.out.println("1. Paket Basic (SD) : Rp 50.000");
            System.out.println("2. Paket Standard (HD) : Rp 100.000");
            System.out.println("3. Paket Premium (4K) : Rp 150.000");

            System.out.print("Pilih paket (1-3, ketik q untuk keluar) :");
            String pkt = sc.nextLine();
            if (isExit(pkt)) {
                System.out.println("Program Selesai");
                break;
            }
            System.out.println();

            System.out.println("Durasi langganan :");
            System.out.println("1. Bulanan: +0%");
            System.out.println("2. 3 bulan: diskon 5%");
            System.out.println("3. 6 bulan: diskon 10%");
            System.out.println("4. Tahunan: diskon 15%");

            System.out.print("Pilih durasi langganan (1-4, ketik q untuk keluar) :");
            String durasi = sc.nextLine();
            if (isExit(durasi)) {
                System.out.println("Program Selesai");
                break;
            }
            System.out.println();

            System.out.println("Jumlah perangkat :");
            System.out.println("1. 1 perangkat: +0%");
            System.out.println("2. 2 perangkat: +20%");
            System.out.println("3. 4 perangkat: +40%");

            System.out.print("Pilih jumlah perangkat (1-3, ketik q untuk keluar) :");
            String dev = sc.nextLine();
            if (isExit(dev)) {
                System.out.println("Program Selesai");
                break;
            }
            System.out.println();

            System.out.println("Biaya tambahan :");
            System.out.println("1. Konten sport: +Rp 25.000 per bulan");
            System.out.println("2. Download offline: +Rp 15.000 per bulan");

            System.out.print("Pilih biaya tambahan (1-2, ketik q untuk keluar) :");
            String add = sc.nextLine();
            if (isExit(add)) {
                System.out.println("Program Selesai");
                break;
            }
            System.out.println();

            int biayaPkt = 0;
            String strPkt = "";
            if (pkt.equals("1")) {
                biayaPkt = 50000;
                strPkt = "Paket Basic (SD)";
            } else if (pkt.equals("2")) {
                biayaPkt = 100000;
                strPkt = "Paket Standard (HD)";
            } else if (pkt.equals("3")) {
                biayaPkt = 150000;
                strPkt = "Paket Premium (4K)";
            }

            double diskonDurasi = 0;
            String strDurasi = "";
            if (durasi.equals("1")) {
                diskonDurasi = 0;
                strDurasi = "Bulanan";
            } else if (durasi.equals("2")) {
                diskonDurasi = 0.05;
                strDurasi = "3 bulan";
            } else if (durasi.equals("3")) {
                diskonDurasi = 0.10;
                strDurasi = "6 bulan";
            } else if (durasi.equals("4")) {
                diskonDurasi = 0.15;
                strDurasi = "Tahunan";
            }

            double biayaDev = 0;
            String strDev = "";
            if (dev.equals("1")) {
                biayaDev = 0;
                strDev = "1 perangkat";
            } else if (dev.equals("2")) {
                biayaDev = 0.20;
                strDev = "2 perangkat";
            } else if (dev.equals("3")) {
                biayaDev = 0.40;
                strDev = "4 perangkat";
            }

            int biayaAdd = 0;
            String strAdd = "Tidak ada biaya tambahan";
            if (add.equals("1")) {
                biayaAdd = 25000;
                strAdd = "Konten sport";
            } else if (add.equals("2")) {
                biayaAdd = 15000;
                strAdd = "Download offline";
            }

            double total = biayaPkt * (1 - diskonDurasi) * (1 + biayaDev) + biayaAdd;
            System.out.println("Paket: " + strPkt);
            System.out.println("Durasi: " + strDurasi);
            System.out.println("Perangkat: " + strDev);
            System.out.println("Biaya Tambahan: " + strAdd);
            System.out.println("-----------------------------");
            System.out.println("Total biaya yang harus dibayar: Rp " + rupiah.format(total));

            System.out.print("Reset pilihan? (y/n) :");
            String val = sc.nextLine();
            if (val.equalsIgnoreCase("y") || val.equalsIgnoreCase("yes")) {
                System.out.println("Pilihan direset. Silakan pilih paket lagi.");
                System.out.println();
            } else {
                System.out.println("Program Selesai");
                break;
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
