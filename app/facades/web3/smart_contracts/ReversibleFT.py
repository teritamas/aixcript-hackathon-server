from web3 import Web3

from app.facades.web3.account import ContractOwner
from app.facades.web3.smart_contracts.base import BaseContract
from app.utils.logging import logger


class ReversibleFT(BaseContract):
    """トークン発行のコントラクト"""

    def __init__(
        self,
        contract_owner: ContractOwner,
        contract_address: str,
        provider_network_url: str = "https://evm.shibuya.astar.network",
        mock_mode: bool = False,
    ) -> None:
        if mock_mode:  # MockModeの時は初期化しない
            return

        super().__init__(
            contract_owner,
            contract_address,
            f"./app/assets/abi/{contract_address}.json",
            provider_network_url,
        )
        token_name = self.contract.functions.name().call()
        token_symbol = self.contract.functions.symbol().call()
        balance = self.contract.functions.balanceOf(
            Web3.to_checksum_address(self.contract_owner.address)
        ).call()
        logger.info(
            f"Contract Name: {token_name}, Symbol: {token_symbol}, 残高: {balance}"  # NOQA
        )

    def owner(
        self,
    ):
        """コントラクトの所有者を取得"""
        return self.contract.functions.owner().call()

    def name(
        self,
    ):
        """コントラクトの名称を取得"""
        return self.contract.functions.name().call()

    def mint_deposit(self, wallet_address: str):
        self.approve(wallet_address, 1000000)
        tx = self.contract.functions.mintDeposit(
            self.convert_checksum_address(wallet_address)
        ).build_transaction(
            {
                "nonce": self.network.eth.get_transaction_count(
                    self.contract_owner.address,
                ),
                "from": self.contract_owner.address,  # 自身のアドレスを含める
            }
        )
        tx_result = self.execute(tx)
        logger.info(f"{tx_result=}")

    def approve(self, address, amount):
        tx = self.contract.functions.approve(
            self.convert_checksum_address(address), amount
        ).build_transaction(
            {
                "nonce": self.network.eth.get_transaction_count(
                    self.contract_owner.address,
                ),
                "from": self.contract_owner.address,  # 自身のアドレスを含める
            }
        )
        tx_result = self.execute(tx)
        logger.info(f"approveリクエストの結果。 {tx_result=}")

    def brokerage(self, from_address, to_address, amount):
        """売買を行い、トークンの移動をする"""
        logger.info(f"指定したアドレスにトークンを移管します. {from_address=},{to_address=}, {amount=}")

        tx = self.contract.functions.brokerage(
            self.convert_checksum_address(from_address),
            self.convert_checksum_address(to_address),
            amount,
        ).build_transaction(
            {
                "nonce": self.network.eth.get_transaction_count(
                    self.contract_owner.address,
                ),
                "from": self.contract_owner.address,  # 自身のアドレスを含める
            }
        )
        tx_result = self.execute(tx)
        logger.info(f"トークンの移管が完了しました. {tx_result=}")

    def balance_of_address(self, address):
        """ウォレットアドレスが所有しているトークン量を返す"""
        return self.contract.functions.balanceOf(
            self.convert_checksum_address(address)
        ).call()

    def balance_of_deposit(
        self,
    ):
        """供給可能なトークン量を確認する"""
        return self.contract.functions.balanceOfDeposit().call()
