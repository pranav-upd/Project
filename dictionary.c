// Implements a dictionary's functionality
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <strings.h>
#include <stdbool.h>

#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
}
node;

// Number of buckets in hash table
const unsigned int N = 26;

// Hash table
node *table[N];
node *start[N];
node *newptr;
node *buffer;

// Returns true if word is in dictionary else false
bool check(const char *word)
{
    int a = 0, b = 0;
    a = hash(word);
    while(table[a]!=NULL){
        b = strcasecmp(table[a]->word, word);
        //..
        if (b==0){
            table[a] = start[a];
            return true;
        }
        //..
        table[a] = table[a]->next;
    }
    //..
    table[a] = start[a];
    return false;

}

// Hashes word to a number
unsigned int hash(const char *word)
{
     int c = 0, d = 0;
     if (word[0]>=65 && word[0]<=90)
     {
        c = word[0] - 65;
     }

     if (word[0]>=97 && word[0]<=122)
     {
         c = word[0] - 97;
     }
     return c;
}

// Loads dictionary into memory, returning true if successful else false
bool load(const char *dictionary)
{
    FILE *dict = fopen(dictionary, "r");
    if (dict == NULL){
        return false;
    }
    //..
    for (int i=0; i<26; i++){
    table[i] = malloc(sizeof(node));
    }
    //..
    for (int j=0; j<26; j++){
    start[j] = table[j];
    }
    //..
    int m=0,p=0,t=0,l=0,j=0,u=0;
    char word2[LENGTH + 1];
    while (m != EOF){
        m = fgetc(dict);
        if (m == 10){
        word2[p] = '\0';
        u = u + 1;
        t = hash(word2);
        //..
            if (u>1){
            while(table[t]->next!=NULL){
                table[t] = table[t]->next;
            }
            newptr = malloc(sizeof(node));
            if (newptr==NULL){
                return 1;
            }
            strcpy(newptr->word, word2);
            newptr->next = NULL;
            table[t]->next = newptr;
            }
        else if (u==1){
            strcpy(table[t]->word, word2);
            table[t]->next = NULL;
        }
        //..
        memset(word2,0,sizeof(word2));
        p = 0;
        }
        if (m!=10){
        word2[p] = m;
        p = p + 1;
        }
    }
    for (int n=0; n<26; n++){
        table[n] = start[n];
    }
    fclose(dict);
    return true;
}

// Returns number of words in dictionary if loaded else 0 if not yet loaded
unsigned int size(void)
{
    int k=0;
    //..
    for (int i=0; i<26; i++){
        while(table[i]!=NULL){
        if (table[i]->word[0]!=0){
            k = k + 1;
        }
        table[i] = table[i]->next;
        }
    }
    for (int j=0; j<26; j++){
        table[j] = start[j];
    }
    return k;
}

// Unloads dictionary from memory, returning true if successful else false
bool unload(void)
{
    // TODO
    for (int i=0; i<26; i++){
        //..
        while(table[i]!=NULL){
            buffer = table[i];
            table[i] = table[i]->next;
            free(buffer);
        }
    }
    return true;
}
