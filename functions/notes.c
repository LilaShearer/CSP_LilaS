//Lila Shearer, Functions Notes C
#include <stdio.h>
//main is a function. C is an older programming language, so it needs that function to be in existence. In C, instead of using def as the key word. You don't have a key word. The starting function starts with int which is a data type. The return statement is giving an integer. In c, indents don't matter. Things just have to be between the curly brackets.




//int num;
//void  add(int numOne, int numTwo){
 //   printf("%d\n", numOne+numTwo);
//}


//int main(void){
//    printf("Please tell me a number:\n");
//    scanf("%d", num);
//    add(num,21);
 //   return 0;
//}

// to do returns you're going to do return numOne+numTwo

//ONLY USE PARAMETERS AND ARGUMENTS WHEN THE INFORMATION IS CHANGING


//int num;
//char name[50], place[50], verb [50];

//const char* word(char type[50]){
//    char choice[50];
//    printf("Please give me a %s:\n", type);
//    scanf("%s", choice);
//    return choice;
//}

void due(char assignment[50], char day[20]){
    printf("The %s assignment is due %s\n", assignment, day);

}

int main(void){
    due("Functions notes", "Today");
    due("Hello Word Update", "Tomorrow" );
    due("Essay", "Wednesday");
}


//char name_input[50];
//const char* name(char name_input[50]){
//    
//    printf("Please give me a name:\n");
//    scanf("%s", name_input);
//    return("Hello, %s!\n",name_input);
//}

//char main(char name[50]){
//    name();
//    printf(name);
//   return 0;
//}