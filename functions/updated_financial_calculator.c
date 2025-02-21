//Lila Shearer, Updated Financial Calculator - C
#include <stdio.h>
#include <math.h>

void info(float cost, float income, char type[50]){
    float percent = cost/income*100;
    printf("The amount of money that goes to %s is $%.2f, which is %.1f%% of your income.\n", type, cost, percent);
}

float user_info(char expense[20]){
    float answer;
    printf("How much money do you spend on %s?\n", expense);
    scanf("%f",&answer);
    return answer;
}
float income;
int main(void){
    printf("\nWelcome to Financial Calculator!\nThis program is designed to calculate what percentage of your income that expenses and savings take up, and show how much you have left to spend.\n");
    printf("\nWhen answering questions, please write numbers and do not include the dollar sign (example: 256.78). Thanks!\n");
    printf("\nWhat is your income?\n");
    scanf("%f",&income);
    float savings = income/10;
    float rent = user_info("rent");
    float utilities = user_info("utilities");
    float groceries = user_info("groceries");
    float transportation = user_info("transportation");
    float spending = (income-rent-utilities-groceries-transportation-savings);
    printf("\nHere are your results!\n");
    info(rent, income, "rent");
    info(utilities, income, "utilities");
    info(groceries, income, "groceries");
    info(transportation, income, "transportation");
    info(savings, income, "savings");
    info(spending, income, "spending");
    printf("\nThank you for using Financial Calculator!\nHave a great day!\n");
    return 0;
}