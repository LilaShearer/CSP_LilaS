//Lila Shearer, Updated Hello World C
#include <stdio.h>


void due(char assignment[50], char day[20]){
    printf("The %s assignment is due %s\n", assignment, day);

}

int main(void){
    due("Functions notes", "Today");
    due("Hello Word Update", "Tomorrow" );
    due("Essay", "Wednesday");
}