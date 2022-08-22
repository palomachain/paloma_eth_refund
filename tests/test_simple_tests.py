import ape

def test_init(paloma_eth_refund, owner, accounts):
    bal2 = accounts[2].balance
    paloma_eth_refund.refund([accounts[1], accounts[2], accounts[3]], sender=owner, value=5 * 10 ** 17)
    assert accounts[2].balance == bal2 + 10 ** 17
    