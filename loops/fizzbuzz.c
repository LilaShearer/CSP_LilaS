//Lila Shearer, FizzBuzz C
#include <stdio.h>

int main(void){
    int number = 0;
    while (number < 50){
        if (number > 50){
            break;
        }
        else{
            if (number%3 == 0 && number %5 == 0){
                printf("FizzBuzz");
            }
            else if (number%3 == 0){
                printf("Fizz");
            }
            else if (number%5 == 0){
                printf("Buzz");
            }
            else{
                printf("%d", number);
            }
        }
    }
    return 0;
}