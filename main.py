# Made with <3 by pluto
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
async def gif(ctx,*,q="catgirl"):
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
#uhnime / command
@bot.tree.command(name='gif')
async def gif(interaction: discord.Interaction, q: str = "catgirl"):
    api_instance = giphy_client.DefaultApi()
    try:
        api_response = api_instance.gifs_search_get(api_key, q, limit=5, rating='g')
        lst = list(api_response.data)
        giff = random.choice(lst)
        embed = discord.Embed(title=q)
        embed.set_image(url=f"https://media.giphy.com/media/{giff.id}/giphy.gif")
        await interaction.response.send_message(embed=embed)
    except ApiException as r:
        print("Exception from api")
#rawr
@bot.tree.command(name = 'rawr')
async def rawr(interaction: discord.Interaction):
    await interaction.response.send_message('https://tenor.com/bFGYi.gif')

@bot.tree.command(name = 'meow')
async def meow(interaction: discord.Interaction):
    await interaction.response.send_message('https://tenor.com/8ijz.gif')
@bot.tree.command(name = 'freaky')
async def freaky(interaction: discord.Interaction):
    await interaction.response.send_message('https://tenor.com/view/freaky-cat-cat-freaky-cat-freaky-tongue-freaky-cat-tongue-freaky-tongue-gif-11560619178986255398')
@bot.command(name = 'rawr')
async def rawr(ctx):
    await ctx.channel.send('https://tenor.com/bFGYi.gif')
@bot.command(name = 'meow')
async def meow(ctx):
        await ctx.channel.send('https://tenor.com/8ijz.gif')
@bot.command(name = 'freaky')
async def freaky(ctx):
        await ctx.channel.send('https://tenor.com/view/freaky-cat-cat-freaky-cat-freaky-tongue-freaky-cat-tongue-freaky-tongue-gif-11560619178986255398')
@bot.tree.command(name = 'license')
async def license(interaction: discord.Interaction):
    await interaction.response.send_message('https://github.com/OpenPluto/blissful-bot/blob/main/LICENSE')
@bot.command(name = 'license')
async def license(ctx):
    await ctx.channel.send('https://github.com/OpenPluto/blissful-bot/blob/main/LICENSE')
#help
@bot.tree.command(name = 'help')
async def help(interaction: discord.Interaction):
    embed = discord.Embed(title="Blissful Bot Commands", description="Here are the available commands for Blissful Bot:")
    embed.add_field(name="/ping", value="Responds with 'pong'", inline=False)
    embed.add_field(name="/coinflip", value="Flips a coin and returns Heads or Tails", inline=False)
    embed.add_field(name="/astolfo", value="Sends a picture of Astolfo", inline=False)
    embed.add_field(name="/gif [query]", value="Searches for a GIF based on the provided query (default: catgirl)", inline=False)
    embed.add_field(name="/rawr", value="Sends a rawr cat GIF", inline=False)
    embed.add_field(name="/meow", value="Sends a meow cat GIF", inline=False)
    embed.add_field(name="/freaky", value="Sends a freaky cat GIF", inline=False)
    embed.add_field(name="/license", value="Provides a link to the bot's license on GitHub", inline=False)
    await interaction.response.send_message(embed=embed, ephemeral=True)
#start bot
bot.run(token)
