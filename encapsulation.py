# 🧪 Code Example: Encapsulation in Action
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner        # public
        self.__balance = balance  # private

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ₹{amount}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrawn ₹{amount}")
        else:
            print("Invalid withdrawal amount.")

    def get_balance(self):
        return self.__balance

    def __str__(self):
        return f"Account owner: {self.owner}, Balance: ₹{self.__balance}"


# Using the class
acc = BankAccount("Vikash", 1000)
print(acc)

acc.deposit(500)
acc.withdraw(200)
print("Current Balance:", acc.get_balance())

# Trying to access private variable directly
print(acc.__balance)  # ❌ Will raise AttributeError


# Python does name mangling for private variables (__balance becomes _BankAccount__balance), so technically:
print(acc._BankAccount__balance)  # ✅ Works, but NOT recommended!
# Encapsulation relies on developer discipline, not strict compiler rules.