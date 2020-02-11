#include <stdio.h>
#include <stdlib.h>
typedef struct node {
  int data;
  struct node *next;
}
node;
//Start of program
int main(void)
{
node *data1 = malloc(sizeof(node));
node *start = malloc(sizeof(node));
node *newptr;
start = data1;
//..
for (int i=0; i<10; i++){
if (data1->data!=0){
while(data1->next!=NULL){
 data1 = data1->next;
}
newptr = malloc(sizeof(node));
newptr->data = i+1;
newptr->next = NULL;
data1->next = newptr;
}
if (data1->data==0){
   data1->data = i+1;
   data1->next = NULL;
}
}
data1 = start;
while(data1!=NULL){
 printf("%d\n",data1->data);
 data1 = data1->next;
}
}