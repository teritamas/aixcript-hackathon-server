from os import environ

from dotenv import load_dotenv

load_dotenv(verbose=True)

cred_path = environ.get("CRED_PATH", "")
if cred_path == "":
    print(f"CRED_PATH is required. {cred_path=}")
    exit()

google_cloud_storage_bucket_name = environ.get("GOOGLE_CLOUD_STORAGE_BUCKET", "")

# OpenAIのAPIキー
openai_api_key = environ.get("OPENAI_API_KEY", "")

# メタマスクの秘密鍵
system_wallet_private_key_path = environ.get("SYSTEM_WALLET_PRIVATE_KEY_PATH", "")
# Provider Network
provider_network = environ.get("PROVIDER_NETWORK", "")
# 払い戻し可能なトークンのコントラクトアドレス
reversible_ft_contract_address = environ.get("REVERSIBLE_FT_CONTRACT_ADDRESS", "")
