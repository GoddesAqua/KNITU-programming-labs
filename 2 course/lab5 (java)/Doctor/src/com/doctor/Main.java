package com.doctor;

import java.util.ArrayList;

public class Main {

    public static void main(String[] args) {
        ArrayList<Medic> medics = new ArrayList<>();
        medics.add(new Doctor("test doct", 43, "2-nd class"));
        medics.add(new Doctor("test nurse", 27, "stage"));
    }
}
