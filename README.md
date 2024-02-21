# Simple Langchain + OpenAI + ChromaDB Embeddings Example

**A Cautionary Note...**
The tutorial I followed, and many others at the time I worked out this project, are based off an older ChromaDB and Langchain APIs. While LangChain wasn't too bad to adapt, Chroma remains incomplete and its documentation is sparse. Another possibly good options is [this one](https://github.com/neo-con/chromadb-tutorial), though it doesn't address LangChain's `RetrievalQA` (which I'm starting to doubt exists with Chroma right now)

It seems chroma is still very new, and it shows. It seems simple enough for learning the basics, but another vector database is probably a better options.

# Getting Started

This project is based off a [tutorial](https://www.gettingstarted.ai/tutorial-chroma-db-best-vector-database-for-langchain-store-embeddings/) by Jeff at gettingstarted.ai about using Chroma. It covers the basics of using Chroma and langchain to query information in PDF documents. _Unfortunately much of the demo is out-of-date (libraries/apis no longer match current), so read it in spirit but know it's not going to help with code very much (eg there's no longer `similarity_search` on collections).

---

**Create a python virtual environment**

```
python3 -m venv virtualenv
source virtualenv/bin/activate
```

**Install dependencies**

...using requirements

```
pip install -r requirements.txt
```

or manually...

```
pip install openai chromadb langchain pypdf tiktoken pandas langchain-community langchain-core
```

**Download sample data (PDF)**

```
mkdir data
curl -o data/document.pdf https://www.gettingstarted.ai/content/files/2023/12/document.pdf
```

**Run ChromaDB in Docker**

```
docker run -p 8000:8000 chromadb/chroma
```

**Add OpenAI API Key:**
```
export OPENAI_API_KEY="..."
```

**Run the script, first to embed**
```
python3 main.py --verbose --embed
```

When embedding, the Chroma collection is deleted and recreated with fresh embeddings from the document.pdf file. Feel free to change the PDF document - I presume any standard PDF text document should work.


**Query**

```
python3 main.py --verbose --query "What is a thinking machine?"
```

