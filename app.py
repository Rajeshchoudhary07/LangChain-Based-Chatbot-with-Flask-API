from flask import Flask, request, jsonify
from flask_cors import CORS
from scraper import scrape_data
from embeddings import create_vector_store
from chat import create_chatbot

# Initialize Flask App
app = Flask(__name__)
CORS(app)

# Prepare Data and Load Vector Store
docs = scrape_data()
vectorstore = create_vector_store(docs)
qa_chain = create_chatbot(vectorstore)
chat_history = []

@app.route("/chat", methods=["POST"])
def chat():
    global chat_history
    user_input = request.json.get("message")
    if not user_input:
        return jsonify({"error": "No message provided"}), 400

    response = qa_chain.run({"question": user_input, "chat_history": chat_history})
    chat_history.append((user_input, response))

    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
