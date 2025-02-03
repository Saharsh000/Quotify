
import discord
from utils import random_color

def register_greet(bot):
    @bot.command(name='hi')
    async def greet(ctx):
        embed = discord.Embed(
            title="👋 Hi there!",
            description="I'm Quotify! What's Up?!",
            color=random_color()
        )
        await ctx.send(embed=embed)
