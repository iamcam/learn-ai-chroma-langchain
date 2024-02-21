# From https://www.gettingstarted.ai/tutorial-chroma-db-best-vector-database-for-langchain-store-embeddings/
import argparse
import os
# Ignore unclosed SSL socket warnings - optional in case you get these errors
import warnings

import chromadb
import pandas as pd
from chromadb.utils.embedding_functions import OpenAIEmbeddingFunction
#pip install langchain-community langchain-core
from langchain_community.document_loaders import PyPDFLoader
# pip install langchain-openai openai
from langchain_openai import ChatOpenAI, OpenAIEmbeddings

warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)
warnings.filterwarnings("ignore", category=DeprecationWarning)

## Arg parsing
parser = argparse.ArgumentParser(description='Use ChromaDB to store and query embeddings')
parser.add_argument('--embed', action='store_true', help='Perform embedding', required=False)
parser.add_argument('--query', type=str, help='Perform query', required=False)
parser.add_argument('--verbose', action='store_true', help='Verbose output', required=False)
args = parser.parse_args()

EMBED = args.embed == True
VERBOSE = args.verbose
if VERBOSE:
    print(args)
query = args.query
if query == "":
    print("Please specify a query with the --query argument")
    exit(1)
elif args.query is None:
    query = "What is the Thinking Machine?"



# Create the ChromaDB client - must be running locally (eg, docker)
# By default data stored in Chroma is ephemeral making it easy to prototype scripts, otherwise use chromadb.PersistentClient
# chroma_client = chromadb.Client()
chroma_client = chromadb.PersistentClient()
embedding_function = OpenAIEmbeddingFunction(api_key=os.environ.get('OPENAI_API_KEY'), model_name="text-embedding-3-small")

if EMBED:
    chroma_client.delete_collection(name="lc_chroma_demo") # Delete a collection and all associated embeddings, documents, and metadata. ⚠️ This is destructive and not reversible

collection = chroma_client.get_or_create_collection(
    name='lc_chroma_demo',
    embedding_function=embedding_function,
    # metadata={"hnsw:space": "cosine"} # l2 is the default
)

if EMBED:
    # Load the PDF and split it into pages
    loader = PyPDFLoader('data/document.pdf')
    docs = loader.load_and_split()

    # Convert the pages into a DataFrame
    content = []
    for doc in docs:
        # print(str(doc.page_content))
        content.append(str(doc.page_content))

    docs_df = pd.DataFrame(content, columns=['text'])
    docs_df.text = docs_df.text.astype(str)
    docs_df.index = docs_df.index.astype(str)
    # TODO: Add metadata to the DataFrame
    if VERBOSE:
        print(docs_df.head())


    embeddings = OpenAIEmbeddings()

    # Creates the embeddings (with OpenAI, via the API)
    collection.add(
        ids=docs_df.index.to_list(),
        documents=docs_df.text.to_list()
    )

## Search Locally

results = collection.query(query_texts=[query], n_results=1)
# print(f"collection peek: {collection.peek()}")
formatted_results_simple = "\n\n>>".join(map(str,results['documents'][0]))

for idx, doc in enumerate(results['documents']):
    print(f"\n\nDistance: {results['distances'][idx]}")
    print(f"Document: {doc[idx]}")

