# python-command-line-chat-gpt

ChatGPT is a Python script that uses the OpenAI API to generate responses based on user input on the command line. This script can be used to create chatbots or conversational agents for a variety of purposes.

## Readme.md

<h1 align="center">Hi, guys! <img src="https://github.com/FujiwaraChoki/FujiwaraChoki/blob/main/assets/238178097-766d336d-b87d-44ba-807c-c51de2bc6b4d.gif" width="28px" alt="👋"></h1>

![PowerShell](https://img.shields.io/badge/-PowerShell-black?style=flat-square&logo=powershell)

![GitHub last commit](https://img.shields.io/github/last-commit/davidtkeane/jervis-ChatGPT?style=flat-square)
![GitHub issues](https://img.shields.io/github/issues-raw/davidtkeane/jervis-ChatGPT?style=flat-square)

<b>Languages</b>

[![Python](https://img.shields.io/badge/python-black?style=for-the-badge&logo=python)](https://github.com/davidtkeane)

<b>OS</b>

[![Linux](https://img.shields.io/badge/linux-black?style=for-the-badge&logo=Linux)](https://github.com/davidtkeane)
[![Windows](https://img.shields.io/badge/Windows-black?style=for-the-badge&logo=Windows)](https://github.com/davidtkeane)

<p align="center">
    <b>Welcome to ChatGPT on the command line uses with API!</b>
    <br>
    <br>
    <i>
        I'm Rangersmyth (internet name), and I'm currently learning Python and Bash coding.<br>
    <br>
    </i>
    <br>

<p align="center">
  <img src="https://count.getloli.com/get/@rangersmyth?theme=gelbooru" />
</p>

<div align="center">
<a href="https://github.com/davidtkeane" target="_blank">
<img src=https://img.shields.io/badge/github-%2324292e.svg?&style=for-the-badge&logo=github&logoColor=white alt=github style="margin-bottom: 5px;" />
</a>
<a href="https://twitter.com/davidtkeane" target="_blank">
<img src=https://img.shields.io/badge/twitter-%2300acee.svg?&style=for-the-badge&logo=twitter&logoColor=white alt=twitter style="margin-bottom: 5px;" />
</a>
<a href="https://linkedin.com/in/sami-hindi-b31435248/" target="_blank">
<img src=https://img.shields.io/badge/linkedin-%231E77B5.svg?&style=for-the-badge&logo=linkedin&logoColor=white alt=linkedin style="margin-bottom: 5px;" />
</a>
</div>

😃

# ChatGPT

ChatGPT is a Python script that uses the OpenAI API to generate responses based on user input. This script can be used to create chatbots or conversational agents for a variety of purposes.

## Installation

1. Clone the repository: `git clone https://github.com/davidtkeane/python-command-line-chat-gpt.git`
2. Install the required dependencies using pip: `pip install -r requirements.txt`
3. FYI - I had to manually type pip3 install openai and pip3 install direnv also as I was getting an error even when i used pip install -r requirements.txt 
4. Add your own OpenAi API key to your .env file, but first rename test.env to .env to make this work.`https://platform.openai.com/` 
5. Free for a certain time, then 5 Euros a month, but I have had this for a few months now and I have only clocked up €1.87 cents so far. I use `https://chat.openai.com/` for most work, but love using my terminal and console! 
6. Go run the file, see below. 🍔

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
```
