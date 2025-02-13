//Lila Shearer, Silly Sentences C

#include <stdio.h>
//variables for the user input words, minimum of 3 
char description_of_something[50];
char action_word[50];
char noun[50];
char location[50];
char time_of_day[50];
char famous_person[50];
char name_of_town[50];
int main(void){
    //welcome the user (print statement)
    printf("\nWelcome to silly sentence generator!\nThe purpose of this program is to create a silly sentence using words that you, the user, provides.\nYou don't get to see the sentence until after you have provided words, making it a fun suprise.\n");
    //ask user for words (print statement with a question scanf to set to variable ) In c you need to tell the user that they cna only type 1 word
    printf("\nWhen answering questions for this program, please provide one word answers only.\n");
    printf("\nPlease provide a one-word description of something (ex: yellow, shiny, rough).\n");
    scanf("%s", description_of_something);
    printf("\nAlright. Now please provide a one-word action (ex: running, jumping, swimming).\n");
    scanf("%s", action_word);
    printf("\nSweet. Now please provide a noun (a person, place, or thing).\n");
    scanf("%s", noun);
    printf("\nAwesome. Now please provide a one-word place (ex: library, school, jail). Please don't include the word 'the'.\n");
    scanf("%s", location);
    printf("\nOk. Now please provide a time of day (ex: noon, afternoon, midnight)\n");
    scanf("%s", time_of_day);
    printf("\nGood choice! Now please provide the last name of a famous person (ex: Washington, Jefferson, Hamilton).\n");
    scanf("%s", famous_person);
    printf("\nSounds good. Now please provide a one-word name of a town (ex: Lehi, Seattle, Chicago).\n");
    scanf("%s", name_of_town);
    printf("\nYour silly sentence is complete! Here it is:\n");
    printf("\nMy %s bike is my most prized possesion. The story of how I got it is a long one, but I'm sure you'd love to hear the tale. I was %s down the street with my %s. I was heading to %s because that's where I go every %s. As I turned the corner, I stopped dead in my tracks. %s! In %s?! They stopped and looked at me. 'Do you know where the %s is?' They asked. I nodded, so shocked I was barely able to speak. 'That's where I'm headed too!' I announced. Together we walked to the %s and we became friends. Soon, %s had to leave to go attend some important meetings. As a parting gift, they gave me my bike. That is the story of how I got my %s bike.", description_of_something, action_word, noun, location, time_of_day, famous_person, name_of_town, location, location, famous_person, description_of_something);
    
    //after scanning and getting all words, print a statement that puts them into a story. Insert the variables. You have to do f string. "%s"
    //instructions actually mean one print statement, not one sentence. 
    return 0;
}