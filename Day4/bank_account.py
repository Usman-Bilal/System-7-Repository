"""
Task 4: Bank Account System using OOP
Skills: Basic OOP, modules
"""

from datetime import datetime
import random

class BankAccount:
    """Base Bank Account class"""
    
    account_counter = 1000
    
    def __init__(self, account_holder, initial_balance=0, account_type="Checking"):
        """Initialize bank account"""
        self.account_number = BankAccount.account_counter
        BankAccount.account_counter += 1
        self.account_holder = account_holder
        self._balance = initial_balance
        self.account_type = account_type
        self.transactions = []
        self._add_transaction("Account Created", initial_balance)
    
    def _add_transaction(self, transaction_type, amount):
        """Private method to record transactions"""
        transaction = {
            'date': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'type': transaction_type,
            'amount': amount,
            'balance': self._balance
        }
        self.transactions.append(transaction)
    
    def deposit(self, amount):
        """Deposit money into account"""
        if amount <= 0:
            print("❌ Deposit amount must be positive!")
            return False
        
        self._balance += amount
        self._add_transaction("Deposit", amount)
        print(f"✓ ${amount:.2f} deposited successfully!")
        print(f"New balance: ${self._balance:.2f}")
        return True
    
    def withdraw(self, amount):
        """Withdraw money from account"""
        if amount <= 0:
            print("❌ Withdrawal amount must be positive!")
            return False
        
        if amount > self._balance:
            print("❌ Insufficient funds!")
            return False
        
        self._balance -= amount
        self._add_transaction("Withdrawal", amount)
        print(f"✓ ${amount:.2f} withdrawn successfully!")
        print(f"New balance: ${self._balance:.2f}")
        return True
    
    def get_balance(self):
        """Get current balance"""
        return self._balance
    
    def display_info(self):
        """Display account information"""
        print("\n" + "="*50)
        print("ACCOUNT INFORMATION")
        print("="*50)
        print(f"Account Number: {self.account_number}")
        print(f"Account Holder: {self.account_holder}")
        print(f"Account Type:   {self.account_type}")
        print(f"Balance:        ${self._balance:.2f}")
        print("="*50)
    
    def display_transactions(self, limit=10):
        """Display transaction history"""
        print("\n" + "="*70)
        print("TRANSACTION HISTORY")
        print("="*70)
        
        if not self.transactions:
            print("No transactions yet.")
            return
        
        print(f"{'Date':<20} {'Type':<15} {'Amount':<12} {'Balance':<12}")
        print("-"*70)
        
        for trans in self.transactions[-limit:]:
            print(f"{trans['date']:<20} {trans['type']:<15} "
                  f"${trans['amount']:<11.2f} ${trans['balance']:<11.2f}")
        
        print("="*70)
    
    def __str__(self):
        """String representation"""
        return (f"Account({self.account_number}): {self.account_holder} - "
                f"{self.account_type} - Balance: ${self._balance:.2f}")


class SavingsAccount(BankAccount):
    """Savings account with interest"""
    
    def __init__(self, account_holder, initial_balance=0, interest_rate=0.03):
        super().__init__(account_holder, initial_balance, "Savings")
        self.interest_rate = interest_rate
    
    def add_interest(self):
        """Add interest to account"""
        interest = self._balance * self.interest_rate
        self._balance += interest
        self._add_transaction("Interest", interest)
        print(f"✓ Interest of ${interest:.2f} added!")
        print(f"New balance: ${self._balance:.2f}")
        return interest


class CheckingAccount(BankAccount):
    """Checking account with overdraft"""
    
    def __init__(self, account_holder, initial_balance=0, overdraft_limit=500):
        super().__init__(account_holder, initial_balance, "Checking")
        self.overdraft_limit = overdraft_limit
    
    def withdraw(self, amount):
        """Withdraw with overdraft protection"""
        if amount <= 0:
            print("❌ Withdrawal amount must be positive!")
            return False
        
        available = self._balance + self.overdraft_limit
        
        if amount > available:
            print(f"❌ Exceeds overdraft limit! Available: ${available:.2f}")
            return False
        
        self._balance -= amount
        self._add_transaction("Withdrawal", amount)
        
        if self._balance < 0:
            print(f"⚠️ Account overdrawn by ${abs(self._balance):.2f}")
        
        print(f"✓ ${amount:.2f} withdrawn successfully!")
        print(f"New balance: ${self._balance:.2f}")
        return True


class Bank:
    """Bank management system"""
    
    def __init__(self, name):
        self.name = name
        self.accounts = {}
    
    def create_account(self, account_type, holder_name, initial_balance=0):
        """Create new account"""
        if account_type.lower() == "savings":
            account = SavingsAccount(holder_name, initial_balance)
        elif account_type.lower() == "checking":
            account = CheckingAccount(holder_name, initial_balance)
        else:
            account = BankAccount(holder_name, initial_balance, account_type)
        
        self.accounts[account.account_number] = account
        print(f"\n✓ Account created successfully!")
        print(f"Account Number: {account.account_number}")
        return account.account_number
    
    def get_account(self, account_number):
        """Get account by number"""
        return self.accounts.get(account_number)
    
    def list_accounts(self):
        """List all accounts"""
        print("\n" + "="*70)
        print(f"{self.name} - ALL ACCOUNTS")
        print("="*70)
        
        if not self.accounts:
            print("No accounts found.")
            return
        
        for acc_num, account in self.accounts.items():
            print(account)
        
        print("="*70)
        print(f"Total Accounts: {len(self.accounts)}")
