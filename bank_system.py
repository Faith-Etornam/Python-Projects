class Account:
    def __init__(self, account_number, account_holder, initial_amount):
        self.account_number = account_number
        self.account_holder = account_holder
        self._balance = initial_amount

    def withdraw(self, amount):
        if self._balance >= amount:
            self._balance -= amount
            return True
        return False
    
    def deposit(self, amount):
        self._balance += amount

    def return_balance(self):
        return self._balance
    
    def display_account_info(self):
        print(f"Account number {self.account_number} in the name of {self.account_holder} has an amount of {self._balance}")

    def __str__(self):
        return f"{self.account_number} and {self.account_holder}"


class Bank:
    def __init__(self):
        self._accounts = []

    def create_account(self, account_holder, initial_deposit):
        account_num = len(self._accounts) + 1
        new_account = Account(account_num, account_holder, initial_deposit)
        self._accounts.append(new_account)
        return new_account

    def get_account(self, account_number):
        for account in self._accounts:
            if account.account_number == account_number:
                return account
        return f"Cannot find account with account number {account_number}"

    def transfer_funds(self, from_acc, to_acc, amount):
        from_account = self.get_account(from_acc)
        to_account = self.get_account(to_acc)

        if not from_account or not to_account:
            return "One or more accounts not found"
        
        if from_account.withdraw(amount):
            to_account.deposit(amount)
            return f"Transferred {amount} from account #{from_acc} to account # {to_acc}"
        else:
            return "Insufficient funds for transfer"


    def list_all_accounts(self):
        for accounts in self._accounts:
            print(accounts)


bank = Bank()

# Create accounts
alice = bank.create_account("Alice Johnson", 1000)
Bob = bank.create_account("Bob Smith", 500)

print("All accounts:")
bank.list_all_accounts()

alice_acc = bank.get_account(1)
bob_acc = bank.get_account(2)


alice_acc.withdraw(200)
bob_acc.deposit(200)

print("\nAfter transactions:")
bank.list_all_accounts()

# Transfer funds
print(bank.transfer_funds(1, 2, 300))

print("\nAfter transfer:")
bank.list_all_accounts()

print(alice.display_account_info())



