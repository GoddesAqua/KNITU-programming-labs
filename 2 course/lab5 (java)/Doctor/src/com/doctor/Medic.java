package com.doctor;

public abstract class Medic {
    String name;
    Integer age;
    String qualification;

    public Medic(String name, Integer age, String qualification) {
        this.name = name;
        this.age = age;
        this.qualification = qualification;
    }
}
