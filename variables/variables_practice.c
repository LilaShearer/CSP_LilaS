#include <stdio.h>

char name[] = "Lila Shearer";
int number_between_1_and_10 = 3;
int number_between_100_and_1000 = 443;
char breakfast_food[] = "almond butter toast";
char color[] = "dark green";
char school[] = "UCAS";
int year = 2025;
char eye_color[] = "hazil";
int age = 14;
char subject[] = "Seminary";
int main(void){
    printf("Hello my name is %s. The number I chose between 1 and 10 is %d and the number I chose between 100 and 100 is %d. I had %s for breakfast and my favorite color is %s. I go to %s in the year %d and my eyes are %s. I am %d years old and my favorite subject in school is %s.", name, number_between_1_and_10, number_between_100_and_1000, breakfast_food, color, school, year, eye_color, age, subject);
    return 0;
}