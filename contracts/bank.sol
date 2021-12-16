// SPDX-License-Identifier: MIT
pragma solidity >=0.6.0 <0.9.0;

contract Bank {
    address owner;
    mapping(address => Account) public accounts;

    struct Account {
        address _address;
        string _firstName;
        string _lastName;
        uint256 _balance;
    }

    constructor() public {
        owner = msg.sender;
    }

    function withdraw(uint256 amount) public {
        require(
            accounts[msg.sender]._address != address(0x0),
            "Your account does not exist. Please contact the bank owner to create your account."
        );
        require(
            amount <= accounts[msg.sender]._balance,
            "You do not have enough funds to withdraw."
        );
        accounts[msg.sender]._balance -= amount;
    }

    function deposit(uint256 amount) public {
        require(
            accounts[msg.sender]._address != address(0x0),
            "Your account does not exist. Please contact the bank owner to create your account."
        );
        accounts[msg.sender]._balance += amount;
    }

    function showBalance() public view returns (uint256) {
        return accounts[msg.sender]._balance;
    }

    modifier onlyOwner() {
        require(msg.sender == owner);
        _;
    }

    function addAccount(
        string memory _firstName,
        string memory _lastName,
        uint256 _initialBalance
    ) public onlyOwner {
        require(
            _initialBalance > 0,
            "Initial balance must be greater than zero."
        );
        require(
            accounts[msg.sender]._address == address(0x0),
            "Account already exists!"
        );
        address _address = msg.sender;
        accounts[_address] = Account(
            _address,
            _firstName,
            _lastName,
            _initialBalance
        );
    }
}
