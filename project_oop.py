MAX_LINES = 3 #Constant
MAX_BET = 100
MIN_BET = 1

class Deposito:
    
    def deposit(self):
        while True:
            amount = input("What amount of money would you like to deposit? ")
            if amount.isdigit():
                amount = int(amount)
                if amount > 0:
                    break
                else:
                    print("Amount must be greater than zero")
            else:
                print("Please enter a positive number")

        return amount
    
class Obtener:

    def get_amount_of_lines(self):
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
    
class Apuesta:
    def get_bet(self):
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

class Principal(Deposito, Obtener, Apuesta):

    def main(self): 
        balance = self.deposit()
        lines = self.get_amount_of_lines()
        bet = self.get_bet()
        total_bet = bet * lines
        print(f"You are betting {bet}€ on {lines} lines. Total bet is equal to {total_bet}€")

objeto = Principal()
objeto.main()