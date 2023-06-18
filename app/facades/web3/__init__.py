from app import config
from app.facades.web3.account import ContractOwner
from app.facades.web3.smart_contracts.ReversibleFT import ReversibleFT

# 提案用NFT
reversible_ft = ReversibleFT(
    contract_owner=ContractOwner(config.system_wallet_private_key_path),
    provider_network_url=config.provider_network,
    contract_address=config.reversible_ft_contract_address,
)

# print(reversible_ft.owner())
# print(reversible_ft.mint_deposit("0x420E74b449263f3363bB08f8a9237d80b763e046"))
# print(
#     reversible_ft.brokerage(
#         "0x420E74b449263f3363bB08f8a9237d80b763e046",
#         "0xc430E55964427921056157A6372b03D6f78647a8",
#         100,
#     )
# )

# print(reversible_ft.balance_of_address("0x420E74b449263f3363bB08f8a9237d80b763e046"))
print(reversible_ft.balance_of_address("0xb872960EF2cBDecFdC64115E1C77067c16f042FB"))
