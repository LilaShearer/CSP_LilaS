//Lila Shearer, Variables Notes C
#include <stdio.h>

int age = 15;

char name[] = "Vienna";

float pi = 3.14;

//this in an input
char food[20];
float pi2;

int main(void){
    printf("Hello, I am %s. I am %d years old. I like the number %f.\n", name, age, pi);
    printf("%d\n", age);
    printf("%f\n", pi);
    printf("Welcome, what is your favorite food: \n");
scanf("%s", food);
printf("%s is a great food!", food);
scanf("%f", &pi);
printf("%f is a lot of pi! Good job.");
    return 0;
}


//you have to say how many charaters when its a string of characters
// you need to add an & symbol when doing an input variable thing. 
