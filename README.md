# Project Report: LangChain-Based Chatbot with Flask API  

## 1. Introduction  
This project involves building a custom chatbot using LangChain, leveraging web scraping, vector embeddings, and a Flask-based REST API. The chatbot extracts course data from Brainlox, creates vector embeddings, stores them in a vector database, and enables conversational interaction.  

## 2. Project Objectives  
- Extract technical course data from Brainlox using LangChain URL loaders.  
- Generate vector embeddings for textual data.  
- Store embeddings in a vector database (ChromaDB for persistence).  
- Develop a RESTful API using Flask to facilitate chatbot interactions.  

## 3. Implementation Details  

### 3.1 Web Scraping with LangChain  
- **Tool Used**: LangChain's `WebBaseLoader`  
- **Source URL**: [Brainlox Courses](https://brainlox.com/courses/category/technical)  
- **Process**: Extracts web content and splits it into manageable chunks using `RecursiveCharacterTextSplitter`.  

### 3.2 Embeddings & Vector Storage  
- **Embedding Model**: OpenAIEmbeddings  
- **Vector Database**: ChromaDB (for persistence and efficient retrieval)  
- **Storage Method**: Data is stored locally in `chroma_store/`.  

### 3.3 Flask REST API  
- **Framework**: Flask + Flask-CORS  
- **Endpoints**:  
  - `/chat` (POST): Accepts user queries, retrieves responses using LangChain's `ConversationalRetrievalChain`, and maintains conversation history.  
- **Conversation History**: Stored for context retention in chatbot responses.  

## 4. Technologies Used  
- **Programming Language**: Python  
- **Libraries**: LangChain, Flask, ChromaDB, OpenAI, Requests  
- **Database**: ChromaDB for vector storage  
- **Deployment**: Can be run locally using `python app.py`  

## 5. Setup & Execution  
1. **Install Dependencies:**  
   ```bash
   pip install flask flask-cors langchain chromadb openai
   ```  
2. **Run the Flask API:**  
   ```bash
   python app.py
   ```  
3. **Test API:** Use Postman or cURL to send POST requests to `/chat` with a JSON payload.  

## 6. Conclusion  
This project successfully integrates LangChain for web scraping, vector embeddings, and retrieval-based chatbot interaction. Using ChromaDB ensures efficient data storage and retrieval, while Flask provides an API interface for chatbot interactions.  

## 7. Future Enhancements  
- Deploy the API on a cloud platform (AWS, GCP, or Azure).  
- Implement authentication mechanisms.  
- Enhance response accuracy with fine-tuned embeddings.  
- Support multiple languages for chatbot interactions.  
