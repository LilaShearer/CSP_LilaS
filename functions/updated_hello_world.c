//Lila Shearer, Updated Hello World C
#include <stdio.h>

const char* name(){
    char input_name[50]; 
    printf("Please tell me a name:\n");
    scanf("%s", input_name);
    return ("Hello, %s!\n", input_name);
}


int main(void){
    printf(name);
    printf(name);
    printf(name);
    printf(name);
    printf(name);
    return 0;
}