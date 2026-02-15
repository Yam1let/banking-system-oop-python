"""
Banking System - OOP in Python
Author: Yam1let
Date: February 2026
"""

class BankAccount:
    """
    Represents a bank account with basic deposit and withdrawal functionality.
    """

    def __init__(self, holder: str, balance):
        """
        Initialize a bank account.

        :param holder: Name of the account holder
        :param balance: Initial account balance
        """
        if not isinstance(holder, str):
            raise TypeError("holder must be a string")
        if not isinstance(balance, (int, float)):
            raise TypeError("balance must be int or float")

        self.holder = holder
        self.balance = balance

    def deposit(self, amount):
        """
        Deposit money into the account.
        """
        if not isinstance(amount, (int, float)):
            raise TypeError("amount must be int or float")

        if amount <= 0:
            raise ValueError("deposit amount must be positive")

        self.balance += amount

    def withdraw(self, amount):
        """
        Withdraw money from the account.
        """
        if not isinstance(amount, (int, float)):
            raise TypeError("amount must be int or float")

        if amount <= 0:
            raise ValueError("withdrawal amount must be positive")

        if amount > self.balance:
            raise ValueError("insufficient funds")

        self.balance -= amount

    def __repr__(self):
        return f"<Account: {self.holder} | Balance: {self.balance}>"



class Client:
    """
    Represents a client who owns a bank account.
    """

    def __init__(self, name: str, account):
        """
        Initialize a client with an associated BankAccount.
        """
        if not isinstance(name, str):
            raise TypeError("name must be a string")

        if not isinstance(account, BankAccount):
            raise TypeError("account must be a BankAccount instance")

        self.name = name
        self.account = account

    def check_balance(self):
        """
        Return the current balance of the client's account.
        """
        return self.account.balance

    def transfer(self, other_client, amount):
        """
        Transfer money to another client.
        """
        if not isinstance(other_client, Client):
            raise TypeError("recipient must be a Client")

        if not isinstance(amount, (int, float)):
            raise TypeError("amount must be int or float")

        if amount <= 0:
            raise ValueError("transfer amount must be positive")

        self.account.withdraw(amount)
        other_client.account.deposit(amount)



# Example usage
if __name__ == "__main__":

    account1 = BankAccount("Andrea", 15000)
    account2 = BankAccount("Regina", 6500)

    client1 = Client("Andrea", account1)
    client2 = Client("Regina", account2)

    client1.transfer(client2, 2000)

    print(f"{client1.name} balance: {client1.check_balance()}")
    print(f"{client2.name} balance: {client2.check_balance()}")

    print(account1)
    print(account2)


