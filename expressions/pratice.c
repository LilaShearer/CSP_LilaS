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
    double sevenone = pow(x, y);
    double x2 = 2.0, y2 = 2.0;

    // Storing the answer in seventwo.
    double seventwo = pow(x2, y2);
    printf("(3*%f/15)-(5-2%f)", sevenone, seventwo);

    double x3 = 1.0, y3 = 4;

    // Storing the answer in eightone.
    double eightone = pow(x3, y3);
    double x4 = 2.0, y4 = 2.0;

    // Storing the answer in eightwo.
    double eighttwo = pow(x4, y4);
    double x5 = 3.0, y5 = 3.0;

    // Storing the answer in eightthree.
    double eightthree = pow(x5, y5);
    double x6 = 2.0, y6 = 5.0;

    // Storing the answer in eightfour.
    double eightfour = pow(x6, y6);
    printf("(%f*%f+%f)-%f/4", eightone, eighttwo, eightthree,eightfour);
    double x7 = (22/2-2*5), y7 = 2.0;

    // Storing the answer in nineone.
    double nineone = pow(x7, y7);
    double x8 = (4-6/6), y8 = 2;

    // Storing the answer in ninetwo.
    double ninetwo = pow(x8, y8);
    printf("%f+%f", nineone, ninetwo);
    return 0;
}