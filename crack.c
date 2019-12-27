#include <cs50.h>
#include <stdio.h>
#include <crypt.h>
#include <string.h>

int main(int argc, string argv[])
{
  int i,j,k,l,m=0,p=0,q=0;
  char salt[20]="";
  char text[20]="";
  char text2[20]="";
  string hash2="";
  // Initializing the variables
 // We check for arguements     
  if (argc!=2){
      printf("Usage: ./crack hash\n");
      exit(1);
  }
  // Now we get the salt
   string hash = argv[1];
   for (i=0;i<2;i++){
       salt[i] = hash[i];
   }
 // Now we start brute forcing
 //First we store the respective ascii numbers in an array
 //a-z and A-Z
 int n[60]={32,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90};
//For Loop
//Here we loop from "    a" -"ZZZZZ"
//(53^4*52) Combinations
//..
for(i=0;i<53;i++){
    text[0]=n[i];
    //..
     for(j=0;j<53;j++){
         text[1]=n[j];
         //..
         for(k=0;k<53;k++){
             text[2]=n[k];
             //..
             for(l=0;l<53;l++){
                 text[3]=n[l];
                 //..
                  for (m=1;m<53;m++){
                       text[4]=n[m];
                        ++p;
                      //We now inverse the string and cut the ' ' char from it
                      for(q=0;q<5;q++){
                            if (text[4-q]!=32){
                            text2[q]=text[4-q];
                        }
                     }    
                   // End of reverse 
                   // Now we hash the text
                   // and compare it with the previou hash
                            hash2="";
                            hash2=crypt(text2,salt);
                            if (strcmp(hash2,hash)==0){
                                printf("%s\n",text2);
                                exit(0);
                            }  
                  }
              }
         }
     }
}
    printf("\nstring=%s, string2=%s, p=%d\n",text,text2,p);
    
}
