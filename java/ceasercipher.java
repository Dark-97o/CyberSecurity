package CyberSecurity.java;
import java.util.Scanner;

public class ceasercipher {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String str;
        int key;
        String encryptedMessage = ""; // Store encrypted message

        System.out.println("Enter message:");
        str = sc.nextLine();

        System.out.println("Enter numeric encryption key:");
        key = sc.nextInt(); // key as integer

        for (;;) {
            System.out.println("\n1. Encrypt\n2. Decrypt\n3. Exit");
            int choice = sc.nextInt();

            switch (choice) {
                case 1:
                    encryptedMessage = encrypt(str, key);
                    System.out.println("Encrypted message: " + encryptedMessage);
                    break;

                case 2:
                    if (encryptedMessage.equals("")) {
                        System.out.println("Please encrypt a message first!");
                    } else {
                        String decrypted = decrypt(encryptedMessage, key);
                        System.out.println("Decrypted message: " + decrypted);
                    }
                    break;

                case 3:
                    System.out.println("Exiting...");
                    System.exit(0);

                default:
                    System.out.println("Invalid option, try again!");
                }
        }
    }

    // Encryption function
    public static String encrypt(String str, int key) {
        String encrypted = "";
        for (int i = 0; i < str.length(); i++) {
            char c = str.charAt(i);

            if (Character.isUpperCase(c)) {
                c = (char) ((c - 'A' + key) % 26 + 'A');
            } else if (Character.isLowerCase(c)) {
                c = (char) ((c - 'a' + key) % 26 + 'a');
            }

            encrypted += c;
        }
        return encrypted;
    }

    // Decryption function
    public static String decrypt(String str, int key) {
        String decrypted = "";
        for (int i = 0; i < str.length(); i++) {
            char c = str.charAt(i);

            if (Character.isUpperCase(c)) {
                c = (char) ((c - 'A' - key + 26) % 26 + 'A');
            } else if (Character.isLowerCase(c)) {
                c = (char) ((c - 'a' - key + 26) % 26 + 'a');
            }

            decrypted += c;
        }
        return decrypted;
    }
}