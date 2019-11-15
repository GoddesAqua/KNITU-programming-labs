package com.kancoll3ree;

import java.util.TreeSet;

public class Main {

    public static void main(String[] args) {
        TreeSet<Ship> fleet = new TreeSet<>();
        fleet.add(new Ship("Хибики", "Эсминец"));
        fleet.add(new Ship("Акацуки", "Эсминец"));
        fleet.add(new Ship("Сендай", "Лёгкий крейсер"));
        fleet.add(new Ship("Икадзучи", "Эсминец"));
        fleet.add(new Ship("Инадзума", "Эсминец"));
        fleet.add(new Ship("Нагато", "Линкор"));
        fleet.add(new Ship("Акаги", "Авианосец"));
        fleet.add(new Ship("Сорю", "Авианосец"));
        fleet.add(new Ship("Тайхо", "Авианосец"));
        fleet.add(new Ship("Нака", "Лёгкий крейсер"));
        fleet.add(new Ship("Ямато", "Линкор"));
        fleet.add(new Ship("Джинцу", "Лёгкий крейсер"));
        for(Ship ship: fleet){
            System.out.printf("%s %s\n", ship.rank, ship.name);
        }
    }
}
