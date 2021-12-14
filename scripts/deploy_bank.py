from brownie import Bank, network, accounts, config


def deploy_bank():
    account = accounts[0]
    bank = Bank.deploy({"from": account})

    first_name, last_name = "Jon", "Snow"
    initial_deposit = 50
    print(f"Creating account for '{first_name} {last_name}' ...")
    transaction = bank.addAccount(first_name, last_name, initial_deposit)
    transaction.wait(1)
    print(f"Account created for '{first_name} {last_name}'!")
    balance = bank.showBalance({"from": account})
    print(f"Current balance is {balance}")

    withdraw_amount = 20
    print(f"Withdrawing {withdraw_amount} ...")
    transaction = bank.withdraw(withdraw_amount, {"from": account})
    transaction.wait(1)
    balance = bank.showBalance({"from": account});
    print(f"Withdrew {withdraw_amount}. Current balance is {balance}.")

    deposit_amount = 70
    print(f"Depositing {deposit_amount} ...")
    transaction = bank.deposit(deposit_amount, {"from": account})
    transaction.wait(1)
    balance = bank.showBalance({"from": account})
    print(f"Deposited {deposit_amount}. Current balance is {balance}.")

def main():
    deploy_bank()
