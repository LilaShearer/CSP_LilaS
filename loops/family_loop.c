//Lila Shearer, Family Loop
#include <stdio.h>

int main(void){
    char family_members[][20] = {"Wade", "Ivana", "Paisley", "Max", "Afton", "Jack"};
    int ilength = sizeof(family_members)/sizeof(family_members[0]);
    int i;
    for(i=0;i<ilength;i++){
        printf("%s\n", family_members[i]);
    }
    return 0;
}