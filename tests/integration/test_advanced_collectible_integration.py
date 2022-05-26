from requests import request
from scripts.helpful_scripts import (
    LOCAL_BLOCKCHAIN_ENVIRONMENTS,
    get_account,
    get_contract,
)
from scripts.advancedCollectible.deployNFT import deploy_and_create
import pytest
import time
from brownie import network, AdvancedCollectible


def test_can_create_advanced_collectible_integration():
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip("integration testing!!")
    advancedCollectible, creation_tx = deploy_and_create()
    time.sleep(60)
    assert advancedCollectible.tokenCounter() == 1
