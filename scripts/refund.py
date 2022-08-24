from ape import accounts, Contract

def main():
    acct = accounts.load("deployer_account")
    contract = Contract("0x6CdcF854c4b16e59c89EeE5806E1CDa8f6512BB5")
    receivers = [
        "0x63798ad4eb791a8247bb522bce38062e41f7ce26",
        "0x63f55bc560e981d53e1f5bb3643e3a96d26fc635",
        "0xf95837f321d1647dab446ebb90ea578b39d02efe",
        "0x7b7287710104f4e7f5ff4f6bd2ddd399cab2d099",
        "0xe898fc35d5c3ceb801ad5f365142972eaafe2e9b",
        "0xee9265b42ec8cecd36063b6f029396bde1e4146c",
        "0x11b6c349d67244e2d62d1cb2f8460226b492cceb"
        ]
    contract.refund(receivers, sender=acct, value=len(receivers) * 15 * 10 ** 16)