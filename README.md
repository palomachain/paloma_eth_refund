# Paloma Eth Refund

## ApeWorx installation

```sh
pipx install eth-ape
ape plugins install infura vyper etherscan
```

## Foundry installation

```sh
curl -L https://foundry.paradigm.xyz | bash
foundryup
```

## Test

```sh
ape test
```

## Deployment

```sh
ape run scripts/deploy.py --network :mainnet:infura
```

## Refund

Edit deployed address and recipient addresses in the `scripts/refund.py` and run following script.

```sh
ape run scripts/refund.py --network :mainnet:infura
