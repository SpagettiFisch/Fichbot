import discord, json, time
from discord.ext import commands
from functions import command_selection
from discord.ext import slash
c = open("BotFiles/config.json")
json_data = json.load(c)
token = json_data["token"]
intents = discord.Intents.all()
bot = slash.SlashBot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print('Starting Bot')
    await command_selection.if_ready(bot, commands, slash)

@bot.slash_cmd()
async def test(ctx: slash.Context):
    "Just a Test Command"
    await ctx.respond('!test')

"""
@bot.slash_cmd(hidden=True)
async def clear(ctx: slash.Context, number: slash.Option(description='Number of messages to clear', required=True)):
    "Can clear a specific number of messages in the used channel"
    messages = await ctx.channel.history(limit=int(number)).flatten()
    for message in messages:
        await message.delete()
"""


bot.run(token)
#client = MyClient(intents=intents)
#client.run(token)