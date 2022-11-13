import time


balance = 100.00
withdrawal = []
deposit = []


def add_balance(b, a):
    balance = b + a
    deposit.append(
        f"Time: {time.strftime('%H:%S')} Deposited: ${format(a, '.2f')}")
    return balance


def reduce_balance(b, r):
    balance = b - r
    withdrawal.append(
        f"Time: {time.strftime('%H:%S')} Withdrew: ${format(r, '.2f')}")
    return balance


def print_statement(sum):
    balance = sum
    if balance == 0:
        return f"Your balance is ${format(balance, '.2f')}"
    elif balance < 0:
        return f"\nYour balance is ${format(balance - 35, '.2f')}, you have withdrawn your account AND you have been charged a $35.00 late fee"
    else:
        return f"Your balance is ${format(balance, '.2f'):>5}"


print("+------------------------------------------------+")
print("|          Welcome to Your Bank Account!         |")
print("+------------------------------------------------+")
print(f"|      Your current balance is ${format(balance, '.2f'):<9}        |")
print("|  Enter 'V' to view your transaction history    |")
print("+------------------------------------------------+")
while balance > 0:

    user_choice = input(
        "\nWould you like to (W)ithdrawal or (D)eposit into your acct?: ").upper()
    if user_choice == 'W':
        reduce_amount = float(input("How much would you like to withdrawal? "))
        balance = reduce_balance(balance, reduce_amount)
        print(print_statement(balance))

    elif user_choice == 'D':
        add_amount = float(input("How much would you like to Deposit? "))
        balance = add_balance(balance, add_amount)
        print(print_statement(balance))

    elif user_choice == 'V':
        print("+-----------------------------------------+")
        for i in deposit:
            if len(i) == 28:
                print(f"| {i} {' ':>10} |")
            elif len(i) == 29:
                print(f"| {i} {' ':>9} |")
            else:
                print(f"| {i} {' ':>8} |")
        for i in withdrawal:
            if len(i) == 27:
                print(f"| {i} {' ':>11} |")
            elif len(i) == 28:
                print(f"| {i} {' ':>10} |")
            else:
                print(f"| {i} {' ':>9} |")
        print("+-----------------------------------------+")

    else:
        print("Sorry, Please try your command entry again")


print("\n    Your final transaction statement: ")
print("+-----------------------------------------+")
for i in deposit:
    if len(i) == 28:
        print(f"| {i} {' ':>10} |")
    elif len(i) == 29:
        print(f"| {i} {' ':>9} |")
    else:
        print(f"| {i} {' ':>8} |")
for i in withdrawal:
    if len(i) == 27:
        print(f"| {i} {' ':>11} |")
    elif len(i) == 28:
        print(f"| {i} {' ':>10} |")
    else:
        print(f"| {i} {' ':>9} |")
print("+-----------------------------------------+")
