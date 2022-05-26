from brownie import network, AdvancedCollectible
from scripts.helpful_scripts import get_breed, get_account, OPENSEA_FORMAT

dog_metadata_dic = {
    "PUG": "ipfs://Qmd9MCGtdVz2miNumBHDbvj8bigSgTwnr4SbyH6DNnpWdt?filename=0-PUG.json",
    "SHIBA": "ipfs://QmdryoExpgEQQQgJPoruwGJyZmz6SqV4FRTX1i73CT3iXn?filename=1-SHIBA_INU.json",
    "BERNARD": "ipfs://QmbBnUjyHHN7Ytq9xDsYF9sucZdDJLRkWz7vnZfrjMXMxs?filename=2-ST_BERNARD.json",
}


def main():
    print(f"Working on {network.show_active()}")
    advancedCollectible = AdvancedCollectible[-1]
    tokenCounter = advancedCollectible.tokenCounter()
    print(f"You have {tokenCounter} tokenIds.")
    for token_id in range(tokenCounter):
        breed = get_breed(advancedCollectible.tokenIdToBreed(token_id))

        if not advancedCollectible.tokenURI(token_id).startswith("https://"):
            print(f"Setting TokenURI of {token_id}")
            setTokenURI(token_id, advancedCollectible, dog_metadata_dic[breed])


def setTokenURI(token_id, nft_contract, tokenURI):
    account = get_account()
    tx = nft_contract.setTokenURI(token_id, tokenURI, {"from": account})
    tx.wait(1)
    print(
        f"Awesome! You can view your NFT at {OPENSEA_FORMAT.format(nft_contract.address,token_id)}"
    )
    print("Please wait for 20 minutes and then press refresh!")
