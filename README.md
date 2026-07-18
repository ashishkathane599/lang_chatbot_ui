# 🤖 LangGraph AI Chatbot

A conversational AI chatbot built using **LangGraph**, **LangChain**, **Groq LLM**, and **Streamlit**. This project demonstrates how to build a stateful AI chatbot using LangGraph's graph-based workflow while providing a clean and interactive Streamlit interface.

## 🌐 Live Demo

👉 **Try the chatbot here:**  
https://langchatbotui-ajt9fssg8exq3cslnyyudd.streamlit.app/

---

## 🚀 Features

- 💬 Interactive chatbot interface using Streamlit
- 🧠 Stateful conversations powered by LangGraph
- ⚡ Fast inference using Groq API
- 🔄 Graph-based execution workflow
- 📝 Session-based chat history
- 🔐 Environment variable support using `.env`
- 🧩 Simple and modular code structure

---

## 🛠️ Tech Stack

- Python
- Streamlit
- LangGraph
- LangChain
- Groq API
- python-dotenv

---

## 📂 Project Structure

```
Langraph-chatbot/
│
├── streamlit_frontend.py      # Streamlit UI
├── langgraph_backend.py       # LangGraph workflow
├── requirements.txt
├── .gitignore
├── .env                       # API Keys (Not included)
└── README.md
```

---

## ⚙️ How It Works

### Frontend

The Streamlit application:

- Accepts user input through a chat interface.
- Stores conversation history using `st.session_state`.
- Sends user messages to the LangGraph backend.
- Displays AI responses in real time.

### Backend

The backend creates a simple LangGraph workflow:

```
START
   │
   ▼
Chat Node
   │
   ▼
 END
```

The chatbot:

1. Receives the conversation state.
2. Passes the messages to the Groq LLM.
3. Gets the AI response.
4. Updates the conversation state.
5. Returns the latest response to the frontend.

---

## 🧠 LangGraph Workflow

```python
START
   │
   ▼
Chat Node
   │
   ▼
 END
```

The graph consists of a single AI node that processes user messages and generates responses using the Groq language model.

---

## 📦 Installation

### Clone the repository

```bash
git clone https://github.com/ashishkathane599/lang_chatbot_ui.git
cd lang_chatbot_ui
```

### Create a virtual environment

```bash
python -m venv .venv
```

### Activate the environment

Windows

```bash
.venv\Scripts\activate
```

Linux / macOS

```bash
source .venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file in the project root.

```env
GROQ_API_KEY=your_groq_api_key
```

---

## ▶️ Run the Application

```bash
streamlit run streamlit_frontend.py
```

---

## 📸 Demo

You can also try the hosted version:

**https://langchatbotui-ajt9fssg8exq3cslnyyudd.streamlit.app/**

---

## 📚 What You'll Learn

This project demonstrates:

- Building conversational AI applications
- LangGraph fundamentals
- Managing conversation state
- Integrating Groq LLM with LangChain
- Creating interactive Streamlit applications
- Structuring AI projects for production

---

## 🔮 Future Improvements

- Conversation memory persistence
- Multiple chat sessions
- Streaming responses
- File upload support
- RAG (Retrieval-Augmented Generation)
- Authentication
- Database integration
- Chat history export

---

## 👨‍💻 Author

**Ashish Kathane**

- LinkedIn: https://www.linkedin.com/in/ashish-kathane/
- GitHub: https://github.com/ashishkathane599

---

## ⭐ Support

If you found this project helpful, consider giving it a ⭐ on GitHub. It helps others discover the project and motivates future improvements.
