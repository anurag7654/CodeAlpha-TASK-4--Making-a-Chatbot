# 🤖 AI Chatbot with Groq – CodeAlpha Internship Task 4

This project is a **Generative AI Chatbot** developed as part of **Task 4** for the **CodeAlpha Internship** under the *Cloud and Cyber Technology* domain.

The chatbot uses **Groq's Mixtral-8x7B** language model to provide real-time responses and is built with **Flask** for the backend and **HTML/JavaScript** for the frontend. It is deployed on **Render** for live access.

---

## 🚀 Features

- ⚡ **Fast Responses** using Groq’s high-speed LLM API  
- 🧠 **Context-aware replies** powered by Mixtral-8x7B  
- 🌐 **Web interface** using HTML, CSS, and JS  
- 🔐 **Secure API Key Handling** using environment variables  
- ☁️ **Cloud Deployment** via Render  
- ✅ Error handling and fallback messages

---

## 📂 Project Structure

CodeAlpha-TASK-4--Making-a-Chatbot/
├── main.py # Flask backend
├── templates/
│ └── index.html # Frontend UI
├── static/
│ └── script.js # JS for sending/receiving chat
├── requirements.txt # Python dependencies
├── .gitignore # Ignoring .env, pycache, etc.
└── .env (not pushed) # Contains GROQ_API_KEY

yaml
Copy code

---

## ⚙️ Setup Instructions

### 1. Clone the Repo

```bash
git clone https://github.com/anurag7654/CodeAlpha-TASK-4--Making-a-Chatbot.git
cd CodeAlpha-TASK-4--Making-a-Chatbot
2. Create a Virtual Environment
bash
Copy code
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
3. Install Dependencies
bash
Copy code
pip install -r requirements.txt
4. Set Up Environment Variable
Create a .env file in the root directory:

env
Copy code
GROQ_API_KEY=your_groq_api_key_here
💡 You can get your API key from https://console.groq.com

5. Run the App Locally
bash
Copy code
python main.py
Visit http://localhost:5000 in your browser.

☁️ Deployment on Render
Push this repo to GitHub

Create a new Web Service on Render

Connect your GitHub repo

Set environment variable:

Key: GROQ_API_KEY

Value: your actual API key

Set Build Command: pip install -r requirements.txt

Set Start Command: python main.py

🔑 API Details
Endpoint: https://api.groq.com/openai/v1/chat/completions

Model: mixtral-8x7b-32768

Method: POST

Headers:

Authorization: Bearer YOUR_API_KEY

Content-Type: application/json

📸 Screenshots
📷 Add your screenshots here:

Chatbot web UI

Render dashboard (Live)

API response example

GitHub commits

✅ Status
✅ Completed and Working
🚀 Live on Render (if public)

📚 Learning Outcome
Integrated LLM APIs with a Flask web app

Deployed full-stack AI project to the cloud

Managed API keys securely

Debugged and tested real-time response systems

🙏 Acknowledgements
💼 CodeAlpha for the internship opportunity

🧠 Groq for fast & free LLM inference

☁️ Render for cloud hosting

❤️ Open-source contributors and Flask docs

📎 License
This project is for educational and internship purposes under CodeAlpha.
Feel free to fork or improve it!

👤 Author
Anurag