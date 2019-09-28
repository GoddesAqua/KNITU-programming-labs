package com.calc;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        Calculator calc = new Calculator();
        if(input.hasNextDouble()){
            double solve = calc.solve(input.nextDouble(), input.next(), input.nextDouble());
            System.out.print(solve);
        }
        else{
            double solve = calc.solve(input.next(), input.nextDouble());
            System.out.print(solve);
        }
    }
}
