import random

bankaccounts = {}

def generate_account_number():
    while True:
        account_number = random.randint(100, 999)
        if account_number not in bankaccounts:
            return account_number


def create_account(name, initial_balance=0):
    account_number = generate_account_number()

    bankaccounts[account_number] = {
        "name": name,
        "balance": initial_balance
    }

    print(f"Account created successfully!")
    print(f"Account Number: {account_number}")
    print(f"Name: {name}")
    print(f"Balance: ₹{initial_balance}\n")

    return account_number


# Deposit money
def deposit(account_number, amount):
    if account_number in bankaccounts:
        bankaccounts[account_number]["balance"] += amount
        print(f"₹{amount} deposited successfully.")
        print(f"New Balance: ₹{bankaccounts[account_number]['balance']}")
    else:
        print("Account not found.")


# Withdraw money
def withdraw(account_number, amount):
    if account_number not in bankaccounts:
        print("Account not found.")
        return

    if bankaccounts[account_number]["balance"] >= amount:
        bankaccounts[account_number]["balance"] -= amount
        print(f"₹{amount} withdrawn successfully.")
        print(f"Remaining Balance: ₹{bankaccounts[account_number]['balance']}")
    else:
        print("Insufficient balance.")


# Transfer money
def transfer(sender_acc, receiver_acc, amount):
    if sender_acc not in bankaccounts:
        print("Sender account not found.")
        return

    if receiver_acc not in bankaccounts:
        print("Receiver account not found.")
        return

    if bankaccounts[sender_acc]["balance"] < amount:
        print("Insufficient balance.")
        return

    bankaccounts[sender_acc]["balance"] -= amount
    bankaccounts[receiver_acc]["balance"] += amount

    print(
        f"₹{amount} transferred from "
        f"{sender_acc} to {receiver_acc}"
    )


# View balance
def view_balance(account_number):
    if account_number in bankaccounts:
        print(
            f"Balance: ₹{bankaccounts[account_number]['balance']}"
        )
    else:
        print("Account not found.")


# List all accounts
def list_accounts():
    print("\nAll Accounts")
    print("-" * 40)

    for acc_no, details in bankaccounts.items():
        print(
            f"Account No: {acc_no} | "
            f"Name: {details['name']} | "
            f"Balance: ₹{details['balance']}"
        )


# Total money in bank
def total_bank_balance():
    total = sum(
        account["balance"]
        for account in bankaccounts.values()
    )

    print(f"\nTotal Money in Bank: ₹{total}")


def main():
    acc1 = create_account("Uttam KJ", 1500)
    acc2 = create_account("Suraj KJ")
    acc3 = create_account("Dillip KJ", 550000)

    deposit(acc2, 5000)

    withdraw(acc1, 500)

    transfer(acc3, acc1, 10000)

    view_balance(acc1)

    list_accounts()

    total_bank_balance()


if __name__ == "__main__":
    main()