package com.kancoll2;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.Scanner;

public class Main {

    private static ArrayList<String> ranks = new ArrayList<>();
    private static LinkedList<String> fleetQueue = new LinkedList<>();
    private static HashMap<String, String> fleet = new HashMap<>();

    private static void addToFleetQueue(String ship) {
        if(fleet.containsKey(ship)){
            int shipRankIndex = ranks.indexOf(fleet.get(ship));
            int queueShipRankIndex;
            int delta;
            int minDelta = ranks.size() + 1;
            int minDeltaShipIndex = -1;
            for(String queueShip: fleetQueue){
                queueShipRankIndex = ranks.indexOf(fleet.get(queueShip));
                delta = shipRankIndex - queueShipRankIndex;
                if((delta > 0) & (delta<=minDelta)){
                    minDelta = delta;
                    minDeltaShipIndex = fleetQueue.indexOf(queueShip);
                }
            }
            if(minDeltaShipIndex >= 0){
                fleetQueue.add(minDeltaShipIndex+1, ship);
            }
            else{
                fleetQueue.add(ship);
            }
        }
    }

    public static void main(String[] args) {
        ranks.add("Эсминец");
        ranks.add("Лёгкий крейсер");
        ranks.add("Линкор");
        ranks.add("Авианосец");
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
        System.out.println(ranks);
        Scanner input = new Scanner(System.in);
        while(true){
            String ship = input.next();
            if(!(ship.equals("0"))){
                addToFleetQueue(ship);
                System.out.println(fleetQueue);
            }
            else{
                break;
            }
        }
    }
}
