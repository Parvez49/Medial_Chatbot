from pinecone import Pinecone, ServerlessSpec
from langchain_pinecone import PineconeVectorStore
from dotenv import load_dotenv
import os 

from src.helper import load_pdf_file, text_split, download_hugging_face_embeddings


load_dotenv()
PINECONE_API_KEY=os.environ.get('PINECONE_API_KEY')
OPENAI_API_KEY=os.environ.get('OPENAI_API_KEY')

data = load_pdf_file(path='data/')
text_chunks = text_split(data)
embeddings = download_hugging_face_embeddings()

pc = Pinecone(api_key=PINECONE_API_KEY)
index_name = "medical-bot"
pc.create_index(

    name=index_name,

    dimension=384, 

    metric="cosine",

    spec=ServerlessSpec(

        cloud="aws",

        region="us-east-1"

    ) 

)

docsearch = PineconeVectorStore.from_documents(
    documents=text_chunks,
    index_name=index_name,
    embedding=embeddings,
)

### Already stored in database
docsearch = PineconeVectorStore.from_documents(
    documents=text_chunks,
    index_name=index_name,
    embedding=embeddings,
)