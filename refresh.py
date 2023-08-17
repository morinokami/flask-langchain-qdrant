from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams
from langchain.vectorstores import Qdrant
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from pypdf import PdfReader

def split(text: str):
    splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(
        # model_name=,
        chunk_size=250,
        chunk_overlap=0,
    )
    return splitter.split_text(text)

def extract_text(pdf_path: str):
    reader = PdfReader("./documents/sample.pdf")
    return '\n\n'.join([page.extract_text() for page in reader.pages])

def load_qdrant():
    client = QdrantClient(path="./qdrant_data")

    try:
        client.get_collection("my_collection")
    except:
        client.create_collection(
            collection_name="my_collection",
            vectors_config=VectorParams(size=1536, distance=Distance.COSINE),
        )
        print("Collection created")

    return Qdrant(
        client=client,
        collection_name="my_collection",
        embeddings=OpenAIEmbeddings(),
    )

def main():
    text = extract_text("./documents/sample.pdf")
    split_text = split(text)
    if text:
        qdrant = load_qdrant()
        qdrant.add_texts(split_text)
        print("Text added to Qdrant")

if __name__ == "__main__":
    main()
