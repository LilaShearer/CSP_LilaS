//Lila Shearer, Expressions Practice C

#include <stdio.h>
#include <math.h>
int one = 7-24/8*4+6;
int two = 18/3-7+2*5;
int three = 6*4/12+72/8-9;
int four = (17-6/2)+4*3;
int five = -2*(1*4-2/2)+(6+2-3);
int six = -1*((3-4*7)/5)-2*24/6;

int main(void){
    printf("%d\n %d\n %d\n %d\n %d\n %d\n", one, two, three, four, five, six);
     double x = 5.0, y = 5.0;

    // Storing the answer in sevenone.
    float sevenone = pow(5, 5);
  
    // Storing the answer in seventwo.
    float seventwo = pow(2, 2);
    printf("(3*%f/15)-(5-2%f)", sevenone, seventwo);

    // Storing the answer in eightone.
    float eightone = pow(1, 4);
    
    // Storing the answer in eightwo.
    float eighttwo = pow(2, 2);

    // Storing the answer in eightthree.
    float eightthree = pow(3, 3);
   
    // Storing the answer in eightfour.
    float eightfour = pow(2, 5);
    printf("(%f*%f+%f)-%f/4", eightone, eighttwo, eightthree,eightfour);


    // Storing the answer in nineone.
    float nineone = pow(22/2-2*5, 2);

    // Storing the answer in ninetwo.
    float ninetwo = pow(4-6/6, 2);
    printf("%f+%f", nineone, ninetwo);
    return 0;
}