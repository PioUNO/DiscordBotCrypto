import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
from Utilidades import preciobtc
from Utilidades import precioeth
from Utilidades import inflaciontotal

load_dotenv()
cliente = discord.Client()
TOKEN = os.getenv('DISCORD_TOKEN')
bot = commands.Bot(command_prefix='!') #el prefix

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Streaming(name="Live Price For Crypto", url="http://www.twitch.tv/"))
    print("el bot {0.user} esta funcionando".format(bot))


@bot.command()
async def ping(ctx, arg=None):
        if arg == "ping":
            await ctx.send("pong")

        else:
            await ctx.send(f'tu ping actual es de {round(bot.latency * 1000)} ms')


@bot.command()
async def bitcoin(ctx):
    await ctx.send("BTC {} USD".format(preciobtc))


@bot.command()
async def ethereum(ctx):
    await ctx.send("ETH {} USD {}/24h".format(precioeth, inflaciontotal))


bot.run(TOKEN)