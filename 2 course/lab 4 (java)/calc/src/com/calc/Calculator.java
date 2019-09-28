package com.calc;
import java.lang.Math;

public class Calculator {
    public double solve(double a, String sign, double b){
        switch (sign) {
            case "+":
                return a + b;
            case "-":
                return a - b;
            case "*":
                return a * b;
            case "/":
                return a / b;
            default:
                throw new IllegalStateException("Unexpected value: " + sign);
        }
    }
    public double solve(String sign, double a) {
        switch (sign) {
            case "sqrt":
                return Math.sqrt(a);
            case "cbrt":
                return Math.cbrt(a);
            case "ln":
                return Math.log(a);
            default:
                throw new IllegalStateException("Unexpected value: " + sign);
        }
    }
}
