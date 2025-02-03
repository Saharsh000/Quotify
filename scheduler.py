#this is for sending the daily message at 7.00am IST..(will add a 12 hour cycle, dont worry lol. it takes time hehe
import pytz
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from utils import get_study_quote, random_color
import discord
import os

GUILD_ID = int(os.getenv('GUILD_ID'))
CHANNEL_ID = int(os.getenv('CHANNEL_ID'))

scheduler = AsyncIOScheduler()

async def send_daily_quote(bot):
    guild = bot.get_guild(GUILD_ID)
    if guild:
        channel = guild.get_channel(CHANNEL_ID)
        if channel:
            quote = get_study_quote()
            embed = discord.Embed(
                title="📚 Study Motivation of the Day",
                description=quote,
                color=random_color()
            )
            # Main image
            embed.set_image(url="https://i.pinimg.com/564x/36/ef/39/36ef397f3c989d2c642789d7bc6eeb5e.jpg")
            await channel.send(embed=embed)

def schedule_daily_quote(bot):
    ist = pytz.timezone('Asia/Kolkata')
    scheduler.add_job(lambda: send_daily_quote(bot), 'cron', hour=7, minute=0, timezone=ist)
    scheduler.start()
