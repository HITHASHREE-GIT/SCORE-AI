import redis
import hashlib
import json
from typing import Optional

class SemanticCache:
    def __init__(self, host='localhost', port=6379, db=0):
        try:
            self.redis = redis.Redis(host=host, port=port, db=db, decode_responses=True)
            self.enabled = True
        except:
            print("⚠️ Redis not available. Cache disabled.")
            self.enabled = False
    
    def _get_key(self, query: str) -> str:
        """Generate cache key from query"""
        return f"cache:{hashlib.md5(query.encode()).hexdigest()}"
    
    def get(self, query: str) -> Optional[dict]:
        """Get cached response"""
        if not self.enabled:
            return None
        
        key = self._get_key(query)
        cached = self.redis.get(key)
        if cached:
            return json.loads(cached)
        return None
    
    def set(self, query: str, response: dict, ttl: int = 3600):
        """Cache response with TTL (1 hour default)"""
        if not self.enabled:
            return
        
        key = self._get_key(query)
        self.redis.setex(key, ttl, json.dumps(response))
    
    def invalidate(self, query: str):
        """Invalidate cache for a query"""
        if not self.enabled:
            return
        
        key = self._get_key(query)
        self.redis.delete(key)

semantic_cache = SemanticCache()