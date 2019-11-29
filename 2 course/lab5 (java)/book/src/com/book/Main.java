package com.book;

import java.util.ArrayList;

public class Main {

    public static void main(String[] args) {
        ArrayList<Book> books = new ArrayList<>();
        books.add(new Directory("dfjkd", "Author", "test directory", "2007",
                "prosveshenie"));
        books.add(new Dict("dkjfkd", "Author", "test dict", "2008", "drofa"));
    }
}
