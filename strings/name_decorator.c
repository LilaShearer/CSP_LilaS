//Lila Shearer, Name Decorator C
#include <stdio.h>
#include <string.h>
char name[50];
char option[50] = "<><>";
char option_part_two[50] = "<><>";


int main(void){
   printf("Welcome to name decorator!\nThis program is deisgned to take your name and add fun decorations to it.\nWhat is your first name?\n");
   scanf("%s", name);
   strcat(option,name);
   strcat(option,option_part_two);
   printf("%s\n", option);
   
    return 0;
}

