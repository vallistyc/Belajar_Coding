import java.util.Scanner;

public class nasgor {
    public static void main(String[] args) {

        try (Scanner input = new Scanner(System.in)) {

            double hargaBeli;
            double hargaJual;
            double biayaTambahan;
            double keuntungan;

            // input user
            System.out.print("Masukkan harga beli per porsi : ");
            hargaBeli = input.nextDouble();

            System.out.print("Masukkan harga jual per porsi : ");
            hargaJual = input.nextDouble();

            // biaya gas dan bumbu 12%
            biayaTambahan = 0.12 * hargaBeli;

            // hitung keuntungan
            keuntungan = hargaJual - hargaBeli - biayaTambahan;

            // output
            System.out.println("\n=== HASIL PERHITUNGAN ===");
            System.out.println("Harga beli : Rp" + hargaBeli);
            System.out.println("Harga jual : Rp" + hargaJual);
            System.out.println("Biaya tambahan : Rp" + biayaTambahan);
            System.out.println("Keuntungan per porsi : Rp" + keuntungan);
        }
    }
}