#include <stdio.h>
#include <string.h>
#include <strings.h>
int main(void)
{
int n=0;
char word1[10];
char word2[10];
strcpy(word1, "A");
strcpy(word2, "a");
n = strcasecmp(word1, word2);
printf("%d\n",n);
}