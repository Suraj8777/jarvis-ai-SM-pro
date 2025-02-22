# server.py (Python backend using Flask)
from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

API_KEYS = {
    'weather': 'a5caf05ac5bff33416c4fafb3d168ae1',
    'scene': 'ccc6aaee923a4e57822939126c916aab',
    'ai1': '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',
    'ai2': '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'
}

@app.route('/process', methods=['POST'])
def process_command():
    command = request.json.get('command', '')
    
    # Example: Weather API integration
    if 'weather' in command.lower():
        response = requests.get(
            f'https://api.openweathermap.org/data/2.5/weather?q=London&appid={API_KEYS["weather"]}'
        )
        return jsonify({'response': response.json()})
    
    # Example: AI response
    headers = {
        'Authorization': f'Bearer {API_KEYS["ai1"]}',
        'Content-Type': 'application/json'
    }
    
    data = {
        'prompt': command,
        'max_tokens': 100
    }
    
    ai_response = requests.post(
        'https://api.openai.com/v1/engines/davinci/completions',
        headers=headers,
        json=data
    )
    
    return jsonify({'response': ai_response.json()['choices'][0]['text']})

if __name__ == '__main__':
    app.run(debug=True)
