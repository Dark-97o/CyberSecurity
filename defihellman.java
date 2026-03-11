import java.util.Scanner;

public class DiffieHellmanSwitch {

    static long power(long a, long b, long mod) {
        long result = 1;
        for(int i = 0; i < b; i++) {
            result = (result * a) % mod;
        }
        return result;
    }

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        long p, g, a, b;
        long A = 0, B = 0, keyA = 0, keyB = 0;
        int choice;

        System.out.print("Enter prime number p: ");
        p = sc.nextLong();

        System.out.print("Enter primitive root g: ");
        g = sc.nextLong();

        System.out.print("Enter private key of User A: ");
        a = sc.nextLong();

        System.out.print("Enter private key of User B: ");
        b = sc.nextLong();

        do {
            System.out.println("\n--- Diffie Hellman Menu ---");
            System.out.println("1. Generate Public Key of A");
            System.out.println("2. Generate Public Key of B");
            System.out.println("3. Generate Secret Key for A");
            System.out.println("4. Generate Secret Key for B");
            System.out.println("5. Exit");

            System.out.print("Enter choice: ");
            choice = sc.nextInt();

            switch(choice) {

                case 1:
                    A = power(g, a, p);
                    System.out.println("Public Key of A: " + A);
                    break;

                case 2:
                    B = power(g, b, p);
                    System.out.println("Public Key of B: " + B);
                    break;

                case 3:
                    keyA = power(B, a, p);
                    System.out.println("Secret Key for A: " + keyA);
                    break;

                case 4:
                    keyB = power(A, b, p);
                    System.out.println("Secret Key for B: " + keyB);
                    break;

                case 5:
                    System.out.println("Exiting...");
                    break;

                default:
                    System.out.println("Invalid Choice");
            }

        } while(choice != 5);

        sc.close();
    }
}