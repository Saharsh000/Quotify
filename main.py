# main.py
import os
import discord
from discord.ext import commands
from scheduler import schedule_daily_quote
from dotenv import load_dotenv
import importlib.util
import pathlib

load_dotenv()

TOKEN = os.getenv('DISCORD_BOT_TOKEN')

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='.', intents=intents)

@bot.event
async def on_ready():
    print(f'Bot is ready. Logged in as {bot.user}')
    schedule_daily_quote(bot)

# Dynamically import and register commands from the commands directory.
commands_path = pathlib.Path('./commands')
for command_file in commands_path.glob('*.py'):
    module_name = command_file.stem
    spec = importlib.util.spec_from_file_location(module_name, command_file)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    
    # Each module should have a registration function.
    if module_name == 'greet' and hasattr(module, 'register_greet'):
        module.register_greet(bot)
    elif module_name == 'quote' and hasattr(module, 'register_quote'):
        module.register_quote(bot)
    elif module_name == 'encourage' and hasattr(module, 'register_encourage'):
        module.register_encourage(bot)
    elif module_name == 'emotion' and hasattr(module, 'register_emotion'):
        module.register_emotion(bot)

bot.run(TOKEN)


