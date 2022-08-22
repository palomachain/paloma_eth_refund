from ape import accounts, Contract

def main():
    acct = accounts.load("deployer_account")
    contract = Contract("0x")
    receivers = [
        "0x",
        "0x"
        ]
    contract.refund(receivers, sender=acct, value=len(receivers) * 10 ** 17)