import discord, json, time
from discord.ext import commands
from functions import if_abfragen
c = open("BotFiles/config.json")
json_data = json.load(c)
token = json_data["token"]
intents = discord.Intents.all()
client = discord.Client()
bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

@bot.command()
async def test(ctx):
    await ctx.send('!test')

@bot.command(hidden=True)
async def clear(ctx, number):
    messages = await ctx.channel.history(limit=int(number)).flatten()
    for message in messages:
        await message.delete()


bot.run(token)
#client = MyClient(intents=intents)
#client.run(token)