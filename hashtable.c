// hashtable
#include <stdio.h>
#include <stdlib.h>

#define SIZE 10

struct HashTable {
    int key;
    int value;
} table[SIZE];

void initializeTable() {
    for (int i = 0; i < SIZE; i++)
        table[i].key = -1;
}

int hashFunction(int key) {
    return key % SIZE;
}

void insert(int key, int value) {
    int index = hashFunction(key);
    while (table[index].key != -1)
        index = (index + 1) % SIZE;
    table[index].key = key;
    table[index].value = value;
}

int search(int key) {
    int index = hashFunction(key);
    int start = index;
    while (table[index].key != key) {
        index = (index + 1) % SIZE;
        if (index == start) return -1;
    }
    return table[index].value;
}

void display() {
    printf("Hash Table:\n");
    for (int i = 0; i < SIZE; i++)
        if (table[i].key != -1)
            printf("Key: %d, Value: %d\n", table[i].key, table[i].value);
}

int main() {
    initializeTable();
    int choice, key, value;
    do {
        printf("\n1. Insert\n2. Search\n3. Display\n4. Exit\nEnter choice: ");
        scanf("%d", &choice);
        switch (choice) {
            case 1:
                printf("Enter key and value: ");
                scanf("%d %d", &key, &value);
                insert(key, value);
                break;
            case 2:
                printf("Enter key to search: ");
                scanf("%d", &key);
                value = search(key);
                if (value == -1)
                    printf("Key not found\n");
                else
                    printf("Value: %d\n", value);
                break;
            case 3:
                display();
                break;
        }
    } while (choice != 4);
    return 0;
}