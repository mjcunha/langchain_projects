from datetime import datetime, timedelta
from langchain_openai import OpenAIEmbeddings
from langchain.chains.query_constructor.base import AttributeInfo
from langchain.retrievers.self_query.base import SelfQueryRetriever
from langchain_openai import OpenAI
from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores.timescalevector import TimescaleVector
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import CharacterTextSplitter
from typing import Tuple
from dotenv import find_dotenv, load_dotenv
import os


def main():
    print("Hello, World!")
    _ = load_dotenv(find_dotenv())    
    OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]
    OPENAI_ORGANIZATION = os.environ["OPENAI_ORGANIZATION"]
    SERVICE_URL = os.environ["TIMESCALE_SERVICE_URL"]
    print(OPENAI_API_KEY)
    COLLECTION_NAME = "state_of_the_union_test"
    embeddings = OpenAIEmbeddings(
        openai_api_key=OPENAI_API_KEY, openai_organization=OPENAI_ORGANIZATION
    )
    COLLECTION_NAME = "data_rel_admin_mi4u_16"

    # loader = TextLoader("state_of_the_union.txt")
    # documents = loader.load()
    # text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    # docs = text_splitter.split_documents(documents)    
    # print(docs)

    vector_store = TimescaleVector.f

    



if __name__ == "__main__":
    main()