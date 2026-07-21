from agents.base_agent import BaseAgent
from ai_service import get_ai_response
from typing import Dict, Any

class GeneratorAgent(BaseAgent):
    def __init__(self):
        super().__init__("GeneratorAgent")
    
    async def process(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        query = input_data.get("query", "")
        documents = input_data.get("documents", [])
        
        print(f"🔄 Generating answer for: {query}")
        print(f"📄 Using {len(documents)} documents")
        
        # Build context from retrieved documents
        context = "\n\n---\n\n".join([doc['text'] for doc in documents])
        
        # Build prompt with context
        prompt = f"""
You are a helpful AI assistant. Answer the user's question based ONLY on the provided documents below.

If the answer is not in the documents, say "I cannot find this information in the documents."

DOCUMENTS:
{context}

USER QUESTION: {query}

YOUR ANSWER (based ONLY on the documents):
"""
        
        # Generate response
        response = get_ai_response(prompt)
        
        # Create citations
        citations = []
        for i, doc in enumerate(documents):
            source = doc.get('metadata', {}).get('source', f'Document {i+1}')
            citations.append({
                "id": i + 1,
                "source": source,
                "text": doc['text'][:200] + "..." if len(doc['text']) > 200 else doc['text']
            })
        
        return {
            "answer": response,
            "citations": citations,
            "documents_used": len(documents)
        }