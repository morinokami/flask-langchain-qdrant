# fastapi-langchain-qdrant

## 準備

このプロジェクトではパッケージマネージャーとして [Rye](https://rye-up.com/) を使用しています。[Installation](https://rye-up.com/guide/installation/) のページを参考に、まず Rye をインストールしておいてください。

```sh
$ git clone git@github.com:morinokami/fastapi-langchain-qdrant.git
$ cd fastapi-langchain-qdrant
$ rye sync
```

## Qdrant の初期化

`documents` ディレクトリに `sample.pdf` を配置してから、以下のコマンドを実行する。

```sh
$ OPENAI_API_KEY="<your-secret-key>" python refresh.py
```

## サーバーの起動

```sh
$ OPENAI_API_KEY="<your-secret-key>" rye run flask --app main run --reload
```

## メッセージの送信

```sh
$ http POST localhost:5000/chat message=pizza
HTTP/1.1 200 OK
content-length: 97
content-type: application/json
date: Thu, 17 Aug 2023 07:08:53 GMT
server: uvicorn

{
    "answer": "Why did the tomato turn red?\n\nBecause it saw the salad dressing!",
    "cost": 0.0038385000000000003
}
```
