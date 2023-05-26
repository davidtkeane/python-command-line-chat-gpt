#!/usr/bin/env python3
# Import modules
# This script enables you to search using ChatGPT on the command line

import openai
import os
import requests
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

# Set up the OpenAI API client
openai.api_key = os.getenv('OPENAI_API_KEY')

# Set up the model and prompt
model_engine = "text-davinci-003"

# Set up the file path
file_name = "chatgpt-chat.txt"
file_path = os.path.join(os.getcwd(), file_name)

# Set response until otherwise cancelled
prompt = input("🤖 How can I help you my Lord?\n")

def openai_create(prompt):
    response = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        temperature=0.9,
        max_tokens=2000,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.9,
        stop=[" Human:", " AI:"]
    )

    return response.choices[0].text

def chat(prompt):
    message = input(prompt)
    history = []
    while message.strip():
        response = openai_create(prompt + message)
        history.append((message, response))
        with open(file_path, "a") as f:
            f.write("Question: " + message + "\n")
            f.write("Response: " + response + "\n\n")
        message = input("🤖 What else can I help you with my Lord?\n")
    return history

# rememeber
def parse_file(file_name):
    file_data = open(file_name, 'r').readlines()
    data_dict = {}
    for line in file_data:
        question, answer = line.split(';')
        data_dict[question] = answer
    return data_dict
# remember

# Create file if it doesn't exist
if not os.path.exists(file_path):
    with open(file_path, "w") as f:
        f.write("Conversation Log\n")
        f.write("Created: " + str(datetime.now()) + "\n\n")

# Generate a response and save to file    
while prompt.lower() not in ("no", "n", "no!", "you can't", "you cant", "nothing"):
        # Generate a response
        completion = openai.Completion.create(
            engine=model_engine,
            prompt=prompt,
            max_tokens=2024,
            n=1,
            stop=None,
            temperature=0.9,
        )

        response = completion.choices[0].text
    
# Add conversation to file
        with open(file_path, "a") as f:
            f.write("Prompt: " + prompt + "\n")
            f.write("Time: " + str(datetime.now()) + "\n")
            f.write("Response: " + response + "\n\n")
            print("🤖 " + response + "\n")
        prompt = input("🤖 What else can I help you with my Lord?\n")

print("🤖...")
