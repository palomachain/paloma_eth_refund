import ape
from ape.api import Address

def test_init(paloma_eth_refund, owner, accounts):
    acc0 = Address("0x39Ce025916b6141A2218dC76e1a3fCb5a0E0ecEe")
    acc1 = Address("0x867CEc2D57436B466A976ECd73a40A17Bf90239B")
    acc2 = Address("0x36364d61FD017BE1E4f897aB8270880CAc52d95D")

    paloma_eth_refund.refund([acc0, acc1, acc2], [10 ** 16, 10 ** 17, 10 ** 18], sender=owner, value=111 * 10 ** 16)
    assert acc0.balance == 10 ** 16
    assert acc1.balance == 10 ** 17
    assert acc2.balance == 10 ** 18
    