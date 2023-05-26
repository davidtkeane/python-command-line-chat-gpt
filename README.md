# python-command-line-chat-gpt

ChatGPT is a Python script that uses the OpenAI API to generate responses based on user input on the command line. This script can be used to create chatbots or conversational agents for a variety of purposes.

## Readme.md

😃

# ChatGPT

ChatGPT is a Python script that uses the OpenAI API to generate responses based on user input. This script can be used to create chatbots or conversational agents for a variety of purposes.

## Installation

1. Clone the repository: `git clone https://github.com/davidtkeane/python-command-line-chat-gpt.git`
2. Install the required dependencies using pip: `pip install -r requirements.txt`
3. Add your own OpenAi API key to your .env file, but first rename test.env to .env to make this work.`https://platform.openai.com/` 
4. Free for a certain time, then 5 Euros a month, but I have had this for a few months now and I have only clocked up €1.87 cents so far. I use `https://chat.openai.com/` for most work, but love using my terminal and console! 
5. Go run the file, see below. 🍔

## Usage

To start a conversation with the chatbot, run the following command:
`python chatgpt.py`

1. When you first run the file it will create a new chatgpt-chat.txt file where all of the questions you have asked will be sent to the txt file for reference later on. 

The script will prompt you for input and generate a response based on your input. To end the conversation, type "no" or "nothing".

## Improvements

Here are a few suggestions for improving the script: 

- Add error handling to gracefully handle API errors or other issues.
- Implement a caching mechanism to reduce API usage and improve response times.
- Add more options for configuring the OpenAI API parameters, such as temperature, max_tokens, and top_p.
- Implement a GUI or web interface for the chatbot instead of a command-line interface.

## Requirements.txt

Here is the requirements.txt file that includes the necessary modules for running the script:

```
openai
dotenv
requests

ATA - I had to manually type pip3 install openai as I was getting an error even when i used pip install -r requirements.txt 
```
