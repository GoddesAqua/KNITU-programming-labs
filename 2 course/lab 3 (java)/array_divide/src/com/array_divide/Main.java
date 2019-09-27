package com.array_divide;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.print("Выберите опцию:\n" +
                "1. Вывести числа которые делятся на 3 и 9\n" +
                "2. Вывести числа которые делятся на 5 и 10\n" +
                "В случае неверного ввода будет выбран первый вариант\n");
        int first, second;
        switch(input.nextInt()){
            case 1:
                first = 3; second = 9;
            case 2:
                first = 5; second = 10;
            default:
                first = 3; second = 9;
        }
        int n = input.nextInt();
        int list[] = new int[n];
        for (int i = 0; i < n; i++) {
            list[i] = input.nextInt();
        }
        System.out.printf("Делятся на %d: ", first);
        for (int i = 0; i < n; i++) {
            if (list[i] % first == 0) {
                System.out.print(list[i]);
                System.out.print(" ");
            }
        }
        System.out.printf("\nДелятся на %d: ", second);
        for (int i = 0; i < n; i++) {
            if (list[i] % second == 0) {
                System.out.print(list[i]);
                System.out.print(" ");
            }
        }
    }
}
