# Programming for FinTech: Project 2

Faris Mohamedain

## Project Idea

For my second Programming for FinTech project, I decided to create a Credit Card Payoff Calculator using Python. The purpose of this program is to show how long it could take to pay off a credit card based on the amount owed, the interest rate, and the amount paid each month. My first project focused on building a monthly budget. This project looks more closely at borrowing money and how interest can affect the total cost.

## How the Program Works

The program starts by asking the user for three numbers: their credit card balance, their annual interest rate, and their planned monthly payment. It converts the annual rate into a monthly rate and calculates the interest added to the balance each month. After that, it applies the monthly payment and repeats the process until the balance is paid off. The final payment is adjusted so that the user does not pay more than the remaining amount.

Once the calculation is complete, the program displays the number of months needed to pay off the balance, the total interest paid, and the overall amount paid. I also included a few basic checks. For example, the program tells the user when their payment is not enough to cover the interest. It also catches inputs that are not numbers, instead of immediately crashing.

## Example

If someone has a credit card balance of $1,000 with an 18% annual interest rate and pays $100 every month, the program estimates that it will take 11 months to pay it off. The total interest would be about $91.62, bringing the total amount paid to about $1,091.62. This example shows that the original balance is not always the full amount someone ends up paying.

## Connection to FinTech

This project connects to financial technology because it uses programming to make a common financial calculation easier to understand. Many people use credit cards without knowing how much interest they are paying over time. A tool like this gives users a quick estimate so they can compare their payments and make better decisions about managing debt. It is a simple example of how software can support personal financial planning.

## What I Learned

Working on this project helped me practice using user input, variables, conditional statements, and a while loop in Python. I also got more practice with calculations involving percentages and repeated monthly changes. One important part was making sure that the program could recognize when a monthly payment was too small to reduce the balance.

The calculator is only an estimate. It assumes that the interest rate stays the same, the user makes the same payment each month, and no additional purchases or fees are added. Real credit cards can calculate interest differently, so the results may not exactly match a bank statement. In the future, I could add a feature that compares different monthly payments to show how paying more might save time and money.
