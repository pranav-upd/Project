#include <cs50.h>
#include <stdio.h>

int main(void)
{ 
 int i,j,k;
 float n;   
 prompt:
 printf("Height: ");
 scanf("%f",&n);
 if (n<1){
     goto prompt;
 }
 else if (n>8){
    goto prompt;   
}
 else { 
     for (i=0;i<=n-1;i++){
       for (j=0;j<=(n-i)-2;j++){
               printf(" ");
       }
         for (k=0;k<=i;k++){
             printf("#");
         }
      printf("\n");
     }
               }
               } 

