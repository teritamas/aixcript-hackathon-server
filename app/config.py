from os import environ

from dotenv import load_dotenv

load_dotenv(verbose=True)

cred_path = environ.get("CRED_PATH", "")
if cred_path == "":
    print(f"CRED_PATH is required. {cred_path=}")
    exit()
