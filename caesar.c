#include <cs50.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, string argv[])
{
 
 // Declaring variables
  int i,n,m,k,l,j,o;
  char ch;
 
 // We check for the number of arguments.
 // If it`s not 2, then we exit the program
 // exit() is a part of <stdlib.h>  
  if (argc!=2){
        printf("Usage: ./caesar key\n");
        exit(1);
  }
   // Declaring the string in a new variable
   // We now try to find if there are any other characters in the string
   // other than numbers   
    string s = argv[1];
    n = strlen(s);
    //loop    
    for (i=0;i<n;i++){
        m = (int)(s[i]);
        // Here we check if the input string
        // has any character other than
        // 0 - 9
        if ((m<48)||(m>57)){
               printf("Usage: ./caesar key\n");
               exit(1);
         }
        // If it does not, then continue    
       }
        
    //Loop Done. Now we convert string s to int 
    //using function atoi()
    
    k = atoi(s);
    
    //Now we have sucessfully converted the input
    //to integer. Now we have to take the input
    //plaintext from the user
    
    string p = get_string("plaintext:  ");
    
    // Now we cipher the text 
    // by adding the integer in the arguement
    // with all the the characters of the input string
    // we keep rotating the characters from a-z
    
    
    //Now we start by Initializing the variables
    i=0, m=0, n=0, l=0;
    n = strlen(p);
    
    
    //Now we start looping 
    //We check if the input is a character a-z or A-Z
    for (i=0;i<n;i++){
        m = (int)(p[i]);
        o = k%26;
        //Now we check if the input (p[i]) is a character between A-Z        
        if ((m>=65)&&(m<=90)){
        l = (m+o);   
        //If p[i]+k>Z
        //..             
                if (l>90){
                    j = l-90;
                    m = 64+j;
                    o = 0;
                }
         p[i] = (m+o);
             }
        
        //Now we check if the input (p[i]) is a character between a-z
        else if ((m>=97)&&(m<=122)){
            l = (m+o);
            //if p[i]+k>z
            if (l>122){
                    j = l-122;
                    m = 96+j;
                    o = 0;
                 }
         p[i] = (m+o);
          }        
      // if it is not a character from a-z and A-Z
      // then just continue on the loop 
     }
    printf("ciphertext:  %s\n",p);
 }
    



