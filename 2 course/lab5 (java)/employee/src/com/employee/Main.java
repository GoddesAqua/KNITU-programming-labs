package com.employee;

import java.util.ArrayList;

public class Main {

    public static void main(String[] args) {
        ArrayList<Employee> employees = new ArrayList<>();
        employees.add(new Engineer("test eng", 72, "1-st class"));
        employees.add(new Manager("test man", 14, "stage"));
        employees.add(new Supervisor("test super", 36, "mom's friend son"));
    }
}
