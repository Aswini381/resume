from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os
load_dotenv()

loader = PyPDFLoader("rag/resume.pdf")

documents = loader.load()

text_splitters = RecursiveCharacterTextSplitter(
    chunk_size = 500,
    chunk_overlap = 100
)

chunks = text_splitters.split_documents(documents)

embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

chunk_texts = [chunk.page_content for chunk in chunks]

embedding = embedding_model.encode(chunk_texts)

embeddings = np.array(embedding).astype("float32")

dimension = embeddings.shape[1]

index = faiss.IndexFlatL2(dimension)

index.add(embeddings)



def ask_rag(question):
    question_embedding = embedding_model.encode([question])

    question_embedding = np.array(question_embedding).astype("float32")

    distances, indices = index.search(
        question_embedding,
        k=3
    )

    retrieved_chunks = []
    for i in indices[0]:
        retrieved_chunks.append(chunk_texts[i])

    context = "\n\n".join(retrieved_chunks)

    llm = ChatGroq(
        model="openai/gpt-oss-120b",
        temperature=0
    )
    prompt = f"""
    You are an AI assistant for my portfolio.

    Answer the user's question using ONLY the information
    provided in the resume context below.

    If the answer is not available in the context,
    say that the information is not available in the resume.

    Resume Context:
    {context}

    User Question:
    {question}
    """

    response = llm.invoke(prompt)

    return response.content

print(ask_rag("what projects have you built?"))