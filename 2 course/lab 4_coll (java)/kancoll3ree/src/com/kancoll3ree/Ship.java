package com.kancoll3ree;

import java.util.ArrayList;

public class Ship implements Comparable<Ship> {
    String name;
    String rank;
    private static ArrayList<String> ranks;

    Ship(String name1, String rank1) {
        this.name = name1;
        if(ranks.contains(rank1)){
            this.rank = rank1;
        }
        else{
            throw new IllegalArgumentException("Допустимые ранги кораблей: ");
        }
    }

    public int compareTo(Ship ship){
        Integer rankIndex = ranks.indexOf(this.rank);
        Integer shipRankIndex = ranks.indexOf(ship.rank);
        if(rankIndex > shipRankIndex){
            return 1;
        }
        else {
            return -1;
        }
    }

    static {
        ranks = new ArrayList<>();
        ranks.add("Эсминец");
        ranks.add("Лёгкий крейсер");
        ranks.add("Линкор");
        ranks.add("Авианосец");
    }
}
