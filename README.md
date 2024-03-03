# brownie_fund_me
Web3 brownie fund me
brownie networks add Ethereum ganache-local host=http://127.0.0.1:8545 chainid=1337
brownie networks add development mainnet-fork-dev cmd=ganache-cli host=http://127.0.0.1 fork='https://eth-mainnet.g.alchemy.com/v2/O6oMekkdckKlP7FugK4JhVAhWdOvkcgu' accounts=10 mnemonic=brownie port=8545
brownie test --network mainnet-fork-dev
