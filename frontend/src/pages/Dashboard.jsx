import React, { useState, useEffect } from 'react';
import { useAuth } from '../context/AuthContext';
import ChatInterface from '../components/ChatInterface';
import { Bot, MessageSquare, History, Settings, User } from 'lucide-react';

const Dashboard = () => {
  const { user } = useAuth();
  const [activeTab, setActiveTab] = useState('chat');

  return (
    <div className="min-h-screen bg-gradient-to-b from-gray-900 via-gray-800 to-black pt-20">
      <div className="container mx-auto px-4 max-w-7xl">
        {/* Welcome Header */}
        <div className="mb-8">
          <div className="flex items-center gap-3">
            <div className="w-12 h-12 bg-gradient-to-r from-purple-500 to-blue-500 rounded-full flex items-center justify-center">
              <User className="w-6 h-6 text-white" />
            </div>
            <div>
              <h1 className="text-3xl font-bold text-white">
                Welcome back, {user?.name || 'User'}! 👋
              </h1>
              <p className="text-gray-400">Start a conversation with AI - it remembers context!</p>
            </div>
          </div>
        </div>

        {/* Tab Navigation */}
        <div className="flex gap-2 mb-8 border-b border-white/10 pb-4">
          <button
            onClick={() => setActiveTab('chat')}
            className={`px-6 py-2.5 rounded-lg font-semibold transition-all flex items-center gap-2 ${
              activeTab === 'chat'
                ? 'bg-gradient-to-r from-purple-600 to-blue-600 text-white shadow-lg shadow-purple-500/25'
                : 'text-gray-400 hover:text-white hover:bg-white/5'
            }`}
          >
            <MessageSquare className="w-5 h-5" />
            💬 Chat
          </button>
          <button
            onClick={() => setActiveTab('history')}
            className={`px-6 py-2.5 rounded-lg font-semibold transition-all flex items-center gap-2 ${
              activeTab === 'history'
                ? 'bg-gradient-to-r from-purple-600 to-blue-600 text-white shadow-lg shadow-purple-500/25'
                : 'text-gray-400 hover:text-white hover:bg-white/5'
            }`}
          >
            <History className="w-5 h-5" />
            📜 History
          </button>
          <button
            onClick={() => setActiveTab('settings')}
            className={`px-6 py-2.5 rounded-lg font-semibold transition-all flex items-center gap-2 ${
              activeTab === 'settings'
                ? 'bg-gradient-to-r from-purple-600 to-blue-600 text-white shadow-lg shadow-purple-500/25'
                : 'text-gray-400 hover:text-white hover:bg-white/5'
            }`}
          >
            <Settings className="w-5 h-5" />
            ⚙️ Settings
          </button>
        </div>

        {/* Content Area */}
        <div className="bg-white/5 backdrop-blur-sm rounded-xl border border-white/10 p-6">
          {activeTab === 'chat' && <ChatInterface />}
          
          {activeTab === 'history' && (
            <div className="text-center py-20">
              <History className="w-16 h-16 text-gray-600 mx-auto mb-4" />
              <h3 className="text-xl text-white font-semibold mb-2">Conversation History</h3>
              <p className="text-gray-400">Your past conversations will appear here</p>
              <p className="text-gray-500 text-sm mt-2">The AI remembers context from all your chats!</p>
            </div>
          )}
          
          {activeTab === 'settings' && (
            <div className="max-w-2xl mx-auto py-10">
              <h3 className="text-xl text-white font-semibold mb-6">Settings</h3>
              <div className="space-y-4">
                <div className="bg-white/5 rounded-lg p-4 border border-white/10">
                  <label className="text-white font-medium">User Profile</label>
                  <p className="text-gray-400 text-sm">Name: {user?.name}</p>
                  <p className="text-gray-400 text-sm">Email: {user?.email}</p>
                </div>
                <div className="bg-white/5 rounded-lg p-4 border border-white/10">
                  <label className="text-white font-medium">Memory Settings</label>
                  <p className="text-gray-400 text-sm">✅ Context memory is enabled</p>
                  <p className="text-gray-400 text-sm">✅ AI remembers conversation history</p>
                </div>
                <button className="px-6 py-2 bg-red-500/10 hover:bg-red-500/20 text-red-400 rounded-lg transition-all">
                  Clear All Memory
                </button>
              </div>
            </div>
          )}
        </div>
      </div>
    </div>
  );
};

export default Dashboard;