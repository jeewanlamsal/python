#Create a class BankAccount with private attributes balance and account_number.
#Implement methods deposit() and withdraw() to modify the balance. Ensure that the
#balance cannot be accessed directly from outside the class.

class BankAccount:
    """
    A class to represent a bank account with secure balance management.
    """

    def __init__(self, account_number, initial_balance=0):
        """
        Initialize a BankAccount with an account number and initial balance.

        Parameters:
        account_number (str): The account number.
        initial_balance (float): The initial balance of the account.
        """
        self.__account_number = account_number
        self.__balance = initial_balance

    def deposit(self, amount):
        """
        Deposit a specified amount into the account.

        Parameters:
        amount (float): The amount to deposit.

        Returns:
        str: Confirmation of the deposit.
        """
        if amount > 0:
            self.__balance += amount
            return f"Deposited ${amount:.2f}. New balance: ${self.__balance:.2f}"
        else:
            return "Deposit amount must be positive."

    def withdraw(self, amount):
        """
        Withdraw a specified amount from the account.

        Parameters:
        amount (float): The amount to withdraw.

        Returns:
        str: Confirmation of the withdrawal or an error message if insufficient funds.
        """
        if amount > 0:
            if amount <= self.__balance:
                self.__balance -= amount
                return f"Withdrew ${amount:.2f}. New balance: ${self.__balance:.2f}"
            else:
                return "Insufficient funds."
        else:
            return "Withdrawal amount must be positive."

    def get_balance(self):
        """
        Get the current balance of the account.

        Returns:
        float: The current balance.
        """
        return self.__balance

# Example usage
account = BankAccount("12345678", 500)

# Deposit money
print(account.deposit(200))  # Output: Deposited $200.00. New balance: $700.00

# Withdraw money
print(account.withdraw(100))  # Output: Withdrew $100.00. New balance: $600.00

# Access balance (secure, via method)
print(f"Current balance: ${account.get_balance():.2f}")  # Output: Current balance: $600.00