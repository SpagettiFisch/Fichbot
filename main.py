import discord
import random
import json
from discord.ext import commands
from discord.ext.commands import Bot
#from modules import wichtelbot
#from modules import reactionrole
import time

c = open("config.json")
json_data = json.load(c)
token = json_data["token"]
prefix = json_data["prefix"]


class MyClient(discord.Client):
    #einloggen
    async def on_ready(self):
        print("Ich habe mich eingeloggt. Beep Bop.")

    #Wenn Nachricht gepostet wird
    async def on_message(self, message):
        print(message)


        print("Nachricht von: " + str(message.author) + " enthält " + str(message.content))
        id = str(message).split(' ')[12]
        userID = id.split('=')[1]
        cid = str(message).split(' ')[3]
        ChannelID = cid.split('=')[1]
        react = random.randint(0,500)
        if message.author == client.user:
            return
        if str(message.author) == "Reyana#7046":
            await message.add_reaction("🍞")
        #react = 249
        if react == 249:
            if  int(ChannelID) != 789425205063581698:
                await message.add_reaction("🧐")
            pass
        if int(ChannelID) == 789425205063581698:
            if message.content.startswith(prefix):
                command = message.content.lower()
                if command.startswith(f'{prefix}help'):
                    await message.channel.send(f'``` {prefix}help - Zeigt diese Hilfe an \n {prefix}dice Zufallszahl von 0-100 \n {prefix}roulette <BID> - Startet das Roulette, BID= black/red/number ```')
                elif command.startswith(f"{prefix}dice"):
                    Zahl = random.randint(0, 100)
                    await message.channel.send("Du hast eine " + str(Zahl) + " gewürfelt")
                elif command.startswith(f"{prefix}credits"):
                    await message.author.send("`Dieser Bot wurde von SpagettiFisch programmiert`")
        #        if message.content.startswith("!stats"):
        #            messages = await message.channel.history(limit=50).flatten()
        #            for i in messages:
        #                print(i.content)
        #            counter = 0
        #            async for m in message.channel.history():
        #               if m.author == client.user and m.content == "Du hast verloren :(":
        #                    counter = counter + 1
        #            print(counter)
                elif command.startswith(f"{prefix}roulette "):
                    bid = message.content.split(' ')[1]
                    bid_param = -3
                    if bid.lower() == "black":
                        bid_param = -1
                    elif bid.lower() == "red":
                        bid_param = -2
                    else:
                        try:
                            bid_param = int(bid)
                        except:
                            bid_param = -3
                    if bid_param == -3:
                        await message.channel.send('Ungültige Eingabe')
                        return
                    result = random.randint(0, 36)
                    print(result)
                    if bid_param == -1:
                        won = result % 2 == 0 and not result == 0
                    elif bid_param == -2:
                        won = result % 2 == 1
                    else:
                        won = result == bid_param
                    if won:
                        await message.channel.send(f'Du hast gewonnen <@{userID}> :) ')
                    else:
                        await message.channel.send(f'Du hast verloren <@{userID}> :( ')
#                elif command.startswith(f"{prefix}prefix "):
#                    if int(userID) == 477352031561187328:
#                        neuer_Prefix = (f"{str(command.split(' ')[1])}")
#                    else:
#                        await message.channel.send(f"Du hast nicht die nötigen Rechte dafür <@{userID}>")
            else:
                await message.delete()




client = MyClient()
client.run(token)