MAX_LINES = 3 #Constant
MAX_BET = 100
MIN_BET = 1

def deposit():
    while True:
        amount = input("What amount of money would you like to deposit? ")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than zero")
        else:
            print("Please enter a positive number, not a text or symbol.")

    return amount

def get_amount_of_lines():
    while True:
        lines = input("Enter the number of lines to bet on (between 1 and " + str(MAX_LINES) + ")")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines")
        else:
            print("Please enter a positive number, not a text or symbol.")

    return lines

def get_bet():
    while True:
        amount = input("What amount of money would you like to bet on each line? ")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between {MIN_BET} and {MAX_BET}")
        else:
            print("Please enter a positive number, not a text or symbol.")

    return amount

def main(): 
    amount = deposit()
    lines = get_amount_of_lines()
    bet = get_bet()
    total_bet = bet * lines
    print(f"You are betting {bet}€ on {lines} lines. Total bet is equal to {total_bet}€")

main()