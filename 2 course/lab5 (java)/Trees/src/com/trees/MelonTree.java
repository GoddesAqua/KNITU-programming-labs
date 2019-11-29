package com.trees;

public class MelonTree extends Tree implements GardenTree {
    public MelonTree(Integer age, Integer fruiting) {
        super(age, fruiting);
    }

    @Override
    public Boolean transfer() {
        return (age > 50) & (fruiting < 2);
    }
}
