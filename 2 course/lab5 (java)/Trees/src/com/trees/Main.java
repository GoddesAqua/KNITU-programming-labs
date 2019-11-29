package com.trees;

import java.util.ArrayList;

public class Main {

    public static void main(String[] args) {
        ArrayList<GardenTree> gardenTrees = new ArrayList<>();
        gardenTrees.add(new AppleTree(20, 100));
        gardenTrees.add(new CherryTree(1, 1));
        gardenTrees.add(new PearTree(100, 1));
        gardenTrees.add(new MelonTree(2, 2));
        for(GardenTree gardenTree: gardenTrees){
            System.out.printf("%d. Age: %d Fruiting: %d Need to transfer: %b%n",
                    gardenTree.getNum(), gardenTree.getAge(), gardenTree.getFruiting(), gardenTree.transfer());
        }
    }
}
