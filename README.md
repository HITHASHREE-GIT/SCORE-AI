# 🚀 SCORE AI - Self-Correcting Orchestrated RAG Engine

![SCORE AI Banner](https://img.shields.io/badge/SCORE-AI-purple)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.115.6-green)](https://fastapi.tiangolo.com)
[![React](https://img.shields.io/badge/React-18-blue)](https://react.dev)
[![Groq](https://img.shields.io/badge/Groq-Llama3-orange)](https://groq.com)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

---

# 📋 Overview

**SCORE AI (Self-Correcting Orchestrated RAG Engine)** is an AI-powered intelligent retrieval system designed to reduce hallucinations and improve response accuracy through multi-agent orchestration.

The platform combines **Retrieval Augmented Generation (RAG)**, AI agents, security middleware, and document intelligence to create a reliable AI assistant.

### SCORE AI focuses on:

- Accurate AI responses
- Self-correction mechanisms
- Secure AI interactions
- Context-aware conversations
- Document-based knowledge retrieval

---

# 🎯 Key Features

| Feature | Description |
|---|---|
| 🤖 Multi-Agent System | Retriever, Generator, and Evaluator agents |
| 🔄 Self-Correction Engine | Evaluates and improves AI responses |
| 📄 Document Intelligence | Upload and process documents |
| 🔍 Semantic Search | Vector-based document retrieval |
| 📚 Citation Support | Source-aware AI responses |
| 🧠 Conversation Memory | Stores contextual conversations |
| 🔐 JWT Authentication | Secure registration and login |
| 🛡️ PII Protection | Detects and removes sensitive information |
| ⚡ Groq AI Integration | Llama 3.3 powered responses |
| 🚦 Rate Limiting | API protection |
| 🎨 Modern UI | React + Tailwind interface |

---

# 🏗️ Architecture
                     USER
                       |
                       |
              React Frontend
                Port: 5173
                       |
                       |
              FastAPI Backend
                Port: 8000
                       |
    -----------------------------------
    |              |                  |
 Auth API       AI Engine        Documents
    |              |                  |
   JWT        Groq Llama        ChromaDB
                   |
          Multi-Agent System
                   |
    -----------------------------------
    |              |                  |
Retriever     Generator          Evaluator
                   |
          Self Correction Layer