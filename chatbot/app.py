from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# Replace with your RapidAPI key and host
RAPIDAPI_KEY = "44ea5782b6mshfc5d9605f874bf9p1d40cdjsn001f5a24f788"
RAPIDAPI_HOST = "cheapest-gpt-4-turbo-gpt-4-vision-chatgpt-openai-ai-api.p.rapidapi.com"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    try:
        user_message = request.json.get("message", "")
        if not user_message:
            return jsonify({"error": "Message is required"}), 400

        url = "https://cheapest-gpt-4-turbo-gpt-4-vision-chatgpt-openai-ai-api.p.rapidapi.com/v1/chat/completions"
        headers = {
            'Content-Type': 'application/json',
            'x-rapidapi-host': RAPIDAPI_HOST,
            'x-rapidapi-key': RAPIDAPI_KEY
        }
        payload = {
            "messages": [{"role": "user", "content": user_message}],
            "model": "gpt-4o",
            "max_tokens": 100,
            "temperature": 0.9
        }

        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()  # Raise exception for HTTP errors

        api_response = response.json()
        chatbot_reply = api_response.get("choices", [{}])[0].get("message", {}).get("content", "")

        return jsonify({"response": chatbot_reply})

    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5001)
