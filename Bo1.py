import discord
from Bot import bot


client = discord.Client

@bot.event
async def on_message(message):
    message.content = message.content.lower()
    if message.author == client.user:
        return
    if message.content.startswith("hola"):
            await message.channel.send("como estas?")
