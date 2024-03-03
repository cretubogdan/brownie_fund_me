from brownie import network, accounts, config, MockV3Aggregator
from web3 import Web3


LOCAL_BLOCKCHAIN_ENVS = ["development", "ganache-local"]

DECIMALS = 18
STARTING_PRICE = 2000

def deploy_mocks():
    print("The activate network is: {}".format(network.show_active()))
    print("Deploying mocks...")
    if len(MockV3Aggregator) <= 0:
        MockV3Aggregator.deploy(DECIMALS, Web3.to_wei(STARTING_PRICE, "ether"), {"from": get_account()})
    print("Mocks deployed!")

def get_account():
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVS:
        return accounts[0]
    return accounts.add(config["wallets"]["from_key"])
