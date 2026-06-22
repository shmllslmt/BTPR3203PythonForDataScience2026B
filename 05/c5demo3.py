class BankAccount:
    def __init__(self, balance=0):
        self._balance = balance
        self.__transaction_history = []

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            self.__log_transaction(("deposit", amount))
            print(f"Deposited {amount}. New balance is {self._balance}.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
            self.__log_transaction(("withdraw", amount))
            print(f"Withdrew {amount}. New balance is {self._balance}.")
        else:
            print("Withdrawal amount must be positive and less than or equal to the current balance.")

    def get_balance(self):
        return self._balance

    def get_transaction_history(self):
        return self.__transaction_history

    def __log_transaction(self, transaction):
        self.__transaction_history.append(transaction)

if __name__ == "__main__":
    account = BankAccount(100)
    account.deposit(50)
    account.withdraw(30)
    print("Current balance:", account.get_balance())
    print("Transaction history:", account.get_transaction_history())

