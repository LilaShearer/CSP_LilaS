//Lila Shearer, Strings Notes C
#include <stdio.h>
#include <string.h>
char subject[50];
char name[] = "Victoria";
char sentence[] = "The quick brown fox jumps over the lazy dog.";
int main(void){
    //printf("What class are you in?\n");
   // scanf("%s", subject);
   // fgets(subject, 50, stdin); //when you do fgets it automatically sends it to a new line
    //if you don't know how many characters then do sizeof(subject) instead of writing the number.
    //now to see how to manipulate strings in c. In c, we have very few things you can do to a...
    //...string that has been set.
    //printf("You are in %s, which is the coolest class ever.", subject);
    // in c you can only change a string variable one character at a time. Yikes!
    //in C you always have to use double quotes for strings except for when you are changing them
    //... then you have to use single quotes
    // to change victoria to be Tori, then you have to do name[0] = 'T'; 
    //then you do name[1] = 'o';
    //then name[2] = 'r';
    // then name[3] = 'i';
    //the rest have to be replaced with blank spaces
    
    printf("%lu\n", sizeof(sentence)); //this works always. You need %lu because it's a special data type
    printf("%d\n", strlen(sentence)); // this only works with string.h at the top
    // notice that it gives you 45 and the other gives you 44. One starts counting at 0 while the other...
    //...starts counting at one. 
    //printf("%s", name);

    //time to concatenate! 
    char one[] = "Hello ";
    char two[] = "World!";
    char three[] = "Welcome to my program. ";
    strcat(one, two);
    // to put them together you have to do strcat(one, two)
    // then it will put them together and save the whole thing as variable one. 
    //this means that variable one is now Hello World! instead of just Hello 
    printf("%s\n", one);
    // if you want to put something before Hello World! then you have to do it like this
    //strcat(three, one);
    //they go in the order that you want them to go in. 
    // you can only concatenate TWO THINGS AT A TIME. Because one and two are already concatenated
    //...that means that it already says Hello World
    strcat(three, one);
    printf("%s\n", three);
    return 0;
}