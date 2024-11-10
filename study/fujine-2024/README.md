# あなたのアプリケーションをレガシーコードにしないための実践Pytest入門 写経

https://2024.pycon.jp/ja/talk/D9BDAQ

## 環境構築

Python 3.12.6 で動かした

```
% python -m venv .venv --upgrade-deps
% source .venv/bin/activate
(.venv) $ pip install -e '.[dev]'
```

完全に再現させたい場合は dev-requirements.txt を参照

## DB接続のあるテストを動かすために

```
% mysql --version
mysql  Ver 8.0.39 for macos14.4 on arm64 (Homebrew)
```

別のターミナルで

```
% docker run --rm --name mysql-db -e MYSQL_ROOT_PASSWORD=my-secret-pw -p 13306:3306 -d mysql:8.0
```

テスト実行するターミナルでは、以下を実行した後に`pytest`を叩く

```
export MYSQL_HOST=127.0.0.1
export MYSQL_PORT=13306
export MYSQL_USER=root
export MYSQL_PASSWORD=my-secret-pw
```
