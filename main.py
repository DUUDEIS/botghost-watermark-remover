import discord
import os
from discord.ext import commands

intents = discord.Intents.all()

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
    await bot.change_presence(activity=discord.Watching(name='NEX HOSTHING'))

bot.run('MTA2NjAyMjk0ODExMDA4MjE0OQ.GYVeQo.vLZig9ydUlsb5iuNMJcuadYPoGnnEMLUHa-K9o')
