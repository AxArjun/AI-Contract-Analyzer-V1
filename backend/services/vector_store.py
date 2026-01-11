import os
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from pinecone import Pinecone

# Initialize Pinecone (New SDK)
pc = Pinecone(api_key=pcsk_4Whbpt_8DzjqyPqa5Uto2z6A23CQwtsZ7CtfmZhaX5UzRA3SCkkY7snTJgxAaqEFNs7jai)

# Connect to index
index_name = "contract-analysis"

# Check if index exists before connecting (optional, good for safety)
# For now, just connect assuming it exists or user will create it
index = pc.Index(index_name)

embeddings = GoogleGenerativeAIEmbeddings(
    model="models/embedding-001"
)

def store_result(contract_id: str, domain: str, text: str):
    # Embed the text
    vector = embeddings.embed_query(text)
    
    # Upsert to Pinecone
    index.upsert(
        vectors=[
            {
                "id": f"{contract_id}-{domain}", 
                "values": vector, 
                "metadata": {"domain": domain}
            }
        ]
    )
