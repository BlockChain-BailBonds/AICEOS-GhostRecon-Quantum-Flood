
from web3 import Web3
import json

PROVIDER_URL = "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID"
web3 = Web3(Web3.HTTPProvider(PROVIDER_URL))

TOKEN_CONTRACT_ADDRESS = Web3.to_checksum_address("0xYour918TokenAddress")

ERC20_ABI = json.loads('[{"constant":true,"inputs":[{"name":"_owner","type":"address"}],"name":"balanceOf","outputs":[{"name":"balance","type":"uint256"}],"type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"name":"","type":"uint8"}],"type":"function"}]')

def check_token_access(wallet_address, minimum_918_required=1):
    try:
        contract = web3.eth.contract(address=TOKEN_CONTRACT_ADDRESS, abi=ERC20_ABI)
        balance = contract.functions.balanceOf(wallet_address).call()
        decimals = contract.functions.decimals().call()
        adjusted_balance = balance / (10 ** decimals)
        if adjusted_balance >= minimum_918_required:
            print(f"[918 TOKEN CHECK] Access granted. Balance: {adjusted_balance} 918")
            return True
        else:
            print(f"[918 TOKEN CHECK] Access denied. Balance too low: {adjusted_balance} 918")
            return False
    except Exception as e:
        print(f"[918 TOKEN CHECK] Error verifying balance: {e}")
        return False
