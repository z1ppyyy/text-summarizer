from flask import Flask, render_template, request
from openai import OpenAI
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)

client = OpenAI(api_key='API KEY')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        prompt = request.form['prompt']
        if 'http' in prompt: 
            url = requests.get(prompt)
            soup = BeautifulSoup(url.text, 'html.parser')
            text = soup.get_text()
        else:
            text = prompt
   
        completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a helpful assistant for summarizing text. Make bullet points and split the text into important parts. Do not add any extra formatting such as headers (###), bold text, - or special characters."},
                {
                    "role": "user",
                    "content": text
                }
            ]
        )

        summary_text = completion.choices[0].message.content.strip()

        summary = [line.strip() for line in summary_text.split('\n') if line.strip()]

        return render_template('index.html', summary=summary)

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)