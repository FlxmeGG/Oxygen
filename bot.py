import os
import asyncio
import discord
from dotenv import load_dotenv
from discord.ext import commands

#Load dotenv
load_dotenv()

#Initialize the bot
intents = discord.Intents.all()
bot = commands.Bot(intents=intents)

#Load the commands/extensions
commands = [
  'commands.utils.ping'
]

if __name__=='__main__':
  for command in commands:
    bot.load_extension(command)

@bot.event
async def on_ready():
  print(f"Logged in to discord as {bot.user}")

bot.run(os.getenv('TOKEN'))
