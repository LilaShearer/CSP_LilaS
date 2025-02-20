//Lila Shearer, Updated Hello World C
#include <stdio.h>


void greeting(char answer[50]){
    
    printf("Hello, %s!\n", answer);

}

int main(void){
    printf("Welcome to updated Hello World. This program is designed to say hello to names. You will get the opportunity to insert a name and see other names that are greeted.\n");
    char answer[50];
    printf("Please type a name:\n");
    scanf("%s", answer);
    greeting(answer);
    greeting("Sally");
    greeting("Alexander");
    greeting("Jacob");
    greeting("Zachary");
    return 0;
}