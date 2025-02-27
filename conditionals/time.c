//Lila Shearer, How to do time in c
#include <stdio.h>
#include <time.h>

int main(void){
    //time since January 1, 1970
    time_t seconds;
    seconds = time(NULL);
    //printf("\nIt has been %d seconds since January 1st, 1970.\n", seconds);

    //now to get current time
    time_t rawtime;
    struct tm * timeinfo;
    time(&rawtime);
    timeinfo = localtime(&rawtime);
   // printf("Current time and date is %s.\n", asctime(timeinfo));
   
    //get current hour
    time_t now = time(NULL);
    struct tm * tm_struct = localtime(&now);
    int hour = tm_struct->tm_hour;
    printf("The hour is %d.\n", hour);
   




    //or you can do it like this
    time_t t = time(NULL);
    struct tm *tm = localtime(&t);
    int hour = tm->tm_hour;
    return 0;
}