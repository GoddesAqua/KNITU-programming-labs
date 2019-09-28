package com.zoo;

public class Neko extends Animal {
    private int tailLength;

    public Neko(String name, int age, int tailLength) {
        super(name, age);
        this.tailLength = tailLength;
    }

    public int getTailLength() {
        return this.tailLength;
    }
}
