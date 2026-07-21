from agents.base_agent import BaseAgent
from ai_service import get_ai_response
from typing import Dict, Any

class EvaluatorAgent(BaseAgent):
    def __init__(self):
        super().__init__("EvaluatorAgent")
    
    async def process(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        query = input_data.get("query", "")
        answer = input_data.get("answer", "")
        documents = input_data.get("documents", [])
        
        # Evaluate Faithfulness (Is the answer grounded?)
        faithfulness_prompt = f"""
        Evaluate if the following answer is faithful to the provided documents.
        Score from 0 to 1 (1 = completely faithful).
        
        Question: {query}
        Answer: {answer}
        
        Documents: {str(documents)[:1000]}
        
        Faithfulness Score (0-1):
        """
        
        faithfulness_response = get_ai_response(faithfulness_prompt)
        try:
            faithfulness = float(faithfulness_response.strip()[:5])
        except:
            faithfulness = 0.5
        
        # Evaluate Sufficiency (Did we have enough info?)
        sufficiency_prompt = f"""
        Evaluate if we had sufficient information in the documents to answer.
        Score from 0 to 1 (1 = completely sufficient).
        
        Question: {query}
        Number of documents retrieved: {len(documents)}
        
        Sufficiency Score (0-1):
        """
        
        sufficiency_response = get_ai_response(sufficiency_prompt)
        try:
            sufficiency = float(sufficiency_response.strip()[:5])
        except:
            sufficiency = 0.5
        
        return {
            "faithfulness": faithfulness,
            "sufficiency": sufficiency,
            "passed": faithfulness > 0.7 and sufficiency > 0.6
        }