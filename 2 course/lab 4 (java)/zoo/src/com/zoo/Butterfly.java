package com.zoo;

public class Butterfly extends Animal {
    private int wingspan;

    public Butterfly(String name, int age, int wingspan) {
        super(name, age);
        this.wingspan = wingspan;
    }

    public int getWingspan(){
        return this.wingspan;
    }
}
