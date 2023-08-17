# fasrapi-langchain-qdrant

## 準備

```sh
$ python --version
Python 3.11.4
$ python -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```

## Qdrant の初期化

`documents` ディレクトリに `sample.pdf` を配置してから、以下のコマンドを実行する。

```sh
$ OPENAI_API_KEY="<your-secret-key>" python refresh.py
```

## サーバーの起動

```sh
$ OPENAI_API_KEY="<your-secret-key>" uvicorn main:app --reload
```

## メッセージの送信

```sh
$ http POST localhost:8000/chat message=pizza
HTTP/1.1 200 OK
content-length: 97
content-type: application/json
date: Thu, 17 Aug 2023 07:08:53 GMT
server: uvicorn

{
    "answer": "Why did the tomato turn red?\n\nBecause it saw the salad dressing!",
    "message": "pizza"
}
```
