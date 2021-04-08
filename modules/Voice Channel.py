import discord
import random
from discord.ext import commands
from discord.ext.commands import Bot
IDcategoryvoice = "782600229236244493"

bot = commands.Bot(command_prefix='!')

class MyClient(discord.Client):

    @bot.event
    async def on_ready(self):
        print("Ich habe mich eingeloggt. Beep Bop.")
        return

    @bot.event
    async def on_voice_state_update(self, member, before, after):
        print(before.channel)
        print(after.channel)
        channels = (member.guild.voice_channels)

        emptychannels = False
        cpchannel = channels[0]
        for j in channels:
            if j.category.id == IDcategoryvoice:  # Wenn Kategory richtig ist
                if not j.members:  # Wenn niemand im Channel ist
                    if not emptychannels:  # Wenn emptychannel False ist
                        await j.delete()
#                    else:  # Wenn emptychannel True ist
#                        await j.delete()
                cpchannel = j
        if not emptychannels:
            await cpchannel.clone(name="Channel")



client = MyClient()
client.run("NzMwNDA2MjQ2NDc3NDYzNTUz.XwXB0w.0yFe_YFn5sZg00Z_bSlGaK4JQ9I")