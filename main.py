import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
print('Barisbaba')

from discord.voice_client import VoiceClient

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')


startup_ext = ['musicUtil']

bot = commands.Bot('.')

@bot.event
async def on_ready():
    print('Bot ready')

class main_commands():
    def __init__(self,bot):
        self.bot = bot

@bot.command(pass_context=True)
async def sa(ctx):
    await ctx.send("as")

if __name__ == '__main__':
    for ext in startup_ext:
        try:
            bot.load_extension(ext)
        except Exception as e:
            print('failed to load ext  ', e)


bot.run(TOKEN)
