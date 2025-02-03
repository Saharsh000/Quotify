#basic cmd for getting a quote
import discord
from discord.ext import commands
from utils import get_study_quote, random_color

def register_quote(bot):
    @bot.command(name='quote')
    async def quote(ctx):
        quote_text = get_study_quote()
        embed = discord.Embed(
            title="📚 Motivational Quote",
            description=quote_text,
            color=random_color()
        )
     
