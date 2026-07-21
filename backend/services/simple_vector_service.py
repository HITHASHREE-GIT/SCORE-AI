import uuid
import json
import os
from typing import List, Dict

class SimpleVectorService:
    def __init__(self):
        self.documents = []
        self.data_file = "vector_data.json"
        self._load_data()
    
    def add_document(self, text: str, metadata: Dict = None):
        doc = {
            'id': str(uuid.uuid4()),
            'text': text,
            'metadata': metadata or {}
        }
        self.documents.append(doc)
        self._save_data()
        return doc['id']
    
    def search(self, query: str, n_results: int = 5) -> List[Dict]:
        # Simple text matching
        results = []
        query_lower = query.lower()
        for doc in self.documents:
            if query_lower in doc['text'].lower():
                results.append({
                    'text': doc['text'],
                    'metadata': doc['metadata'],
                    'distance': 0.3
                })
        
        if not results:
            # Return first few documents as fallback
            for doc in self.documents[:n_results]:
                results.append({
                    'text': doc['text'],
                    'metadata': doc['metadata'],
                    'distance': 0.5
                })
        
        return results[:n_results]
    
    def get_all_documents(self) -> List[Dict]:
        return self.documents
    
    def _save_data(self):
        with open(self.data_file, 'w') as f:
            json.dump(self.documents, f, default=str)
    
    def _load_data(self):
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'r') as f:
                    self.documents = json.load(f)
            except:
                self.documents = []

# Create global instance
vector_service = SimpleVectorService()