import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { Send, Bot, User, Plus, MessageSquare, Trash2 } from 'lucide-react';

const API_URL = 'http://localhost:8000';

const ChatInterface = () => {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState('');
  const [loading, setLoading] = useState(false);
  const [conversations, setConversations] = useState([]);
  const [currentConversation, setCurrentConversation] = useState(null);
  const [user, setUser] = useState({ id: 1 });

  // Load conversations on mount
  useEffect(() => {
    loadConversations();
  }, []);

  const loadConversations = async () => {
    try {
      const response = await axios.get(`${API_URL}/conversations/`);
      setConversations(response.data);
      if (response.data.length > 0) {
        setCurrentConversation(response.data[0]);
        loadMessages(response.data[0].id);
      }
    } catch (error) {
      console.error('Error loading conversations:', error);
    }
  };

  const loadMessages = async (conversationId) => {
    try {
      const response = await axios.get(
        `${API_URL}/messages/conversation/${conversationId}`
      );
      setMessages(response.data);
    } catch (error) {
      console.error('Error loading messages:', error);
    }
  };

  const createNewConversation = async () => {
    try {
      const response = await axios.post(`${API_URL}/conversations/`, {
        title: `Chat ${conversations.length + 1}`,
        user_id: user.id
      });
      setConversations([...conversations, response.data]);
      setCurrentConversation(response.data);
      setMessages([]);
    } catch (error) {
      console.error('Error creating conversation:', error);
    }
  };

  const clearConversation = async () => {
    if (!currentConversation) return;
    try {
      await axios.post(`${API_URL}/ai/chat/clear`, null, {
        params: {
          conversation_id: currentConversation.id,
          user_id: user.id
        }
      });
      setMessages([]);
    } catch (error) {
      console.error('Error clearing conversation:', error);
    }
  };

  const sendMessage = async () => {
    if (!input.trim() || !currentConversation) return;

    // Add user message to UI immediately
    const userMessage = { role: 'user', content: input };
    setMessages(prev => [...prev, userMessage]);
    setInput('');
    setLoading(true);

    try {
      // Send message with conversation context
      const response = await axios.post(`${API_URL}/ai/chat`, {
        message: input,
        conversation_id: currentConversation.id,
        user_id: user.id
      });

      // Add AI response to UI
      const aiMessage = { 
        role: 'assistant', 
        content: response.data.response 
      };
      setMessages(prev => [...prev, aiMessage]);
      
      // If context was used, show it (optional)
      if (response.data.context_used && Object.keys(response.data.context_used).length > 0) {
        console.log('Context used:', response.data.context_used);
      }
      
    } catch (error) {
      console.error('Chat error:', error);
      setMessages(prev => [...prev, { 
        role: 'assistant', 
        content: 'Sorry, I encountered an error. Please try again.' 
      }]);
    } finally {
      setLoading(false);
    }
  };

  const handleKeyPress = (e) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      sendMessage();
    }
  };

  return (
    <div className="flex gap-4 h-[600px]">
      {/* Sidebar - Conversations List */}
      <div className="w-64 bg-white/5 rounded-xl border border-white/10 p-4 overflow-y-auto flex flex-col">
        <button
          onClick={createNewConversation}
          className="w-full mb-4 px-4 py-2 bg-gradient-to-r from-purple-600 to-blue-600 rounded-lg text-white font-semibold flex items-center justify-center gap-2 hover:scale-105 transition-transform"
        >
          <Plus className="w-4 h-4" />
          New Chat
        </button>
        
        <div className="flex-1 space-y-2 overflow-y-auto">
          {conversations.map((conv) => (
            <button
              key={conv.id}
              onClick={() => {
                setCurrentConversation(conv);
                loadMessages(conv.id);
              }}
              className={`w-full text-left px-4 py-2 rounded-lg transition-all flex items-center gap-2 ${
                currentConversation?.id === conv.id
                  ? 'bg-purple-500/20 text-white'
                  : 'text-gray-400 hover:bg-white/5'
              }`}
            >
              <MessageSquare className="w-4 h-4 flex-shrink-0" />
              <span className="truncate text-sm">{conv.title}</span>
            </button>
          ))}
        </div>
        
        {currentConversation && (
          <button
            onClick={clearConversation}
            className="mt-4 w-full px-4 py-2 bg-red-500/10 hover:bg-red-500/20 rounded-lg text-red-400 font-semibold flex items-center justify-center gap-2 transition-all"
          >
            <Trash2 className="w-4 h-4" />
            Clear Chat
          </button>
        )}
      </div>

      {/* Chat Area */}
      <div className="flex-1 flex flex-col bg-white/5 rounded-xl border border-white/10">
        {/* Conversation Title */}
        {currentConversation && (
          <div className="border-b border-white/10 p-4">
            <h3 className="text-white font-semibold">{currentConversation.title}</h3>
            <p className="text-gray-400 text-sm">Conversation ID: {currentConversation.id}</p>
          </div>
        )}

        {/* Messages */}
        <div className="flex-1 overflow-y-auto p-4 space-y-4">
          {messages.length === 0 ? (
            <div className="text-center text-gray-400 mt-20">
              <Bot className="w-16 h-16 mx-auto mb-4 text-purple-400" />
              <p className="text-xl">Start a conversation with AI</p>
              <p className="text-sm">The AI will remember the conversation context!</p>
            </div>
          ) : (
            messages.map((msg, index) => (
              <div
                key={index}
                className={`flex items-start gap-3 ${
                  msg.role === 'user' ? 'justify-end' : ''
                }`}
              >
                {msg.role === 'assistant' && (
                  <div className="w-8 h-8 bg-purple-500 rounded-full flex items-center justify-center flex-shrink-0">
                    <Bot className="w-5 h-5 text-white" />
                  </div>
                )}
                <div
                  className={`max-w-[70%] p-3 rounded-lg whitespace-pre-wrap ${
                    msg.role === 'user'
                      ? 'bg-purple-600 text-white'
                      : 'bg-white/10 text-white'
                  }`}
                >
                  {msg.content}
                </div>
                {msg.role === 'user' && (
                  <div className="w-8 h-8 bg-blue-500 rounded-full flex items-center justify-center flex-shrink-0">
                    <User className="w-5 h-5 text-white" />
                  </div>
                )}
              </div>
            ))
          )}
          {loading && (
            <div className="flex items-center gap-3">
              <div className="w-8 h-8 bg-purple-500 rounded-full flex items-center justify-center">
                <Bot className="w-5 h-5 text-white animate-pulse" />
              </div>
              <div className="bg-white/10 p-3 rounded-lg text-white">
                <span className="animate-pulse">Thinking...</span>
              </div>
            </div>
          )}
        </div>

        {/* Input */}
        <div className="border-t border-white/10 p-4">
          <div className="flex gap-2">
            <textarea
              value={input}
              onChange={(e) => setInput(e.target.value)}
              onKeyPress={handleKeyPress}
              placeholder="Type your message... (Enter to send)"
              className="flex-1 px-4 py-2 bg-white/5 border border-white/10 rounded-lg text-white placeholder-gray-400 focus:outline-none focus:border-purple-500 resize-none"
              rows="1"
              style={{ minHeight: '44px', maxHeight: '120px' }}
            />
            <button
              onClick={sendMessage}
              disabled={loading || !currentConversation || !input.trim()}
              className="px-6 py-2 bg-gradient-to-r from-purple-600 to-blue-600 hover:from-purple-700 hover:to-blue-700 rounded-lg text-white font-semibold transition-all disabled:opacity-50 disabled:cursor-not-allowed"
            >
              <Send className="w-5 h-5" />
            </button>
          </div>
          {currentConversation && (
            <p className="text-xs text-gray-500 mt-2">
              AI remembers conversation context. Type anything to test memory!
            </p>
          )}
        </div>
      </div>
    </div>
  );
};

export default ChatInterface;