import java.util.Scanner;

public class Kubus {
    public static void main(String[] args) {
        try (Scanner sc = new Scanner(System.in)) {
            System.out.println("Masukkan sisi kubus:");
            double R = sc.nextDouble();
            System.out.println("Masukkan jari-jari:");
            double r = sc.nextDouble();
            System.out.println("Masukkan tinggi:");
            double h = sc.nextDouble();

            double volumeSisa = Math.pow(R, 3) - (Math.PI * r * r * h / 3);
            double s = Math.sqrt(r * r + h * h);
            double luasSisa = 6 * R * R - Math.PI * r * r + Math.PI * r * s;

            System.out.println("Volume sisa: " + volumeSisa);
            System.out.println("Luas permukaan sisa: " + luasSisa);
        }
    }
}