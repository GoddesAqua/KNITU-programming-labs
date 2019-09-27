package com.array_input;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int n = input.nextInt();
        int list[] = new int[n];
        for (int i = 0; i < n; i++) {
            list[i] = input.nextInt();
        }
        System.out.print("Четные числа: ");
        for (int i = 0; i < n; i++) {
            if (list[i] % 2 == 0) {
                System.out.print(list[i] + " ");
            }
        }
        System.out.print("\nНечетные числа: ");
        for (int i = 0; i < n; i++) {
            if (list[i] % 2 == 1) {
                System.out.print(list[i] + " ");
            }
        }
    }
}
