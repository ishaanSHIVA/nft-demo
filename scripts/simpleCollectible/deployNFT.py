from scripts.helpful_scripts import get_account
from brownie import SimpleCollectible

sample_token_uri = (
    "ipfs://Qmd9MCGtdVz2miNumBHDbvj8bigSgTwnr4SbyH6DNnpWdt?filename=0-PUG.json"
)


def deploy_and_create():
    account = get_account()

    simpleCollectible = SimpleCollectible.deploy({"from": account})

    tx = simpleCollectible.createCollectible(sample_token_uri, {"from": account})
    tx.wait(1)
    # print(simpleCollectible.address, simpleCollectible.tokenCounter())
    OPENSEA_URL = f"https://testnets.opensea.io/assets/{simpleCollectible.address}/{str(simpleCollectible.tokenCounter() - 1)}"
    print(f"View NFT at {OPENSEA_URL}")
    return simpleCollectible


def main():
    deploy_and_create()
