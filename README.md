## Text Summarizer 📝

## Table of Contents

- [Demo](#demo)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [License](#license)

## Demo

https://github.com/user-attachments/assets/5de2d375-3f39-487a-b466-7663cf1d25a6

## Requirements
- Python 3.12 or later
- An OpenAI API key (for DALL-E)

## Installation
To run this project locally, follow these steps:

Setup Instructions
1. Clone the repository:

```
git clone https://github.com/z1ppyyy/text-summarizer.git
```

Navigate to the project directory:

```
cd text-summarizer
```

Paste your API KEY obtained from the https://platform.openai.com/
```
client = OpenAI(api_key='YOUR API KEY')
```

Run the application:

```
flask run
```

The app will be available at http://127.0.0.1:5000/.

## Usage
1. Open the browser and navigate to http://127.0.0.1:5000/.
2. Enter a prompt with your Text or Link you want to summarize 
3. Click on Summarize and wait for the AI to summarize.
4. The summary will be displayed below the input form.


## License
This project is licensed under the MIT License. See the LICENSE file for more details.
