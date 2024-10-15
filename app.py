from flask import Flask, render_template, request
from openai import OpenAI
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)

client = OpenAI(api_key='YOUR API KEY')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        prompt = request.form['prompt']

        completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a helpful assistant for summarizing text. Make bullet points and split the text for important parts"},
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        summary = completion.choices[0].message.content
        print(summary)
        return render_template('index.html', summary=summary)

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)