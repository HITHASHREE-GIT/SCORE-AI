import streamlit as st
import requests
import json
from datetime import datetime
import uuid  # Add this for generating unique session IDs

# API Configuration
API_URL = "http://localhost:8000"

# Page Config
st.set_page_config(
    page_title="SCORE AI Admin Dashboard",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better UI
st.markdown("""
    <style>
    .main-header {
        font-size: 2.5rem;
        font-weight: 700;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        padding: 1rem 0;
    }
    .metric-card {
        background: linear-gradient(135deg, #667eea15 0%, #764ba215 100%);
        border-radius: 10px;
        padding: 1.5rem;
        border: 1px solid #667eea30;
        margin: 0.5rem 0;
    }
    .chat-message {
        padding: 1rem;
        border-radius: 10px;
        margin: 0.5rem 0;
    }
    .user-message {
        background: #667eea20;
        border-left: 4px solid #667eea;
    }
    .assistant-message {
        background: #764ba220;
        border-left: 4px solid #764ba2;
    }
    .status-badge {
        padding: 0.25rem 1rem;
        border-radius: 20px;
        font-weight: 600;
    }
    .status-success { background: #00ff8820; color: #00ff88; }
    </style>
""", unsafe_allow_html=True)

# Initialize session ID
if "session_id" not in st.session_state:
    st.session_state.session_id = str(uuid.uuid4())

# Sidebar
with st.sidebar:
    st.markdown("## 🚀 SCORE AI")
    st.markdown("### Enterprise RAG System")
    st.markdown("---")
    
    # System Status
    st.markdown("### System Status")
    try:
        health = requests.get(f"{API_URL}/health", timeout=2)
        if health.status_code == 200:
            st.success("✅ All Systems Operational")
        else:
            st.warning("⚠️ System Degraded")
    except:
        st.error("❌ API Unreachable - Start Backend!")
    
    st.markdown("---")
    
    # Navigation
    page = st.radio(
        "Navigation",
        ["📊 Dashboard", "📄 Document Manager", "💬 Chat Interface", "📈 Analytics", "⚙️ Settings"]
    )

# ============================================
# DASHBOARD PAGE
# ============================================
if page == "📊 Dashboard":
    st.markdown('<div class="main-header">📊 SCORE AI Dashboard</div>', unsafe_allow_html=True)
    st.markdown(f"*Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("📄 Documents", "15", "+3")
    with col2:
        st.metric("💬 Conversations", "247", "+12")
    with col3:
        st.metric("🎯 Accuracy", "94.7%", "+2.1%")
    with col4:
        st.metric("⚡ Avg Latency", "1.2s", "-0.3s")

# ============================================
# DOCUMENT MANAGER PAGE
# ============================================
elif page == "📄 Document Manager":
    st.markdown('<div class="main-header">📄 Document Manager</div>', unsafe_allow_html=True)
    
    tab1, tab2, tab3 = st.tabs(["📤 Upload", "📋 All Documents", "🔍 Search"])
    
    with tab1:
        st.markdown("### Upload Document")
        uploaded_file = st.file_uploader("Choose a file", type=['pdf', 'txt', 'docx', 'md'])
        if uploaded_file is not None:
            col1, col2 = st.columns(2)
            with col1:
                if st.button("📤 Upload Document", use_container_width=True):
                    with st.spinner("Uploading..."):
                        files = {'file': (uploaded_file.name, uploaded_file.getvalue())}
                        response = requests.post(f"{API_URL}/documents/upload", files=files)
                        if response.status_code == 200:
                            st.success("✅ Document uploaded successfully!")
                            st.json(response.json())
                        else:
                            st.error(f"❌ Upload failed: {response.text}")
    
    with tab2:
        st.markdown("### All Documents")
        try:
            response = requests.get(f"{API_URL}/documents/")
            if response.status_code == 200:
                docs = response.json()
                if docs.get('documents'):
                    for doc in docs.get('documents', []):
                        with st.expander(f"📄 {doc.get('metadata', {}).get('source', 'Unknown')}"):
                            st.text(doc.get('text', '')[:500] + "...")
                else:
                    st.info("📭 No documents found. Upload one!")
        except:
            st.error("❌ Could not connect to API")
    
    with tab3:
        st.markdown("### Search Documents")
        query = st.text_input("🔍 Enter search query")
        if query:
            try:
                response = requests.get(f"{API_URL}/documents/search", params={"query": query})
                if response.status_code == 200:
                    results = response.json()
                    if results.get('results'):
                        for result in results.get('results', []):
                            with st.expander(f"📄 Score: {result.get('distance', 0):.2f}"):
                                st.text(result.get('text', ''))
                    else:
                        st.info("No results found")
            except:
                st.error("❌ Could not connect to API")

# ============================================
# CHAT INTERFACE PAGE - FIXED
# ============================================
elif page == "💬 Chat Interface":
    st.markdown('<div class="main-header">💬 Chat Interface</div>', unsafe_allow_html=True)
    
    # Initialize messages in session state
    if "messages" not in st.session_state:
        st.session_state.messages = []
    
    # Display chat messages
    st.markdown("### 💬 Conversation")
    
    # Chat container with scroll
    chat_container = st.container()
    with chat_container:
        if len(st.session_state.messages) == 0:
            st.info("💡 Start a conversation! Upload documents first for better responses.")
        else:
            for msg in st.session_state.messages:
                role = msg["role"]
                content = msg["content"]
                if role == "user":
                    st.markdown(f"""
                        <div class="chat-message user-message">
                            <strong>🧑 You:</strong><br>{content}
                        </div>
                    """, unsafe_allow_html=True)
                else:
                    st.markdown(f"""
                        <div class="chat-message assistant-message">
                            <strong>🤖 AI:</strong><br>{content}
                        </div>
                    """, unsafe_allow_html=True)
    
    # ============================================
    # CHAT INPUT - FIXED WITH PROPER SESSION ID
    # ============================================
    st.markdown("---")
    
    # Create a form for chat input
    with st.form(key="chat_form", clear_on_submit=True):
        col1, col2 = st.columns([5, 1])
        with col1:
            prompt = st.text_input(
                "💬 Type your message...",
                placeholder="Ask me anything about your documents...",
                key="chat_input",
                label_visibility="collapsed"
            )
        with col2:
            submit = st.form_submit_button("📤 Send", use_container_width=True)
        
        if submit and prompt:
            # Add user message
            st.session_state.messages.append({"role": "user", "content": prompt})
            
            # Get AI response
            with st.spinner("🤔 Thinking..."):
                try:
                    # FIXED: Use session_id from session state
                    response = requests.post(f"{API_URL}/v1/chat", json={
                        "query": prompt,
                        "user_id": "streamlit_user",
                        "session_id": st.session_state.session_id  # FIXED
                    })
                    
                    if response.status_code == 200:
                        data = response.json()
                        if data.get('status') == 'SUCCESS':
                            answer = data.get('answer', 'No answer provided')
                            st.session_state.messages.append({"role": "assistant", "content": answer})
                            
                            # Show citations if available
                            if data.get('citations'):
                                citation_text = "📚 **Sources:**\n"
                                for citation in data.get('citations', []):
                                    citation_text += f"- {citation.get('source', 'Unknown')}\n"
                                st.session_state.messages.append({"role": "assistant", "content": citation_text})
                        else:
                            st.session_state.messages.append({
                                "role": "assistant", 
                                "content": f"⚠️ {data.get('conflict_summary', 'Need more information')}\n\n💡 Try asking a more specific question or upload relevant documents."
                            })
                    else:
                        st.session_state.messages.append({
                            "role": "assistant", 
                            "content": f"❌ Error: {response.status_code} - Could not get response"
                        })
                except Exception as e:
                    st.session_state.messages.append({
                        "role": "assistant", 
                        "content": f"❌ Connection error: {str(e)}\n\nMake sure backend is running at {API_URL}"
                    })
            
            # Rerun to show new messages
            st.rerun()

# ============================================
# ANALYTICS PAGE
# ============================================
elif page == "📈 Analytics":
    st.markdown('<div class="main-header">📈 Analytics</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### AI Performance")
        st.metric("Average Response Time", "1.2s")
        st.metric("Success Rate", "94.7%")
        st.metric("HITL Rate", "5.3%")
    
    with col2:
        st.markdown("### Usage Statistics")
        st.metric("Total Queries", "1,247")
        st.metric("Unique Users", "89")
        st.metric("Documents Processed", "15")

# ============================================
# SETTINGS PAGE
# ============================================
elif page == "⚙️ Settings":
    st.markdown('<div class="main-header">⚙️ Settings</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### AI Settings")
        st.slider("Max Tokens", 100, 2000, 500)
        st.slider("Temperature", 0.0, 1.0, 0.7, 0.1)
    with col2:
        st.markdown("### System Settings")
        st.number_input("Max Retries", 1, 5, 2)
        st.checkbox("Enable Cache", True)

# Footer
st.markdown("---")
st.caption("🚀 SCORE AI Enterprise RAG System v2.0")
st.markdown("""
    <div style='text-align: center; color: #666; padding: 1rem;'>
        Made with ❤️ by Team SCORE | Powered by Gemini AI, ChromaDB, FastAPI
    </div>
""", unsafe_allow_html=True)