import json
import logging
from datetime import datetime
from typing import Dict, Any

class LoggingService:
    def __init__(self):
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger("SCORE_AI")
    
    def log_query(self, user_id: str, query: str, response: Dict[str, Any]):
        """Log query and response"""
        log_entry = {
            "timestamp": datetime.now().isoformat(),
            "user_id": user_id,
            "query": query,
            "response_status": response.get("status"),
            "scores": response.get("scores", {}),
            "latency_ms": response.get("latency_ms", 0)
        }
        self.logger.info(json.dumps(log_entry))
    
    def log_error(self, user_id: str, error: str):
        """Log errors"""
        log_entry = {
            "timestamp": datetime.now().isoformat(),
            "user_id": user_id,
            "error": str(error)
        }
        self.logger.error(json.dumps(log_entry))

logging_service = LoggingService()