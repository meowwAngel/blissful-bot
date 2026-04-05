# made with <3 by pluto
import discord
from discord.ext import commands
from discord import app_commands
from dotenv import load_dotenv
import os
import random

load_dotenv()

token = os.getenv('token')
bot = commands.Bot(command_prefix='$', intents=discord.Intents.all())

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    try:
        synced = await bot.tree.sync()
        print(f'Synced commands!')
    except Exception as e:
        print(e)

@bot.tree.command(name = 'ping')
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message(f'pong')

@bot.tree.command(name = 'coinflip')
async def coinflip(interaction: discord.Interaction):
    o = ['Heads', 'Tails']
    output = random.choice(o)
    await interaction.response.send_message(f'The coin landed on {output}')

@bot.tree.command(name = 'astolfo')
async def astolfo(interaction: discord.Interaction):
    await interaction.response.send_message(f'http://fateextellalink.com/characters/astolfo/images/astolfo.png')


bot.run(token)
