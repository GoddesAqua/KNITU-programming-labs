package com.employee;

public abstract class Employee {
    String name;
    Integer age;
    String qualification;

    public Employee(String name, Integer age, String qualification) {
        this.name = name;
        this.age = age;
        this.qualification = qualification;
    }
}
