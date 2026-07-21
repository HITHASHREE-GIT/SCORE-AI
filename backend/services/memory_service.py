from models.memory import get_memory, save_memory, clear_memory
from typing import Dict, List, Optional

class MemoryService:
    """Service to manage conversation memory"""
    
    @staticmethod
    def add_user_message(conversation_id: int, user_id: int, content: str):
        """Add user message to memory"""
        memory = get_memory(conversation_id, user_id)
        memory.add_message("user", content)
        save_memory(memory)
        return memory.get_context()
    
    @staticmethod
    def add_ai_message(conversation_id: int, user_id: int, content: str):
        """Add AI message to memory"""
        memory = get_memory(conversation_id, user_id)
        memory.add_message("assistant", content)
        save_memory(memory)
        return memory.get_context()
    
    @staticmethod
    def get_conversation_context(conversation_id: int, user_id: int) -> Dict:
        """Get full context for AI prompt"""
        memory = get_memory(conversation_id, user_id)
        context = memory.get_context()
        
        # Build prompt context
        prompt_context = "Previous conversation:\n"
        for msg in context["history"][-5:]:  # Last 5 messages
            prompt_context += f"{msg['role']}: {msg['content']}\n"
        
        if context["context"]:
            prompt_context += f"\nContext: {json.dumps(context['context'], indent=2)}\n"
        
        return {
            "formatted_history": memory.get_formatted_history(),
            "prompt_context": prompt_context,
            "context_data": context["context"]
        }
    
    @staticmethod
    def clear_conversation(conversation_id: int, user_id: int):
        """Clear conversation memory"""
        clear_memory(conversation_id, user_id)
        return {"message": "Conversation memory cleared"}

import json  # Add this at top