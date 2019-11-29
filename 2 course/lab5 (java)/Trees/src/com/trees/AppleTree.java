package com.trees;

public class AppleTree extends Tree implements GardenTree {
    public AppleTree(Integer age, Integer fruiting) {
        super(age, fruiting);
    }

    @Override
    public Boolean transfer() {
        return (age > 5) & (fruiting < 20);
    }
}
