import java.nio.charset.StandardCharsets;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.util.Scanner;

public class Ewalet {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int saldo = 500000;
        String pin = "";
        int kesalahanPin = 0;

        while (true) {
            System.out.print("Masukkan PIN baru anda: ");
            String pinInput = sc.nextLine();

            if (pinInput.matches("\\d{6}")) {
                pin = hashSha256(pinInput);
                System.out.println("PIN anda tersimpan dan terenkripsi");
                break;
            } else {
                System.out.println("PIN harus berupa 6 digit angka!");
            }
        }

        boolean running = true;
        System.out.println("Dompet Digital Anda");
        System.out.println("Saldo Awal: Rp " + formatRupiah(saldo));

        while (running) {
            if (saldo <= 0) {
                System.out.println("Saldo habis. Aplikasi ditutup.");
                break;
            }

            if (kesalahanPin >= 3) {
                System.out.println("Anda telah salah PIN 3 kali berturut-turut.");
                System.out.println("Aplikasi terkunci.");
                break;
            }

            System.out.println("\nMENU");
            System.out.println("1. Cek Saldo");
            System.out.println("2. Top Up");
            System.out.println("3. Bayar");
            System.out.println("4. Transfer");
            System.out.println("5. Ganti PIN");
            System.out.println("6. Keluar");

            System.out.print("Pilihan: ");
            String pilihan = sc.nextLine();

            if (pilihan.equals("1")) {
                System.out.println("Saldo Anda: Rp " + formatRupiah(saldo));

            } else if (pilihan.equals("2")) {
                System.out.print("Masukkan nominal top up: Rp ");
                int nominal = Integer.parseInt(sc.nextLine());

                if (nominal <= 0) {
                    System.out.println("Nominal tidak valid");
                } else {
                    saldo += nominal;
                    System.out.println("Top up berhasil! Saldo sekarang: Rp " + formatRupiah(saldo));
                }

            } else if (pilihan.equals("3")) {
                System.out.print("Masukkan nominal pembayaran: Rp ");
                int nominal = Integer.parseInt(sc.nextLine());

                if (nominal > saldo) {
                    System.out.println("Error: Saldo tidak cukup");
                } else {
                    while (true) {
                        System.out.print("Masukkan PIN: ");
                        String inputPin = sc.nextLine();
                        String hashedInput = hashSha256(inputPin);

                        if (hashedInput.equals(pin)) {
                            saldo -= nominal;
                            kesalahanPin = 0;
                            System.out.println("Pembayaran berhasil!");
                            System.out.println("Saldo sekarang: Rp " + formatRupiah(saldo));
                            break;
                        } else {
                            kesalahanPin++;
                            System.out.println("Error: PIN salah! (Kesalahan " + kesalahanPin + ")");

                            if (kesalahanPin >= 3) {
                                break;
                            }
                        }
                    }
                }

            } else if (pilihan.equals("4")) {
                System.out.print("Masukkan nomor tujuan: ");
                String tujuan = sc.nextLine();

                System.out.print("Masukkan nominal transfer: Rp ");
                int nominal = Integer.parseInt(sc.nextLine());

                if (nominal > saldo) {
                    System.out.println("Error: Saldo tidak cukup");
                } else {
                    while (true) {
                        System.out.print("Masukkan PIN: ");
                        String inputPin = sc.nextLine();
                        String hashedInput = hashSha256(inputPin);

                        if (hashedInput.equals(pin)) {
                            saldo -= nominal;
                            kesalahanPin = 0;
                            System.out.println("Transfer ke " + tujuan + " berhasil!");
                            System.out.println("Saldo sekarang: Rp " + formatRupiah(saldo));
                            break;
                        } else {
                            kesalahanPin++;
                            System.out.println("Error: PIN salah! (Kesalahan " + kesalahanPin + ")");

                            if (kesalahanPin >= 3) {
                                break;
                            }
                        }
                    }
                }

            } else if (pilihan.equals("5")) {
                System.out.print("Masukkan PIN lama: ");
                String pinLama = sc.nextLine();
                String hashedPinLama = hashSha256(pinLama);

                if (hashedPinLama.equals(pin)) {
                    System.out.print("Masukkan PIN baru: ");
                    String pinBaru = sc.nextLine();

                    if (pinBaru.matches("\\d{6}")) {
                        pin = hashSha256(pinBaru);
                        kesalahanPin = 0;
                        System.out.println("PIN berhasil diganti");
                    } else {
                        System.out.println("PIN harus berupa 6 digit angka!");
                    }
                } else {
                    kesalahanPin++;
                    System.out.println("Error: PIN salah! (Kesalahan " + kesalahanPin + ")");
                }

            } else if (pilihan.equals("6")) {
                System.out.println("Terima kasih telah menggunakan aplikasi.");
                running = false;

            } else {
                System.out.println("Pilihan menu tidak valid");
            }
        }

        sc.close();
    }

    private static String hashSha256(String text) {
        try {
            MessageDigest digest = MessageDigest.getInstance("SHA-256");
            byte[] encodedHash = digest.digest(text.getBytes(StandardCharsets.UTF_8));
            StringBuilder hexString = new StringBuilder();

            for (byte b : encodedHash) {
                String hex = Integer.toHexString(0xff & b);
                if (hex.length() == 1) {
                    hexString.append('0');
                }
                hexString.append(hex);
            }

            return hexString.toString();
        } catch (NoSuchAlgorithmException e) {
            throw new RuntimeException("SHA-256 tidak tersedia", e);
        }
    }

    private static String formatRupiah(int value) {
        return String.format("%,d", value);
    }
}
