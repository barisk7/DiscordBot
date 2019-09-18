import os
import discord

from dotenv import load_dotenv

load_dotenv()
token = os.getenv('NjIzOTYyNDkyMjEyNjA5MDQ0.XYKOhg.MhiMX8ky5BtF4KkTazz-GrjZn9c')
client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

client.run(token)