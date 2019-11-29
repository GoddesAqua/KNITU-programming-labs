package com.trees;

public class PearTree extends Tree implements GardenTree {
    public PearTree(Integer age, Integer fruiting) {
        super(age, fruiting);
    }

    @Override
    public Boolean transfer() {
        return (age > 5) & (fruiting < 30);
    }
}
