import discord
import requests
from discord.ext import commands
from utils import random_color
#necessary modules.. lol

def get_random_fact():
    try:
        response = requests.get("https://uselessfacts.jsph.pl/random.json?language=en")
        if response.status_code == 200:
            data = response.json()
            return data.get("text", "Here's a fun fact for you!")
        else:
            return "Sorry, I couldn't fetch a fun fact right now."
    except Exception:
        return "Something went wrong while fetching a fact!"

def register_greet(bot):
    @bot.command(name='hi')
    async def greet(ctx):
        fact = get_random_fact()
        embed = discord.Embed(
            title="👋 Hi there!",
            description=f"I'm Quotify!! \n By the way, Here's a fun fact for you:\n\n*{fact}*", #actual reply the bot gives..
            color=random_color()
        )
        await ctx.send(embed=embed)

