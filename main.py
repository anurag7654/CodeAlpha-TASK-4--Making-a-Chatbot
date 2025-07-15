from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import openai
import os

app = Flask(__name__)
CORS(app)

# Set up the OpenAI client for newer SDK
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message")

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": user_message}],
            max_tokens=150
        )
        reply = response.choices[0].message.content.strip()
        return jsonify({"reply": reply})

    except Exception as e:
        print("Error from OpenAI API:", e)
        return jsonify({"reply": "Sorry, something went wrong."}), 500

# ✅ Required for Render to run correctly
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))

