from langchain.document_loaders import PyPDFLoader, DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
# from langchain.embeddings import HuggingFaceEmbeddings
from langchain_huggingface import HuggingFaceEmbeddings


### Extract Data from PDF File
def load_pdf_file(path):
    loader = DirectoryLoader(path,
                            glob="*.pdf",
                            loader_cls=PyPDFLoader)
    
    document = loader.load()
    return document


### Split the data into Text chunks
def text_split(data):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=200, chunk_overlap=True)
    text_chunks = text_splitter.split_documents(data)
    return text_chunks


### Download the Embeddings from Hugging Face
def download_hugging_face_embeddings():
    embeddings = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-l6-v2')
    return embeddings

