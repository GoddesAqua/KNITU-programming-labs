package com.trees;

public abstract class Tree {
    static Integer next_num = 0;
    Integer num;
    Integer age;
    Integer fruiting;

    public Tree(Integer age, Integer fruiting) {
        this.num = next_num;
        next_num++;
        this.age = age;
        this.fruiting = fruiting;
    }

    public Integer getAge() {
        return age;
    }

    public Integer getFruiting() {
        return fruiting;
    }

    public Integer getNum() {
        return num;
    }
}
