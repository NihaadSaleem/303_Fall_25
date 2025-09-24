import datetime
import string

# Caesar cipher functions

def encode(input_text, shift):
    alphabet_list = [chr(i) for i in range(ord('a'), ord('z')+1)]
    shift = shift % 26
    result = ''
    for ch in input_text:
        if ('a' <= ch <= 'z') or ('A' <= ch <= 'Z'):
            c = ch.lower()
            pos = ord(c) - ord('a')
            new_pos = (pos + shift) % 26
            new_char = chr(ord('a') + new_pos)
            result += new_char
        else:
            result += ch
    return (alphabet_list, result)

def decode(input_text, shift):
    shift = shift % 26
    result = ''
    for ch in input_text:
        if ('a' <= ch <= 'z') or ('A' <= ch <= 'Z'):
            c = ch.lower()
            pos = ord(c) - ord('a')
            new_pos = (pos - shift) % 26
            new_char = chr(ord('a') + new_pos)
            result += new_char
        else:
            result += ch
    return result

# Banking classes

class BankAccount:
    def __init__(self, name="Rainy", ID="1234", creation_date=None, balance=0):
        if creation_date is None:
            creation_date = datetime.date.today()
        if isinstance(creation_date, datetime.datetime):
            creation_date = creation_date.date()
        if not isinstance(creation_date, datetime.date):
            raise TypeError("creation_date must be datetime.date")
        if creation_date > datetime.date.today():
            raise Exception("Creation date cannot be in the future.")
        self.name = name
        self.ID = ID
        self.creation_date = creation_date
        self.balance = float(balance)

    def deposit(self, amount):
        if amount < 0:
            return self.balance
        self.balance += float(amount)
        return self.balance

    def withdraw(self, amount):
        if amount < 0:
            raise ValueError("Negative withdrawal amounts are not allowed.")
        self.balance -= float(amount)
        return self.balance

    def view_balance(self):
        return self.balance

class SavingsAccount(BankAccount):
    def withdraw(self, amount):
        if amount < 0:
            raise ValueError("Negative withdrawal amounts are not allowed.")
        if amount > self.balance:
            return self.balance
        days_open = (datetime.date.today() - self.creation_date).days
        if days_open < 180:
            return self.balance
        self.balance -= float(amount)
        return self.balance

class CheckingAccount(BankAccount):
    def withdraw(self, amount):
        if amount < 0:
            raise ValueError("Negative withdrawal amounts are not allowed.")
        self.balance -= float(amount)
        if self.balance < 0:
            self.balance -= 30.0
        return self.balance
