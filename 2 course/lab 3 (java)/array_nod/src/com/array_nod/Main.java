package com.array_nod;
import java.util.Scanner;

public class Main {

    private static int nod_calc(int a, int b) {
        if (b == 0)
            return Math.abs(a);
        return nod_calc(b, a % b);
    }

    private static int nok_calc(int a, int b) {
        return (a*b)/nod_calc(a, b);
    }

    public static void main(String[] args) {
        int nod, nok, P;
        P = 1;
        Scanner input = new Scanner(System.in);
        int n = input.nextInt();
        int list[] = new int[n];
        for (int i = 0; i < n; i++) {
            list[i] = input.nextInt();
        }
        for(int i = 0; i < n; i++){
            P *= list[i];
        }
        nod = list[0];
        nok = list[0];
        for(int i =1; i < n; i++){
            nod = nod_calc(nod, list[i]);
            nok = nok_calc(nok, list[i]);
        }
        System.out.printf("Нод: %d\nНок: %d", nod, nok);
    }
}
