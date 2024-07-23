from flask import Flask, request, render_template
from langchain_google_genai import GoogleGenerativeAI

app = Flask(__name__)
api_key = "google-api-key"

llm = GoogleGenerativeAI(model="gemini-1.5-pro", google_api_key=api_key)

@app.route('/')
def index():
    return render_template('index1.html')

def call_api(text):
    return llm.invoke(text)

@app.route('/generate', methods=['POST'])
def generate():
    input_text = request.form['input_text']
    output = call_api(input_text)
    return render_template('index.html', input_text=input_text, generated_text=output)

if __name__ == '__main__':
    app.run(debug=True)
