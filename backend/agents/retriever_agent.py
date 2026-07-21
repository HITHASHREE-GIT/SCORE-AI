from agents.base_agent import BaseAgent
from services.simple_vector_service import vector_service
from typing import Dict, Any

class RetrieverAgent(BaseAgent):
    def __init__(self):
        super().__init__("RetrieverAgent")
    
    async def process(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        query = input_data.get("query", "")
        n_results = input_data.get("n_results", 5)
        
        print(f"🔍 Searching for: {query}")
        
        # Search vector database
        results = vector_service.search(query, n_results)
        
        print(f"📚 Found {len(results)} results")
        
        return {
            "documents": results,
            "query": query,
            "num_retrieved": len(results)
        }