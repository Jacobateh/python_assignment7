"""
Bank Account Simulation

Task:
- Manage simple bank accounts.
- Store accounts in dictionary { "account_number": {"name": str, "balance": float} }
- Deposit, withdraw, transfer between accounts.
- Use *args for batch deposits/withdrawals.
- Use **kwargs for flexible account creation (e.g., overdraft_limit).

// NOT FOR THIS TASK
Future OOP Extension:
- BankAccount class with methods deposit(), withdraw(), transfer().
- Bank class to manage all accounts.
"""

accounts = {}

def create_account(account_number, name, **kwargs):
    """Create an account with optional features like overdraft_limit."""
		if account_number in accounts:
			return f"Account {account_number} already exist"
		accounts[account_number]={
			"name": name,
			"balance": 0.0,
			"overdraft_limit": kwargs.get("overdraft_limit", 0.0)
		}
		return f"Account created for {name} with account number {account_number}."
    pass

def deposit(account_number, *amount):
    """Deposit money into account.
        return "Account not found!" (if account does not exists)
        return Deposited {amount} into {accounts name}'s account. if account exists
    """
	if account_number not in accounts:
		return "Account not found"
	total_deposit = sum(amounts)
	account[account_number]["balance"] += total_deposit
	return f"Deposited {total_deposit} into {accounts[account_number]['name']}'s account"
    pass

def withdraw(account_number, amount):
    """Withdraw money if balance is sufficient. else: insufficient funds"""
	if account_number not in accounts:
		return "Accounts not found"
	acc = accounts[account_number]
	if acc["balance"] + acc ["overdraft_limit"] >= amount:
		acc["balance"] -= amount
		return f"withdrew{amount} from {acc['name']}'s account"
	else:
		returnv"insufficient funds"
    pass

def transfer(from_acc, to_acc, amount):
    """Transfer money between accounts. if funds is sufficient"""

	if from_acc not in accounts or to_acc not in accounts:
		return "one or both accounts not found"
	if from_account["balance"] + from_account["overdraft_limit"] >= amount:
		from_account = accounts[from_acc]
		to_account = accounts[to_acc]
		return  f" Transferred {amount} from {from_account['name']} to {to_account['name']}"
	else:
		return "insufficient funds for transfer"
    pass
