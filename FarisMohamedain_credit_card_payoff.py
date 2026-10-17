# Credit Card Payoff Calculator

print("Credit Card Payoff Calculator")
print("-----------------------------")

try:
    balance = float(input("Enter your credit card balance: $"))
    annual_rate = float(input("Enter the annual interest rate (%): "))
    monthly_payment = float(input("Enter your monthly payment: $"))

    if balance <= 0 or annual_rate < 0 or monthly_payment <= 0:
        print("Please enter a positive balance and payment, and a valid interest rate.")
    else:
        monthly_rate = annual_rate / 100 / 12
        first_month_interest = balance * monthly_rate

        if monthly_payment <= first_month_interest:
            print("Your payment is too low to pay off this balance.")
            print("Try a monthly payment higher than the interest added each month.")
        else:
            original_balance = balance
            total_interest = 0
            total_paid = 0
            months = 0

            while balance > 0.005 and months < 1200:
                interest = balance * monthly_rate
                amount_due = balance + interest
                payment = min(monthly_payment, amount_due)
                balance = amount_due - payment
                total_interest += interest
                total_paid += payment
                months += 1

            print("\nPayoff Summary")
            print("--------------")
            print(f"Starting Balance: ${original_balance:.2f}")
            print(f"Monthly Payment: ${monthly_payment:.2f}")
            print(f"Time to Pay Off: {months} months")
            print(f"Total Interest: ${total_interest:.2f}")
            print(f"Total Amount Paid: ${total_paid:.2f}")

            if months >= 1200 and balance > 0.005:
                print("Note: The balance was not fully paid within 100 years.")
            elif total_interest > original_balance / 2:
                print("Interest adds a significant amount to your total cost.")
            else:
                print("Making steady payments helps you pay down your balance.")
except ValueError:
    print("Please enter numbers only.")
