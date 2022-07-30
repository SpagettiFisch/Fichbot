import discord, json
from discord.ext import slash
commands = slash
from functions import command_selection as selection
c = open("BotFiles/config.json")
json_data = json.load(c)
token = json_data["token"]
intents = discord.Intents.all()
client = discord.Client()
bot = slash.SlashBot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    await selection.if_ready(bot, slash)
"""
@bot.event
async def on_message(message):
    await selection.if_message(message, bot)
"""
@bot.event
async def on_message_edit(before, after):
    await selection.if_edit(before, after, bot)

@bot.event
async def on_message_delete(message):
    await selection.if_delete(message, bot)

@bot.event
async def on_member_update(before, after):
    await selection.if_member_update(before, after, bot)

@bot.event
async def on_raw_reaction_add():
    await selection.if_reaction_add(bot)

@bot.event
async def on_interaction(interaction):
    interaction.reponse("test")

bot.run(token)