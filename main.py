import discord, json, time
from functions import command_selection
c = open("BotFiles/config.json")
json_data = json.load(c)
token = json_data["token"]
intents = discord.Intents.all()
bot = discord.Bot(intents=intents)

@bot.event
async def on_ready():
    print('Starting Bot')
    await command_selection.if_ready(bot)

@bot.slash_command(description="Sends the bot's latency.") # this decorator makes a slash command
async def ping(ctx): # a slash command will be created with the name "ping"
    await ctx.respond(f"Pong! Latency is {round(bot.latency * 10 ** 3, 4)}ms")

@bot.slash_command(role='Fisch')
async def sync(ctx):
    "Reloads all slash commands and synces them."
    print("\nReloading Commands...", ephemeral=True)
    await ctx.respond("Reloading Commands...")
    await command_selection.if_ready(bot)

@bot.slash_command(description="Just a Test Command")
async def test(ctx):
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