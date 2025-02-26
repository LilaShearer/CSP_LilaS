//Lila Shearer, Old Enough C
#include <stdio.h>
int age;
int main(void){
    printf("How old are you in years?\n");
    scanf("%d", &age);
    if(age < 5){
        printf("You are not old enough to go to school, get your learner's permit, drive, or vote.\nWhy are you running this program anyway?\nShouldn't you be playing outside or something?\n");
    } else if(age >= 18){
        printf("You are old enough to vote, drive, get your learner's permit, and go to school.\n");
    } else if(age >=16){
        printf("You are old enough to drive. Hopefully you know what you're doing!\n");
    } else if(age>=15){
        printf("You are old enough to get your learner's permit. Exciting!\n");
    } else{
        printf("You are old enough to go to school.\n");
    }


    return 0;
}