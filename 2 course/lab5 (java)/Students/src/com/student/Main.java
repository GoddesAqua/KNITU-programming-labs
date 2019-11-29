package com.student;

import java.util.ArrayList;

public class Main {

    public static void main(String[] args) {
        ArrayList<Student> students = new ArrayList<>();
        ArrayList<Schoolboy> schoolboys = new ArrayList<>();
        ArrayList<Undergraduate> undergraduates = new ArrayList<>();
        students.add(new Schoolboy("Alex", 9, 16));
        students.add(new Schoolboy("Lora", 11, 18));
        students.add(new Undergraduate("Elise", 2, 19));
        students.add(new Undergraduate("Ming", 1, 18));
        for(Student st: students){
            if(st instanceof Schoolboy){
                schoolboys.add((Schoolboy) st);
            }
            else if(st instanceof Undergraduate){
                undergraduates.add((Undergraduate) st);
            }
        }
        System.out.println("Schoolboys: ");
        for(Schoolboy schoolboy: schoolboys){
            System.out.printf("name: %s age: %d course: %d%n", schoolboy.name, schoolboy.age, schoolboy.course);
        }
        System.out.println("Undergraduates: ");
        for(Undergraduate undergraduate: undergraduates){
            System.out.printf("name: %s age: %d course: %d%n",
                    undergraduate.name, undergraduate.age, undergraduate.course);
        }
    }
}
