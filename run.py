## module import
from bs4 import BeautifulSoup
import discord, asyncio
import requests
## set based var
intents = discord.Intents().all()
client = discord.Client(intents=intents)
discord.Activity(name="Testing", type=5)
prefix = "" #write here custom prefix
bot = commands.Bot(command_prefix = prefix,intents=intents) ## this code based event is [bot]

@bot.event
async def on_ready():
    print(f'{bot.user} is during')## print if bot is successful run
# example command
@bot.command(name = "saying")
async def saying(ctx):
    url = 'https://zenquotes.io/api/random'## site url
    response = requests.get(url)#trans to appropriate url
    if response.status_code == 200:
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
    
    else: 
        print("code" + str(response.status_code))  
    code_in = response.text.split('"')## edit to print out
    ##set embed
    embed=discord.Embed(title= code_in[3], color=0xFFFFFF) 
    embed.set_footer(text= code_in[7])
    await ctx.channel.send(embed=embed)
    await ctx.message.delete()
