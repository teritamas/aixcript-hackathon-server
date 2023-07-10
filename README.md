🎗 2023 年/AI x Cripto Hackathon Top30 Product 選出

- [参考](https://docs.google.com/spreadsheets/d/1ftUsPOCXQOBegM4b-rdlADiXoxt-gGXbAkwy0J50sJA/edit#gid=130562828)

# LIT ART MARKET

LIT ART MARKET のバックエンドサーバーです。本アプリケーションには、下記の URL からアクセスしてください

- [LIT ART MARKET](https://hackathon-sandbox-389814.web.app/mypage)

本アプリケーションについては下記の URL を参照してください

- [Lit Art Market | AKINDO](https://app.akindo.io/communities/1PLX1jmpPUz2nZJL/products/peRXkK3QziGV6AmJ)

## 全体像

LIT ART MARKET は下記のような構成になっています。

![構成図](./docs/arc.png)

上記の全体構成のうち、フロントエンド以外は本リポジトリの担当範囲です。  
フロントエンドは、下記のリポジトリで構築されています。

- [GitHub - teritamas/lit-art-market-frontend](https://github.com/teritamas/lit-art-market-frontend)

### スマートコントラクト

上記の検証環境で利用しているコントラクトは、Aster または Oasys のテストネット上にデプロイされているコントラクトを利用している。

2023/07/11 までは Aster にデプロイされたコントラクトを利用している。

- [Aster(Shibuya)にデプロイされたコントラクトのブロックエクスプローラー](https://blockscout.com/shibuya/address/0xBDC9D28691F277b412c0f86faCd3290e4649413D)

2023/07/11 以降は Oasys にデプロイされたコントラクトを利用している。

- [Oasys(Test hub Layer)にデプロイされたコントラクトのブロックエクスプローラー](https://scan.testnet.oasys.games/address/0x8233d664582749F4c1168169028bBE33E16e3814)

## 概要

本リポジトリで構築される API エンドポイントと、その API の SwaggerDocs は下記の通りです。

- https://aixcript-hackathon-server-ez5q3zuvrq-an.a.run.app/
- [SwaggerDocs](https://aixcript-hackathon-server-ez5q3zuvrq-an.a.run.app/docs)

## Quick Start

### 1. 前準備

はじめに.env.sample を参考に、本プロジェクト直下に.env のファイルを作成する。`REVERSIBLE_FT_CONTRACT_ADDRESS`は、次の手順でコントラクトをデプロイしたのちに記入するので、現時点では空欄にしておく。

本番のネットワークにデプロイする場合は、`PROVIDER_NETWORK`, `REVERSIBLE_FT_CONTRACT_ADDRESS`をデプロイしたネットワークに合わせて変更する。

```sh:.env
# Google CloudのServiceAccountのキーのパス
CRED_PATH=./app/key/service_account.json

# Google Cloud Storageのバケット名
GOOGLE_CLOUD_STORAGE_BUCKET=

# OpenAIのAPIキー
OPENAI_API_KEY=

# Forgeで利用する
# デプロイするアカウントのウォレットのシークレットフレーズ
MNEMONIC=

# 開発用ネットワーク(固定)
FOUNDRY=http://localhost:8545
# Asterのテストネット(固定)
SIBUYA=https://evm.shibuya.astar.network

# スマートコントラクトの環境設定
# オーナーウォレットのプライベートキーのパス
SYSTEM_WALLET_PRIVATE_KEY_PATH=./app/key/dev_private.key

# テストネットの設定
PROVIDER_NETWORK=http://localhost:8545
# コントラクトアドレス
REVERSIBLE_FT_CONTRACT_ADDRESS=

# 本番環境の設定
# PROVIDER_NETWORK=https://evm.shibuya.astar.network
# コントラクトアドレス
# REVERSIBLE_FT_CONTRACT_ADDRESS=
```

### 2. コントラクトのデプロイ

`PROVIDER_NETWORK`にデプロイ先のネットワークを指定し、環境変数を設定する

```sh:
source .env
```

ローカルにテストネットを起動する。

```sh:
anvil -m $MNEMONIC
```

その後別の端末を開き、下記のコマンドでコントラクトをデプロイする。

```sh:
source .env
forge script Deploy --broadcast --rpc-url $FOUNDRY

~~省略~~

Waiting for receipts.
⠉ [00:00:00] [#############################################################################] 1/1 receipts (0.0s)
##### anvil-hardhat
✅ Hash: 0x6b69612773390a2c0cbce75cb891ebd47b449ea46c65eeb91070892fb1cc0e5e
Contract Address: 0x0c2065e8bf691b057f41a193ad0bf04f8c305428
Block: 1
Paid: 0.006154056 ETH (1538514 gas * 4 gwei)

~~省略~~
```

実行後、ログの`Contract Address`に記載しているアドレスを`.env`の`REVERSIBLE_FT_CONTRACT_ADDRESS`に記載する。

#### Aster のテストネットにデプロイする場合

Aster のテストネットである Sibuya にデプロイする場合は、下記のコマンドでデプロイする。

```sh:
forge script Deploy --broadcast --rpc-url $SIBUYA
```

デプロイの際にはテストネットのウォレットに十分な残高があるかを確認する

-

#### Oasys のテストネットにデプロイする場合

Oasys のテストネットでにデプロイする場合は、下記のコマンドでデプロイする。

```sh:
forge script Deploy --broadcast --rpc-url $SIBUYA
```

デプロイの際にはテストネットのウォレットに十分な残高があるかを確認する

#### ABI.json のファイル名更新

デプロイ後、`0x....`に続くコントラクトアドレスが発行される。コントラクトアドレスをコピーし、`app/assets/abi/0x....json`のファイル名を`${コピーしたコントラクトアドレス}.json`に変更する。

現時点では、Oasys のテストネットにデモ用に デプロイされているコントラクトアドレス名を利用している。

### 3. サーバーの起動

はじめに必要ライブラリと Python の環境を用意する

```sh:
poetry install
```

単体テストを実行し、正常に動作することを確認する

```sh:
poetry run pytest .
```

その後、下記のコマンドでサーバーを起動する

```sh:
poetry run uvicorn app.main:app --host 0.0.0.0 --port 8080 --reload
```

実行後、下記の URL にアクセスし、SwaggerDocs が表示されることを確認する

- http://localhost:8080/docs
