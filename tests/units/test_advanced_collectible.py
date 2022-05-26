from requests import request
from scripts.helpful_scripts import (
    LOCAL_BLOCKCHAIN_ENVIRONMENTS,
    get_account,
    get_contract,
)
from scripts.advancedCollectible.deployNFT import deploy_and_create
import pytest
from brownie import network, AdvancedCollectible


def test_can_create_simple_collectible():
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip("local testing only!")
    advancedCollectible, creation_tx = deploy_and_create()
    requestId = creation_tx.events["requestCollectible"]["requestId"]
    randomNumber = 777
    get_contract("vrf_coordinator").callBackWithRandomness(
        requestId, randomNumber, advancedCollectible.address, {"from": get_account()}
    )
    assert advancedCollectible.tokenCounter() == 1
    
    assert advancedCollectible.tokenIdToBreed(0) == randomNumber % 3
