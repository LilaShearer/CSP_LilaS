//Lila Shearer, Financial Calculator - C
#include <stdio.h>



int main(void){
    float income;
    float rent;
    float utilities;
    float groceries;
    float transportation;
    printf("Welcome to Financial Calculator!\nThis program is designed to calculate what percentages of your income your expenses, savings, and spending take up.\n");
    printf("What is your monthly income: ");
    scanf("%f",&income);
    printf("What is your monthly expense for rent or mortgage: ");
    scanf("%f",&rent);
    printf("What is your monthly expense for utilities: ");
    scanf("%f",&utilities);
    printf("What is your monthly expense for groceries: ");
    scanf("%f",&groceries);
    printf("What is your monthly expense for transportation:");
    scanf("%f",&transportation);
    printf(" \n");
    printf("Now to calculate your results!\n");
    float spending = (income-rent-utilities-groceries-transportation);
    float spending_percentage = (spending/income*100);
    float savings = (income/10);
    float savings_percentage = (savings/income*100);
    float rent_percentage = (rent/income*100);
    float utilities_percentage = (utilities/income*100);
    float groceries_percentage = (groceries/income*100);
    float transportation_percentage = (transportation/income*100);
    printf(" \n");
    printf("Here are you results!\n");
    printf("The amount of money you spend on your rent or mortages is $%f, which is %f percent of your monthly income.", rent, rent_percentage);
    printf("The amount of money you spend on utilites is $%f, which is %f percent of your monthly income.", utilities, utilities_percentage);
    printf("The amount of money you spend on groceries is $%f, which is %f percent of your monthly income.", groceries, groceries_percentage);
    printf("The amount of money you spend on transportation is $%f, which is %f percent of your monthly income.", transportation, transportation_percentage);
    printf("The amount of money you save is $%f, which is %f percent of your monthly income.", savings, savings_percentage);
    printf("The amount of money you have left to spend is %f, which is %f percent of your monthly income.", spending, spending_percentage);


    return 0;
}