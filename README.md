# Simple Langchain + OpenAI + ChromaDB Embeddings Example

**A Cautionary Note...**
The tutorial I followed, and many others at the time I worked out this project, are based off an older ChromaDB and Langchain APIs. While LangChain wasn't too bad to adapt, Chroma remains incomplete and its documentation is sparse.

It seems chroma is still very new, and it shows.

# Begin

This project is based off a [tutorial](https://www.gettingstarted.ai/tutorial-chroma-db-best-vector-database-for-langchain-store-embeddings/) by Jeff at gettingstarted.ai about using Chroma. It covers the basics of using Chroma and langchain to query information in PDF documents. _Unfortunately much of the demo is out-of-date (libraries/apis no longer match current), so read it in spirit but know it's not going to help with code very much (eg there's no longer `similarity_search` on collections).

---

Get your environment going:

```
python3 -m venv virtualenv
source virtualenv/bin/activate
```

Install dependencies:

```
pip install openai chromadb langchain pypdf tiktoken pandas langchain-community langchain-core
```

Download sample data (PDF)

```
mkdir data
curl -o document.pdf https://www.gettingstarted.ai/content/files/2023/12/document.pdf
```

You will also need an instance of Chroma running - easiest to do via Docker

```
 docker run -p 8000:8000 chromadb/chroma
 ```

