//Lila Shearer, Updated Hello World C
#include <stdio.h>


void greeting(char name[50]){
    printf("Hello, %s!\n", name);

}


const char* question(){
    char answer[50];
    printf("Please type a name\n");
    scanf("%s", answer);
    return answer;
}

int main(char question[50], char answer[50]){
    greeting ();
    greeting ("John");
    greeting ("Lucy");
    greeting ("Rebecca");
    greeting ("Alexander");
    return 0;
}