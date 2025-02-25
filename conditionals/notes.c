// Lila Shearer,  Conditional Notes C
#include <stdio.h>
#include <string.h> //<- this is needed to compare strings.


char name[]= "Sarah";
int num;
int main(void){
//10) How do you write an if statement in C?
if(strcmp(name, "Vienna")==0){ //strcmp means string comparison and when the outcome is 0, the strings are the same.
    printf("\nHello Ms. LaRose, welcome to class.\n");
//11) How do you write else statements in C?
}else{
    printf("\nHello %s, welcome to class.\n", name);
}
printf("How many siblings do you have?\n");
scanf("%d", &num); //number needs the & because c is complicated.
//12) How do you write elif/ else if statements in C?

if(num == 0){
    printf("You are an only child :( \n");
} else if(num <= 2){
    printf("You have a small family.\n");
} else if(num <= 5){
    printf("You have a medium-sized family.\n");
} else{
    printf("You have a LOT of siblings.\n");
}
//13) How do you write the 3 logical operators in C?
// && = and
//|| = or
// ! = not
if (num == 7 || num == 13){ 
    printf("That is an unlucky number!");
}else if(num <10 && num >5){
    printf("%d is a large single digit number.", num);
} else if(!(num > 10)){ //<- this is when it is not less than 10. 
    if(num = 12){
        printf("That's a dozen.\n");
    } else{
        printf("That is a big number.\n");
    }
} else{
    printf("You typed in %d.\n", num);
}
    return 0;
} 
