package com.book;

public abstract class Book {
    String cipher;
    String author;
    String name;
    String year;
    String publisher;

    public Book(String cipher, String author, String name, String year, String publisher) {
        this.cipher = cipher;
        this.author = author;
        this.name = name;
        this.year = year;
        this.publisher = publisher;
    }
}
