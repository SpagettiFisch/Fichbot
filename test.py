import discord, json, time
c = open("BotFiles/config.json")
json_data = json.load(c)
token = json_data["token"]
intents = discord.Intents.all()
<<<<<<< Updated upstream
=======
#client = discord.Client()
bot = commands.Bot(command_prefix='!', intents=intents)
>>>>>>> Stashed changes

from discord.ext import slash
client = slash.SlashBot(
    # normal arguments to commands.Bot()
    command_prefix='!', description="whatever",
    # special option: modify all global commands to be
    # actually guild commands for this guild instead,
    # for the purposes of testing. Remove this argument
    # or set it to None to make global commands be
    # properly global - note that they take 1 hour to
    # propagate. Useful because commands have to be
    # re-registered if their API definitions are changed.
    debug_guild=828896352465190932,
    intents=intents
)

msg_opt = slash.Option(
    # description of option, shown when filling in
    description='Message to send',
    # this means that the slash command will not be invoked
    # if this argument is not specified
    required=True)

@client.slash_cmd() # global slash command
async def repeat( # command name
    ctx: slash.Context, # there MUST be one argument annotated with Context
    message: msg_opt
):
    """Make the bot repeat what you say""" # description of command
    # respond to the interaction, must be done within 3 seconds
    await ctx.respond(message) # string (or str()able) message

client.run(token)