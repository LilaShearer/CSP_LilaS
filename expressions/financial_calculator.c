//Lila Shearer, Financial Calculator - C
#include <stdio.h>



int main(void){
    float income;
    float rent;
    float utilities;
    float groceries;
    float transportation;
    printf("Welcome to Financial Calculator!\nThis program is designed to calculate what percentages of your income that expenses, and savings take up, and show how much you have left to spend.\n");
    printf("What is your monthly income: ");
    scanf("%f",&income);
    printf("What is your monthly expense for rent or mortgage: ");
    scanf("%f",&rent);
    printf("What is your monthly expense for utilities: ");
    scanf("%f",&utilities);
    printf("What is your monthly expense for groceries: ");
    scanf("%f",&groceries);
    printf("What is your monthly expense for transportation: ");
    scanf("%f",&transportation);
    printf(" \n");
    float spending = (income-rent-utilities-groceries-transportation);
    float spending_percentage = (spending/income*100);
    float savings = (income/10);
    float savings_percentage = (savings/income*100);
    float rent_percentage = (rent/income*100);
    float utilities_percentage = (utilities/income*100);
    float groceries_percentage = (groceries/income*100);
    float transportation_percentage = (transportation/income*100);
    printf("Here are you results!\n");
    printf(" \n");
    printf("The amount of money you spend on your rent or mortage is $%.2f, which is %.1f%% of your monthly income.\n", rent, rent_percentage);
    printf("The amount of money you spend on utilites is $%.2f, which is %.1f%% of your monthly income.\n", utilities, utilities_percentage);
    printf("The amount of money you spend on groceries is $%.2f, which is %.1f%% of your monthly income.\n", groceries, groceries_percentage);
    printf("The amount of money you spend on transportation is $%.2f, which is %.1f%% of your monthly income.\n", transportation, transportation_percentage);
    printf("The amount of money you save is $%.2f, which is %.1f%% of your monthly income.\n", savings, savings_percentage);
    printf("The amount of money you have left to spend is $%.2f, which is %.1f%% of your monthly income.\n", spending, spending_percentage);


    return 0;
}