import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import { Menu, X, Bot } from 'lucide-react';

const Navbar = () => {
  const [isOpen, setIsOpen] = useState(false);

  return (
    <nav className="fixed top-0 left-0 right-0 z-50 bg-gray-900/80 backdrop-blur-xl border-b border-white/10">
      <div className="container mx-auto px-4">
        <div className="flex items-center justify-between h-16">
          <Link to="/" className="flex items-center gap-2">
            <div className="w-8 h-8 bg-gradient-to-r from-purple-500 to-blue-500 rounded-lg flex items-center justify-center">
              <Bot className="w-5 h-5 text-white" />
            </div>
            <span className="text-xl font-bold text-white">SCORE AI</span>
          </Link>

          <div className="hidden md:flex items-center gap-8">
            <Link to="/" className="text-gray-300 hover:text-white transition-colors">Home</Link>
            <Link to="/features" className="text-gray-300 hover:text-white transition-colors">Features</Link>
            <Link to="/login" className="px-4 py-2 text-gray-300 hover:text-white transition-colors">Sign In</Link>
            <Link to="/register" className="px-6 py-2 bg-gradient-to-r from-purple-600 to-blue-600 hover:from-purple-700 hover:to-blue-700 rounded-lg text-white font-semibold transition-all transform hover:scale-105">
              Get Started
            </Link>
          </div>

          <button onClick={() => setIsOpen(!isOpen)} className="md:hidden text-gray-300 hover:text-white">
            {isOpen ? <X className="w-6 h-6" /> : <Menu className="w-6 h-6" />}
          </button>
        </div>

        {isOpen && (
          <div className="md:hidden py-4 border-t border-white/10">
            <div className="flex flex-col gap-2">
              <Link to="/" className="px-4 py-2 text-gray-300 hover:bg-white/10 rounded-lg" onClick={() => setIsOpen(false)}>Home</Link>
              <Link to="/features" className="px-4 py-2 text-gray-300 hover:bg-white/10 rounded-lg" onClick={() => setIsOpen(false)}>Features</Link>
              <Link to="/login" className="px-4 py-2 text-gray-300 hover:bg-white/10 rounded-lg" onClick={() => setIsOpen(false)}>Sign In</Link>
              <Link to="/register" className="px-4 py-2 bg-gradient-to-r from-purple-600 to-blue-600 rounded-lg text-white font-semibold text-center" onClick={() => setIsOpen(false)}>Get Started</Link>
            </div>
          </div>
        )}
      </div>
    </nav>
  );
};

export default Navbar;