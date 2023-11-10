import discord, json, time
from discord import default_permissions
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
    print(f'{bot.user} has connected to Discord!')

@bot.event
async def on_raw_reaction_add(reaction):
    await command_selection.verificationReaction(bot, reaction, False)

@bot.event
async def on_raw_reaction_remove(reaction):
    await command_selection.verificationReaction(bot, reaction, True)

@bot.slash_command(description="Sends the bot's latency.") # this decorator makes a slash command
async def ping(ctx): # a slash command will be created with the name "ping"
    await ctx.respond(f"Pong! Latency is {round(bot.latency * 10 ** 3, 3)}ms")

@bot.slash_command(role='Fisch')
@default_permissions(administrator=True)
async def sync(ctx):
    "Reloads all slash commands and synces them."
    print("\nReloading Commands...")
    await ctx.respond("Reloading Commands...", ephemeral=True)
    await command_selection.if_ready(bot)

@bot.slash_command(description="Just a Test Command")
@default_permissions(administrator=True)
async def test(ctx):
    await ctx.respond('!test')

bot.run(token)
#client = MyClient(intents=intents)
#client.run(token)