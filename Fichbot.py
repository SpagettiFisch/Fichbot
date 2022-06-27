import discord, json
from discord.ext import commands
from functions import command_selection as selection
c = open("BotFiles/config.json")
json_data = json.load(c)
token = json_data["token"]
intents = discord.Intents.all()
client = discord.Client()
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    await selection.if_ready(bot)

@bot.event
async def on_message(message):
    await selection.if_message(message, bot)

@bot.event
async def on_message_edit(before, after):
    await selection.if_edit(before, after, bot)

@bot.event
async def on_message_delete(message):
    await selection.if_delete(message, bot)

@bot.event
async def on_member_update(before, after):
    await selection.if_member_update(before, after, bot)

@bot.command()
async def test(ctx):
    await ctx.send('!test')

@bot.command(hidden=True)
async def clear(ctx, number):
    messages = await ctx.channel.history(limit=int(number)).flatten()
    for message in messages:
        await message.delete()

bot.run(token)