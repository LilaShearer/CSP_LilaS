// Lila Shearer, Time of Day C
#include <stdio.h>
#include <time.h>  

int main(void){
    time_t t = time(NULL);
    struct tm *tm = localtime(&t);
    int hour = tm->tm_hour;
    if (hour > 0 && hour < 12){
    printf("Good morning!\n");
    }else if (hour >12 && hour <17){
    printf("Good afternoon!\n");
    }else{
    printf("Good night!\n");
    }
    return 0;
}