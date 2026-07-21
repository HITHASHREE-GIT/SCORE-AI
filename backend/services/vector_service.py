import chromadb
from chromadb.utils import embedding_functions
import uuid
from typing import List, Dict, Optional
import os

class VectorService:
    def __init__(self):
        # Initialize ChromaDB with sentence-transformers
        self.client = chromadb.PersistentClient(path="./chromadb_data")
        self.embedding_fn = embedding_functions.SentenceTransformerEmbeddingFunction(
            model_name="all-MiniLM-L6-v2"
        )
        
        # Get or create collection
        self.collection = self.client.get_or_create_collection(
            name="score_documents",
            embedding_function=self.embedding_fn
        )
    
    def add_document(self, text: str, metadata: Dict = None, doc_id: str = None):
        """Add a document to the vector database"""
        if doc_id is None:
            doc_id = str(uuid.uuid4())
        
        if metadata is None:
            metadata = {}
        
        self.collection.add(
            documents=[text],
            metadatas=[metadata],
            ids=[doc_id]
        )
        return doc_id
    
    def add_documents(self, texts: List[str], metadatas: List[Dict] = None):
        """Add multiple documents"""
        ids = [str(uuid.uuid4()) for _ in texts]
        if metadatas is None:
            metadatas = [{} for _ in texts]
        
        self.collection.add(
            documents=texts,
            metadatas=metadatas,
            ids=ids
        )
        return ids
    
    def search(self, query: str, n_results: int = 5) -> List[Dict]:
        """Search for similar documents"""
        results = self.collection.query(
            query_texts=[query],
            n_results=n_results
        )
        
        documents = []
        if results['documents'] and results['documents'][0]:
            for i in range(len(results['documents'][0])):
                documents.append({
                    'text': results['documents'][0][i],
                    'metadata': results['metadatas'][0][i] if results['metadatas'] else {},
                    'distance': results['distances'][0][i] if results['distances'] else None
                })
        return documents
    
    def delete_document(self, doc_id: str):
        """Delete a document"""
        self.collection.delete(ids=[doc_id])
    
    def get_all_documents(self) -> List[Dict]:
        """Get all documents"""
        results = self.collection.get()
        documents = []
        if results['documents']:
            for i in range(len(results['documents'])):
                documents.append({
                    'id': results['ids'][i],
                    'text': results['documents'][i],
                    'metadata': results['metadatas'][i] if results['metadatas'] else {}
                })
        return documents

# Global instance
vector_service = VectorService()