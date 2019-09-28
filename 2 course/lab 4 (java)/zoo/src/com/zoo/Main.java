package com.zoo;

public class Main {

    public static void main(String[] args) {
        Animal[] animals = new Animal[3];
        animals[0] = new Neko("Chocola", 9, 12);
        animals[1] = new Neko("Vanilla", 10, 13);
        animals[2] = new Butterfly("Brassica", 2, 4);
        Animal older = animals[0];
        for(Animal animal: animals){
            System.out.printf("Имя: %s Возраст: %d", animal.getName(), animal.getAge());
            if(animal.getAge() > older.getAge()){
                older = animal;
            }
            if(animal instanceof Neko){
                System.out.printf(" Длина хвоста: %d", ((Neko) animal).getTailLength());
            }
            else if(animal instanceof Butterfly) {
                System.out.print(" Размах крыльев: " + ((Butterfly) animal).getWingspan());
            }
            System.out.println();
        }
        System.out.printf("\nСтарейшее животное\nИмя: %s Возраст: %d", older.getName(), older.getAge());
    }
}
