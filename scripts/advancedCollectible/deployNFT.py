from scripts.helpful_scripts import get_account, get_contract, fund_with_link
from brownie import AdvancedCollectible, network, config

sample_token_uri = (
    "ipfs://Qmd9MCGtdVz2miNumBHDbvj8bigSgTwnr4SbyH6DNnpWdt?filename=0-PUG.json"
)


def deploy_and_create():
    account = get_account()
    networkSelected = config["networks"][network.show_active()]

    advancedCollectible = AdvancedCollectible.deploy(
        get_contract("vrf_coordinator"),
        get_contract("link_token"),
        networkSelected["keyhash"],
        networkSelected["fee"],
        {"from": account},
        publish_source=networkSelected["verify"],
    )

    fund_with_link(advancedCollectible.address)

    creating_tx = advancedCollectible.createCollectible("None", {"from": account})
    creating_tx.wait(1)

    print(f"New Token has been created!!!")

    return advancedCollectible, creating_tx

    # OPENSEA_URL = f"https://testnets.opensea.io/assets/{simpleCollectible.address}/{str(simpleCollectible.tokenCounter() - 1)}"


def main():
    deploy_and_create()
