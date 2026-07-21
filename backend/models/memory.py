from datetime import datetime
from typing import List, Dict, Optional
import json

class ConversationMemory:
    """Store conversation history for context-aware responses"""
    
    def __init__(self, conversation_id: int, user_id: int):
        self.conversation_id = conversation_id
        self.user_id = user_id
        self.history = []
        self.context = {}
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
    
    def add_message(self, role: str, content: str):
        """Add a message to conversation history"""
        self.history.append({
            "role": role,
            "content": content,
            "timestamp": datetime.now().isoformat()
        })
        self.updated_at = datetime.now()
        self._extract_context(content)
    
    def _extract_context(self, content: str):
        """Extract key information from messages for context"""
        # Simple context extraction - can be enhanced
        if "name" in content.lower():
            # Try to extract name
            parts = content.split("name")
            if len(parts) > 1:
                potential_name = parts[1].strip()
                if potential_name:
                    self.context["user_name"] = potential_name.split()[0]
        
        if "like" in content.lower():
            # Extract preferences
            self.context["preferences"] = content
    
    def get_context(self) -> Dict:
        """Get the current context of the conversation"""
        return {
            "history": self.history[-10:],  # Last 10 messages
            "context": self.context,
            "conversation_id": self.conversation_id,
            "user_id": self.user_id
        }
    
    def get_formatted_history(self) -> List[Dict]:
        """Get formatted history for Gemini API"""
        formatted = []
        for msg in self.history:
            formatted.append({
                "role": msg["role"],
                "parts": [msg["content"]]
            })
        return formatted
    
    def to_dict(self) -> Dict:
        """Convert to dictionary for storage"""
        return {
            "conversation_id": self.conversation_id,
            "user_id": self.user_id,
            "history": self.history,
            "context": self.context,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()
        }

# Global memory store (in-memory, replace with database later)
memory_store = {}

def get_memory(conversation_id: int, user_id: int) -> ConversationMemory:
    """Get or create memory for a conversation"""
    key = f"{user_id}_{conversation_id}"
    if key not in memory_store:
        memory_store[key] = ConversationMemory(conversation_id, user_id)
    return memory_store[key]

def save_memory(memory: ConversationMemory):
    """Save memory to store"""
    key = f"{memory.user_id}_{memory.conversation_id}"
    memory_store[key] = memory

def clear_memory(conversation_id: int, user_id: int):
    """Clear memory for a conversation"""
    key = f"{user_id}_{conversation_id}"
    if key in memory_store:
        del memory_store[key]