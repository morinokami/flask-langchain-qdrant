from flask import Flask
from flask import request
from langchain.callbacks import get_openai_callback
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Qdrant
from qdrant_client import QdrantClient

from const import QDRANT_PATH, COLLECTION_NAME

app = Flask(__name__)


@app.post("/chat")
def chat():
    query = request.json.get("message")
    llm = ChatOpenAI(temperature=0.2)
    qa = build_qa_model(llm)
    with get_openai_callback() as cb:
        answer = qa(query)
        return {
            "answer": answer["result"],
            "cost": cb.total_cost,
        }


def load_qdrant():
    client = QdrantClient(path=QDRANT_PATH)

    try:
        client.get_collection(COLLECTION_NAME)
    except:
        raise Exception("Please run refresh.py first")

    return Qdrant(
        client=client,
        collection_name=COLLECTION_NAME,
        embeddings=OpenAIEmbeddings(),
    )


def build_qa_model(llm):
    qdrant = load_qdrant()
    retriever = qdrant.as_retriever(search_type="similarity", search_kwargs={"k": 10})
    return RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=retriever,
        return_source_documents=True,
        verbose=True,
    )
