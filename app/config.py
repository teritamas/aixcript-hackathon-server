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
