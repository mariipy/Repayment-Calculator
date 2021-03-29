'''
Repayments Calculator
Edit this menu to ask the user to choose 
'''
def display_title_bar():
    # Display a title bar
    print("\t***  Please select an option ***")

def get_user_choice():
    # List options to user
    print("[1] Calculate Minimum Repayment Plan")
    print("[2] Calculate Overpayment Plan")
    print("[q] Quit")
    return input("Please select an option: ")

# Your functions here
# Set choice to be empty and display title
choice = ''
display_title_bar()
# Create a while loop around the users choices
while choice != 'q':
    choice = get_user_choice()
    display_title_bar()
    if choice == '1':
        print("You chose 1") 
        balance = int(input('Enter credit card balance:'))
        rate= float (input('Enter credit card interest rate:'))

        month=1
        

        annual_apr = (balance / 100) * rate
        monthly_apr= annual_apr /12
        min_repayment = balance / 100 
        total_month = min_repayment + monthly_apr
        print("month: " + str(month) + " balance on the account is £ "  +str(balance) + " minimal repayment is £", str(total_month))
        while balance >= 10:
            balance= balance - min_repayment
            new_rate= (balance/100) *rate //12
            month_balance= new_rate + min_repayment
            month= month+1  
            if balance <= 10:
                break
            else: 
                print("month: " + str(month) + " balance on the account is £ "  +str(balance) + " minimum repayment is £", str(month_balance))
            
    if choice == '2':
        print("You chose 2")
        balance = int(input('Enter credit card balance:'))
        rate= float (input('Enter credit card interest rate:'))
        month_payment= int(input("Enter fix payment: "))

        annual_apr = (balance / 100) * rate
        monthly_apr= annual_apr /12
        repayment = month_payment - monthly_apr 
        month=1
        print("month: " + str(month) + " balance on the account is £ "  +str(balance) + " payment is £", str(repayment))

        while balance >= 10:
            balance= balance - repayment
            month= month +1
            if balance <=10:
                    break  
            else:
                print("month: " + str(month) + " balance on the account is £ "  +str(balance) + " payment is £", str(repayment))
if choice == 'q':
    print("You chose q, bye")
else:
    print("Try again")
