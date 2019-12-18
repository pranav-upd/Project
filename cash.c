#include <stdio.h>
#include <cs50.h>
#include <math.h>
int main(void)
{   int cents,quarters,dimes,nickels,pennies,coins; 
    float change = get_float("Change:");
 while (change<0){
     change = get_float("Change:");
 }
 cents = round(change*100);
 quarters = cents/25;
 cents = cents - (quarters*25);
 dimes = cents/10;
 cents = cents - (dimes*10);
 nickels = cents/5;
 cents = cents - (nickels*5);
 pennies = cents;
 coins = quarters + dimes + nickels + pennies;
 printf("%d\n",coins);
}
 
  
