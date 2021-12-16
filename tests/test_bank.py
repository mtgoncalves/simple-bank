from brownie import Bank, accounts


def test_add_account():
    account = accounts[0]
    initial_deposit = 50
    bank = Bank.deploy({"from": account})
    bank.addAccount("Jon", "Snow", initial_deposit)
    balance = bank.showBalance({"from": account})
    assert balance == initial_deposit

def test_deposit():
    account = accounts[0]
    initial_deposit = 50
    bank = Bank.deploy({"from": account})
    bank.addAccount("Jon", "Snow", initial_deposit)

    withdraw_amount = 20
    bank.withdraw(withdraw_amount, {"from": account})
    new_balance = bank.showBalance({"from": account})
    assert new_balance == initial_deposit - withdraw_amount

def test_withdraw():
    account = accounts[0]
    initial_deposit = 50
    bank = Bank.deploy({"from": account})
    bank.addAccount("Jon", "Snow", initial_deposit)

    deposit_amount = 20
    bank.deposit(deposit_amount, {"from": account})
    new_balance = bank.showBalance({"from": account})
    assert new_balance == initial_deposit + deposit_amount
