import discord
import os
import asyncio
from discord import app_commands
from discord.ext import commands
import config


#intents = discord.Intents.all()
#intents.message_content = True
bot = commands.Bot(command_prefix="!", intents = discord.Intents.all())



@bot.event
async def on_ready():
    print(f'Der Code ist eingeloggt als = {bot.user}')
    bot.loop.create_task(status_task())
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} command(s)")
    except Exception as e:
        print(e)
    print('_________________________________________________________')

async def status_task():
    while True:
        await bot.change_presence(activity=discord.Game('discord.gg/5HKT8vjGyz'), status=discord.Status.online)
        await asyncio.sleep(5)
        await bot.change_presence(activity=discord.Game('Programmiert von Freya'), status=discord.Status.online)
        await asyncio.sleep(5)


@bot.tree.command(name="testgreet", description="guckt ob der command funktioniert")
async def testgreet(interaction: discord.Interaction):    
    await interaction.response.send_message(f"Was geht {interaction.user.mention}", 
    ephemeral=True)

@bot.tree.command(name="say")
@app_commands.describe(args = "Was soll ich wiederholen?")
async def say(interaction: discord.Interaction, args: str):
    await interaction.response.send_message(f"{interaction.user.name} said: `{args}`", 
    ephemeral=True)
       
@bot.tree.command(name="help", description="Zeigt dir Alle Commands die ich so Besitze")
async def help(interaction: discord.interactions):
    await interaction.response.send_message(f"Hier sind alle meine Commands: \n\ntestgreet = guckt ob der Bot on ist und reagiert \n\nSay = Wiederholt deine Text denn du in, denn Befehl schreibst",
    ephemeral=True)

@bot.tree.command(name="safespace", description="Mit diesem Befehl kommst du zu meinem Discord Server") 
async def safespace(interaction: discord.interactions,):
    await interaction.response.send_message(f"Heyo {interaction.user.name},\nWenn du meinem schönen Safespace beitretten möchtest dann bist du sehr gerne Willkommen, \nHier Wäre der link zu meinem DC = discord.gg/5HKT8vjGyz \n\n Vielleicht sehen wir uns ja mal dort",
    ephemeral=True)



bot.run(config.TOKEN)