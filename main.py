from flask import Flask, request, jsonify
from openai import OpenAI
from flask_cors import CORS  # Import CORS
from config import apikey
import os


app = Flask(__name__)
CORS(app, resources={r"/chat": {"origins": "*"}})

client = OpenAI(api_key=apikey)
# Use an environment variable for the API key
apikey = os.environ.get('OPENAI_API_KEY')
@app.route('/chat', methods=['POST'])

def chat():
    data = request.get_json()
    user_input = data['messages']
    response = get_api_response(user_input)
    return jsonify({'response': response})


def get_api_response(prompt: str) -> str:
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo-0125", 
            # messages=[
            #     {
            #         "role": "system",
            #         "content": "You are a helpful assistant knowledgeable in banking."
            #     },
            #     {
            #         "role": "user",
            #         "content": prompt
            #     },
      
            # ],
            messages = prompt,
            temperature=0.7, 
            max_tokens=256, 
            top_p=1, 
            frequency_penalty=0,
            presence_penalty=0
        )

        message_content = response.choices[0].message.content
        return message_content 
    except Exception as e:
        print(f"Error: {e}")
        return None

# user_input = "How can I increase my credit score?"
# response = get_api_response(user_input)
# print(response) 
    
if __name__ == '__main__':
    app.run(debug=True)   
