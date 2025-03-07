//Lila Shearer, FizzBuzz C
#include <stdio.h>

int main(void){
    int number = 0;
    while (number < 50){
        if (number > 50){
            break;
        }
        else{
            number+=1;
            if (number%3 == 0 && number %5 == 0){
                printf("FizzBuzz\n");
            }
            else if (number%3 == 0){
                printf("Fizz\n");
            }
            else if (number%5 == 0){
                printf("Buzz\n");
            }
            else{
                printf("%d\n", number);
            }
        }
    }
    return 0;
}