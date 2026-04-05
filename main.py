# made with <3 from pluto
import discord
from discord.ext import commands
from discord import app_commands
from dotenv import load_dotenv
import os
import random
import giphy_client
from giphy_client.rest import ApiException


load_dotenv()
token = os.getenv('token')
api_key = os.getenv('api_key')
bot = commands.Bot(command_prefix='$', intents=discord.Intents.all())

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    try:
        synced = await bot.tree.sync()
        print(f'Synced commands!')
    except Exception as e:
        print(e)
#ping pong
@bot.tree.command(name = 'ping')
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message(f'pong')

#Heads or tails
@bot.tree.command(name = 'coinflip')
async def coinflip(interaction: discord.Interaction):
    o = ['Heads', 'Tails']
    output = random.choice(o)
    await interaction.response.send_message(f'The coin landed on {output}')


#send astolfo pic :3
@bot.tree.command(name = 'astolfo')
async def astolfo(interaction: discord.Interaction):
    await interaction.response.send_message(f'http://fateextellalink.com/characters/astolfo/images/astolfo.png')

#uhnime
@bot.command(name = 'gif')
async def gif(ctx,*,q="Anime"):
    api_instance = giphy_client.DefaultApi()
    try:
        api_response = api_instance.gifs_search_get(api_key, q, limit=5, rating='g')
        lst = list(api_response.data)
        giff = random.choice(lst)

        embed = discord.Embed(title=q)
        embed.set_image(url=f"https://media.giphy.com/media/{giff.id}/giphy.gif")

        await ctx.channel.send(embed=embed)
    except ApiException as r:
        print("Exception from api")

#start bot
bot.run(token)
