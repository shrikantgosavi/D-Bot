import os
import discord
import json
import requests
import urllib
import discord.ext
from keep_alive import keep_alive
from discord.ext import commands
#^ basic imports for other features of discord.py and python ^

client = discord.Client()

client = commands.Bot(command_prefix = '.') #put your own prefix here

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote =  json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)#to get random quote from API

def random_meme():
  url =  "https://some-random-api.ml/meme"
  response = urllib.request.urlopen(url)
  data = json.loads(response.read())
  path = data["image"]
  return path

def github_search_user(ctx, user_name_to_search): #to search user on github
  response = urllib.request.urlopen("https://api.github.com/users/" + user_name_to_search )
  data = json.loads(response.read())
  github_url = data["html_url"]
  github_avatar = data["avatar_url"]
  github_resource = [github_url,github_avatar]
  return github_resource

@client.event
async def on_ready():
    print("Dbot is online") #will print "bot online" in the console when the bot is online
    
@client.command() 
async def ping(ctx):
    await ctx.send('Pong!!') #simple command so that when you type "!ping" the bot will respond with "pong!"

@client.event #to welcome the people joining the Server
async def on_member_join(member):
    print(f'{member}has joined a server.') 

@client.event #to display if someone has left the server
async def on_member_remove(member):
    print(f'{member}has left a server.')  

@client.command() 
async def kick(ctx, member : discord.Member):
    try:
        await member.kick(reason=None)
        await ctx.send("kicked "+member.mention) #simple kick command to demonstrate how to get and use member mentions
    except:
        await ctx.send("bot does not have the kick members permission!")

@client.command() 
async def inspire(ctx):#shows a random quote
    quote = get_quote()
    await ctx.channel.send(quote)   

@client.command() 
async def meme(ctx):
    Meme = random_meme()
    await ctx.channel.send(Meme)

@client.command() 
async def github_search(ctx, user_name_to_search):
    github = github_search_user(ctx, user_name_to_search)
    await ctx.channel.send(github)
 
@client.command() 
async def tech_team(ctx):
    await ctx.channel.send(">>>> \n**GDSC GESCOENGG TECHNICAL TEAM** \n\n Om Gurav \n Nilesh Chinchole \n Vaishnavi Date \n Shrikant Gosavi \n Komal Patil") 

@client.command() 
async def event_team(ctx):
    await ctx.channel.send(">>> \n**GDSC GESCOENGG EVENTS TEAM** \n\n Aniket Kote \n Aashutosh Chandratre \n Parth Parmar") 

@client.command() 
async def lead(ctx):
    await ctx.channel.send(">>> \n**GDSC GESCOENGG LEAD** \n\n Atharva Chandwadkar") 
keep_alive()
client.run(os.getenv('TOKEN'))