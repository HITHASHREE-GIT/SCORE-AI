# 🚀 SCORE AI - Self-Correcting Orchestrated RAG Engine

![SCORE AI Banner](https://img.shields.io/badge/SCORE-AI-purple)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.115.6-green)](https://fastapi.tiangolo.com)
[![React](https://img.shields.io/badge/React-18-blue)](https://reactjs.org)
[![Cohere](https://img.shields.io/badge/Cohere-AI-orange)](https://cohere.com)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

---

## 📋 Overview

**SCORE AI** is a production-grade **Self-Correcting Orchestrated RAG Engine** designed to eliminate hallucinations and handle complex document retrieval challenges. It features a **Multi-Agent Orchestration** system with automated self-correction and Human-in-the-Loop (HITL) resilience.

### 🎯 Key Features

| Feature | Description |
|---------|-------------|
| 🤖 **Multi-Agent System** | Retriever, Generator, Evaluator agents working together |
| 🔄 **Self-Correction** | 3 paths: Success → Re-Query → HITL |
| 📄 **Document Upload** | PDF, TXT, DOCX support |
| 🔍 **Semantic Search** | Vector search with ChromaDB |
| 📚 **Citations** | Source tracking for every answer |
| 🧠 **Memory System** | Context-aware conversations |
| 🔐 **JWT Authentication** | Secure user registration & login |
| 🛡️ **Rate Limiting** | 10/min chat, 5/min upload |
| 🎨 **Modern UI** | React + Tailwind CSS |
| 📊 **Admin Dashboard** | Streamlit monitoring |

---

## 🏗️ Architecture
┌─────────────────────────────────────────────────────────────┐
│ USER │
└─────────────────────┬───────────────────────────────────────┘
│
┌─────────────────────▼───────────────────────────────────────┐
│ React Frontend (Port 5173) │
└─────────────────────┬───────────────────────────────────────┘
│
┌─────────────────────▼───────────────────────────────────────┐
│ FastAPI Backend (Port 8000) │
│ ┌──────────────────────────────────────────────────────┐ │
│ │ 🔐 Auth │ 💬 Chat │ 📄 Documents │ 📊 Admin │ │
│ └──────────────────────────────────────────────────────┘ │
└─────────────────────┬───────────────────────────────────────┘
│
┌─────────────────────▼───────────────────────────────────────┐
│ Multi-Agent Orchestration │
│ ┌──────────────────────────────────────────────────────┐ │
│ │ 🔍 Retriever │ ✍️ Generator │ ✅ Evaluator │ │
│ └──────────────────────────────────────────────────────┘ │
└─────────────────────┬───────────────────────────────────────┘
│
┌─────────────────────▼───────────────────────────────────────┐
│ Vector Database (ChromaDB) │
└─────────────────────────────────────────────────────────────┘

---

## 🚀 Quick Start

### Prerequisites

- Python 3.11+
- Node.js 18+
- Cohere API Key ([Get it here](https://dashboard.cohere.com/api-keys))

### Installation

#### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/SCORE-AI.git
cd SCORE-AI