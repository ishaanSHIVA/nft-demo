from brownie import config, network, AdvancedCollectible
from scripts.helpful_scripts import get_account, get_contract, fund_with_link
from web3 import Web3

dog_metadata_dic = {
    "PUG": "ipfs://Qmd9MCGtdVz2miNumBHDbvj8bigSgTwnr4SbyH6DNnpWdt?filename=0-PUG.json",
    "SHIBA": "ipfs://QmdryoExpgEQQQgJPoruwGJyZmz6SqV4FRTX1i73CT3iXn?filename=1-SHIBA_INU.json",
    "BERNARD": "ipfs://QmbBnUjyHHN7Ytq9xDsYF9sucZdDJLRkWz7vnZfrjMXMxs?filename=2-ST_BERNARD.json",
}


def advancedCollectible():
    account = get_account()
    networkSelected = config["networks"][network.show_active()]

    advancedCollectible = AdvancedCollectible[-1]

    fund_with_link(advancedCollectible.address, amount=Web3.toWei(0.1, "ether"))

    creating_tx = advancedCollectible.createCollectible(
        dog_metadata_dic["BERNARD"], {"from": account}
    )
    creating_tx.wait(1)

    print(f"Collectible created!")


def main():
    advancedCollectible()
