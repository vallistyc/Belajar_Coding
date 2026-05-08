import java.util.Scanner;

public class Ekspansi {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Masukkan bilangan 3 digit: ");
        int n = sc.nextInt();

        int r = n / 100;
        int p = (n % 100) / 10;
        int s = n % 10;

        System.out.println("Bilangan " + n + " = " 
            + (r*100) + " + " + (p*10) + " + " + s);
        sc.close();
    }
}