# Simple Bank

A smart contract application written using Solidity demonstrating basic bank transactions:

- addAccount (only by owner)
- withdraw
- deposit
- showBalance

Brownie and Infura are used as the development and test framework/tool in this project.  
To deploy to testnet such as Kovan or Rinkeby on Infura, you'll need to provide your wallet's private_key and infura's project_id. Export in your terminal or store into a .env file the following variables and then paste in your private key and project id accordingly.

```shell
export PRIVATE_KEY=0x...
export WEB3_INFURA_PROJECT_ID=...
```

#### Deploy to testnet network

```shell
brownie run scripts/deploy_bank.py --network kovan
```
