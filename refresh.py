import os
import shutil

from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Qdrant
from pypdf import PdfReader

QDRANT_PATH = "./qdrant_data"
COLLECTION_NAME = "my_collection"
SAMPLE_PDF_PATH = "./documents/sample.pdf"


def split(text: str):
    splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(
        model_name="gpt-3.5-turbo",
        chunk_size=250,
        chunk_overlap=0,
    )
    return splitter.split_text(text)


def extract_text(pdf_path: str):
    reader = PdfReader(pdf_path)
    return "\n\n".join([page.extract_text() for page in reader.pages])


def main():
    if os.path.exists(QDRANT_PATH):
        shutil.rmtree(QDRANT_PATH)

    text = extract_text(SAMPLE_PDF_PATH)
    split_text = split(text)
    if text:
        Qdrant.from_texts(
            split_text,
            OpenAIEmbeddings(),
            path=QDRANT_PATH,
            collection_name=COLLECTION_NAME,
        )
        print("Text added to Qdrant")


if __name__ == "__main__":
    main()
