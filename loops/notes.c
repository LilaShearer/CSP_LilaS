//Lila Shearer, Loops Notes C
#include <stdio.h>
//To select multiple thing at once do control alt and use the up and down arrow keys.

int main(void){
//What is a loop?
    // A loop is a section of code that gets repeated multiple times. 
//What are the two types of loops?
    // While loops
    int start = 0;
    while (start<5){
        printf("Hello, number that is less than five!\n");
        start++;

    }
    // For loops
    int q;
    for(q=0;q<5;q++){
        printf("%d\n", q);
    }
//What is iteration?
    // repeating something with minor changes each time. In the for loop above, q is an example of iteration because it is changing every time.
//What are arrays(lists)? 
    // An array is a variable that holds multiple values. In C we call it an array instead of a list. Who knows why. 
    //Array items all need to be the same data type.
    // In c, a string is just an array of characters.
    int fun_numbers[] = {7, 23, 27};
//How do you make arrays in C?
    // 1) Set the data type first.
    // 2) After naming, then you do brackets telling it how long the array is.
    // 3) array is surrounded by curly brackets {}
    // 4) Commas between each item

// To print one item from an array, do this:
printf("%d\n", fun_numbers[2]); //It starts at 0. This will give the number 27 from fun numbers above.

// To change an item from an array, do this
fun_numbers[2] = 37; //name of the array, index number then what the new value is

printf("%d\n", fun_numbers[2]);

// to get the length of an array then do this:
int size = sizeof(fun_numbers);
//Ever item in the array is taking up four bites of space. Size right now is the length in bites.
int length = sizeof(fun_numbers)/sizeof(fun_numbers[0]); //You are getting the size of one of the items in the array and then dividing that number by the whole amount to get the number of items in the array.
printf("%d\n", length);

//array with strings
//first bracket sets the length of the array
// second sets the length of each string
char fun_words[][20] = {"Honey badger", "whisky", "badminton", "dandelion"};

printf("%s", fun_words[3]);
int ilength = sizeof(fun_words)/sizeof(fun_words[0]);
//How do you make for loops in C?
// Loops in c never require lists.
int x; //set the iterator, keeps track of times through the loop. Use x or i. That is best practice.
//x++ automatically increases by 1. To count by 2, you would do x+=2
for(x=0; x<=10; x++){ // the three pieces of info in the parenthesis are (starting point; ending point; where to start)
    printf("%d\n", x);
}

int i;
for(i=0;i<ilength;i++){
    printf("%s\n", fun_words[i]);
}


//How do you make while loops in C?
int w = 0;
while(w>=0){ //This is the stop point
    printf("%d\n", w);
    w-=10;
}

    return 0;
}