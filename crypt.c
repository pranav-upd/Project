#include <stdio.h>
#include <crypt.h>
#include <cs50.h>
int main(void){
    string text = get_string("Enter String:");
    string hash = crypt(text,"50");
    printf("%s\n",hash);
}
