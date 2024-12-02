import discord
import requests
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from discord.ext import commands
import os
import pytz
import random

# Config from environment variables
TOKEN = os.getenv('DISCORD_BOT_TOKEN')  # Quotify's token
GUILD_ID = int(os.getenv('GUILD_ID'))  # Server ID
CHANNEL_ID = int(os.getenv('CHANNEL_ID'))  # Channel ID
API_NINJAS_KEY = os.getenv('API_NINJAS_KEY')  # API Ninjas key

# Listing categories of the quotes
categories = ['education', 'success']

# Function to get a study motivational quote from API Ninjas
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

# Function to generate random colors for embeds
def random_color():
    return discord.Color.random()

# Set up the bot with intents
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='.', intents=intents)
scheduler = AsyncIOScheduler()

@bot.event
async def on_ready():
    print(f'Bot is ready. Logged in as {bot.user}')  # Logging in!
    schedule_daily_quote()

# Function to send daily quotes in an embed
async def send_daily_quote():
    channel = bot.get_guild(GUILD_ID).get_channel(CHANNEL_ID)
    if channel:
        quote = get_study_quote()  # Fetch a random study motivational quote
        embed = discord.Embed(
            title="📚 Study Motivation of the Day",
            description=quote,
            color=random_color()
        )
        embed.set_image(url="https://i.pinimg.com/564x/36/ef/39/36ef397f3c989d2c642789d7bc6eeb5e.jpg")

        await channel.send(embed=embed)

# Schedule the daily quote at a specific IST time (7:00 AM)
def schedule_daily_quote():
    ist = pytz.timezone('Asia/Kolkata')
    scheduler.add_job(send_daily_quote, 'cron', hour=7, minute=0, timezone=ist)
    scheduler.start()

# Command to say hi with an embed
@bot.command(name='hi')
async def greet(ctx):
    embed = discord.Embed(
        title="👋 Hello!",
        description="I'm Quotify! What's Up?!",
        color=random_color()
    )
    await ctx.send(embed=embed)

# Command to get a random study motivational quote
@bot.command(name='quote')
async def quote(ctx):
    quote_text = get_study_quote()
    embed = discord.Embed(
        title="📚 Motivational Quote",
        description=quote_text,
        color=random_color()
    )
    await ctx.send(embed=embed)

# Command to send an encouraging message
@bot.command(name='encourage')
async def encourage(ctx):
    messages = [
        "You've got this! Keep pushing forward!",
        "Remember, progress takes time. Keep studying!",
        "Believe in yourself! You're closer than you think.",
        "Every small step counts. Keep moving forward!",
        "Mistakes are proof that you are trying. Keep going!",
        "Hard work always pays off. Stay consistent!",
        "Your potential is limitless. Keep striving!",
        "Success is the result of preparation and determination.",
        "Stay positive and focused on your goals!"
    ]
    message = random.choice(messages)
    embed = discord.Embed(
        title="🌟 Encouragement",
        description=message,
        color=random_color()
    )
    await ctx.send(embed=embed)

# Run the bot
bot.run(TOKEN)

