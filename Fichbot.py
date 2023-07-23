import discord, json, time
from discord.ext import commands
from functions import command_selection
from discord.ext import slash
c = open("BotFiles/config.json")
json_data = json.load(c)
token = json_data["token"]
intents = discord.Intents.all()
bot = slash.slashBot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

@bot.slash_cmd()
async def test(ctx):
    await ctx.send('!test')

@bot.slash_cmd(hidden=True)
async def clear(ctx, number):
    messages = await ctx.channel.history(limit=int(number)).flatten()
    for message in messages:
        await message.delete()


bot.run(token)
#client = MyClient(intents=intents)
#client.run(token)