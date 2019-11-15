package com.kancoll;

import java.util.HashMap;
import java.util.Scanner;

public class Main {

    public static void main(String[] args){
        HashMap<String, String> fleet = new HashMap<>();
        fleet.put("Хибики", "Эсминец");
        fleet.put("Акацуки", "Эсминец");
        fleet.put("Икадзучи", "Эсминец");
        fleet.put("Инадзума", "Эсминец");
        fleet.put("Ямато", "Линкор");
        fleet.put("Нагато", "Линкор");
        fleet.put("Акаги", "Авианосец");
        fleet.put("Сорю", "Авианосец");
        fleet.put("Тайхо", "Авианосец");
        fleet.put("Нака", "Лёгкий крейсер");
        fleet.put("Сендай", "Лёгкий крейсер");
        fleet.put("Джинцу", "Лёгкий крейсер");
        Scanner input = new Scanner(System.in);
        String type = input.next();
        if(fleet.containsValue(type)){
            for(String key : fleet.keySet()){
                String value = fleet.get(key);
                if(value.equals(type)){
                    System.out.println(key);
                }
            }
        }
        else{
            System.out.println("Кораблей такого класса нет, Адмирал");
        }
    }
}
