from ape import accounts, project

def main():
    acct = accounts.load("deployer_account")
    contract = acct.deploy(project.paloma_eth_refund)
    return contract