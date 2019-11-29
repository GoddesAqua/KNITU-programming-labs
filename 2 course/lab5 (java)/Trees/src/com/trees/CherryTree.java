package com.trees;

public class CherryTree extends Tree implements GardenTree {
    public CherryTree(Integer age, Integer fruiting) {
        super(age, fruiting);
    }

    @Override
    public Boolean transfer() {
        return (age > 10) & (fruiting < 200);
    }
}
