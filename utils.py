# this is where the actual quote taking comes.. 
import discord
import requests
import random
import os

API_NINJAS_KEY = os.getenv('API_NINJAS_KEY')
categories = ['education', 'success']

def get_study_quote():
    url = 'https://api.api-ninjas.com/v1/quotes'
    category = random.choice(categories)
    params = {'category': category}
    headers = {'X-Api-Key': API_NINJAS_KEY}

    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        data = response.json()
        if data:
            return f"{data[0]['quote']} — {data[0]['author']}"
    return "Stay motivated and keep learning!"

def random_color():
    return discord.Color.random()
