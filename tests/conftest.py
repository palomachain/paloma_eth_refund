import pytest

@pytest.fixture(scope="session")
def owner(accounts):
    return accounts[0]

@pytest.fixture(scope="session")
def paloma_eth_refund(owner, project):
    return owner.deploy(project.paloma_eth_refund)