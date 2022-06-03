# https://replit.com/@VincentEdwards1/boilerplate-budget-app

# This is a project from freeCodeCamp.org. 
# The Category class is able to instantiate objects based on different budget categories like 
# food, clothing, and entertainment. When objects are created, they are passed in the name of the category. 
# The class has an instance variable called ledger that is a list. 
# The class also contains the methods deposit, withdraw, get_balance, transfer, check_funds, and a specific __repr__ . 
# The create_spend_chart function takes a list of categories as an argument. 
# It returns a string that is a bar chart.

class Category:
    def __init__(self, name: str):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description: str = ''):
        '''Given an amount and description, deposit money into the budget category and add an entry to the ledger.'''
        self.ledger.append({'amount': amount, 'description': description})

    def withdraw(self, amount, description: str = '') -> bool:
        '''Given an amount and description, withdraw money from the budget category and add an entry to the ledger. Return True if there were sufficient funds and the withdraw took place, and False otherwise.'''
        if not self.check_funds(amount):
            return False
        self.ledger.append({'amount': -amount, 'description': description})
        return True

    def get_balance(self) -> float:
        '''Return the current balance of the budget category based on the deposits and withdrawals that have occurred.'''
        balance = 0.0
        for entry in self.ledger:
            balance += entry['amount']
        return balance

    def get_amount_spent(self) -> float:
        '''Return the current amount spent in the buget category based on the withdrawals that have occured'''
        spent = 0.0
        for entry in self.ledger:
            if entry['amount'] < 0:
                spent -= entry['amount']
        return spent
    
    def transfer(self, amount, destination) -> bool:
        '''Given an amount and another budget category, withdrawl the amount from the source category and deposit it in the destination category. Return True if the transfer took place, and False otherwise'''
        if not self.check_funds(amount):
            return False
        self.withdraw(amount, f'Transfer to {destination.name}')
        destination.deposit(amount, f'Transfer from {self.name}')
        return True

    def check_funds(self, amount) -> bool:
        '''Given an amount, return False if the amount is greater than the balance of the budget category and return True otherwise'''
        return amount <= self.get_balance()

    def __str__(self):
        result = self.name.center(30, '*') + '\n'
        for entry in self.ledger:
            if len(entry['description']) > 23:
                result += entry['description'][:23]
            else:
                result += entry['description'].ljust(23)
            amount = float(entry['amount'])
            am_str = f"{amount:.2f}"
            if len(am_str) > 7:
                am_str = f"{amount:.0f}"
            if len(am_str) > 7:
                amount = f"{amount:.2}"
            if len(am_str) > 7:
                amount = f"{amount:.1}"
            result += am_str.rjust(7) + '\n'
        result += f'Total: {self.get_balance():.2f}'
        return result


def create_spend_chart(categories: list[Category]) -> str:
    '''Given a list of categories as an argument, it returns a string that is a bar chart showing the percentage spent in each budget category passed into the function.'''
    amounts_spent = [cat.get_amount_spent() for cat in categories]
    total_spent = sum(amounts_spent)
    percents_spent = [round(a/total_spent*100) for a in amounts_spent]
    
    chart = 'Percentage spent by category\n'
    for n in range(100, -10, -10):
        chart += f"{str(n).rjust(3)}|{str.join('', [(' o ' if per >= n else '   ') for per in percents_spent])} \n"
    chart += ' ' * 4 + '-' * (3 * len(categories) + 1) + '\n'
    for i in range(max([len(cat.name) for cat in categories])):
        chart += f"    {str.join('', [(f' {cat.name[i]} ' if i < len(cat.name) else '   ') for cat in categories])} \n"
    chart = chart[:-1]

    return chart


if __name__ == "__main__":
    food = Category("Food")
    food.deposit(1000, "initial deposit")
    food.withdraw(10.15, "groceries")
    food.withdraw(15.89, "restaurant and more food for dessert")
    print(food.get_balance())
    clothing = Category("Clothing")
    food.transfer(50, clothing)
    clothing.withdraw(25.55)
    clothing.withdraw(100)
    auto = Category("Auto")
    auto.deposit(1000, "initial deposit")
    auto.withdraw(15)

    print(food)
    print(clothing)

    print(create_spend_chart([food, clothing, auto]))
