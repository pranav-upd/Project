#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
  if (argc!=2){
  printf("Usage: ./recover image\n");
  return 1;
}
 FILE *file = fopen(argv[1], "r");
 if (file==NULL){
     printf("File not found\n");
     return 1;
}
 FILE *infile=NULL;
 unsigned char buffer[512];
 char filename[10];
 int size=0,n=0,fn=0;
 while(fread(buffer,sizeof(buffer),1,file) == 1){
  if (buffer[0]==0xff&&buffer[1]==0xd8&&buffer[2]==0xff&&(buffer[3]>=0xe0&&buffer[3]<=0xef)){
  if (n>0){
   fclose(infile);
  }
  sprintf(filename,"%03d.jpg",fn);
  infile = fopen(filename, "w");
  //..
  if (infile==NULL){
   printf("Error creating files\n");
   return 2;
  }
  //..
  n = n+1;
  fn = fn+1;
  }
  if(n>0){
   fwrite(buffer, sizeof(buffer), 1, infile);
  }
  size = size+1;
 }
 printf("%d\n",size);
 fclose(file);
 fclose(infile);
}
