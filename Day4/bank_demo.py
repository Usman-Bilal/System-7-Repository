"""
Bank Account System Demo
"""

from bank_account import Bank, SavingsAccount, CheckingAccount

def main():
    print("\n" + "="*60)
    print("BANK ACCOUNT SYSTEM DEMO")
    print("="*60)
    
    # Create bank
    bank = Bank("ABC Bank")
    
    # Create accounts
    print("\n--- Creating Accounts ---")
    acc1 = bank.create_account("Savings", "John Doe", 1000)
    acc2 = bank.create_account("Checking", "Jane Smith", 500)
    acc3 = bank.create_account("Savings", "Bob Johnson", 2000)
    
    # List all accounts
    bank.list_accounts()
    
    # Perform operations on account 1
    print("\n--- Operations on Account 1 ---")
    account1 = bank.get_account(acc1)
    account1.display_info()
    account1.deposit(500)
    account1.withdraw(200)
    account1.get_balance()
    
    # Add interest (Savings account)
    if isinstance(account1, SavingsAccount):
        print("\n--- Adding Interest ---")
        account1.add_interest()
    
    # Display transactions
    account1.display_transactions()
    
    # Operations on account 2 (Checking with overdraft)
    print("\n--- Operations on Account 2 (Checking) ---")
    account2 = bank.get_account(acc2)
    account2.display_info()
    account2.withdraw(800)  # Should use overdraft
    account2.deposit(1000)
    account2.display_transactions()
    
    print("\n" + "="*60)
    print("DEMO COMPLETE")
    print("="*60)

if __name__ == "__main__":
    main()
