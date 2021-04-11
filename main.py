import discord
import random
import json
import sys
import time

c = open("config.json")
json_data = json.load(c)
token = json_data["token"] #Token of the Discord Bot
prefix = json_data["prefix"] #Preifx for Bot Commands
Logs = json_data["Logs"] #1 is True, each other number is False
BotOwnerID = json_data["Bot_Owner_ID"] #ID of the person who can use all Bot Commands
CommandChannelID = json_data["Command_Channel_ID"] #the Channel ID for the most Bot Commands


class MyClient(discord.Client):

    #einloggen
    async def on_ready(self):
        print("Ich habe mich eingeloggt.")
        await client.change_presence(activity=discord.Game(name="an mir selbst verzweifeln"))


    #blacklist
    async def on_message(self, message):
        blacklist = ["hi", "gh"]
        for x in blacklist:
            if x in message.content:
                await message.delete()
            else:
                pass


    #Bot Commands
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
            if  int(ChannelID) != int(CommandChannelID):
                await message.add_reaction("🧐")
            pass
        if int(ChannelID) == int(CommandChannelID):
            if message.content.startswith(prefix):
                command = message.content.lower()
                if command.startswith(f'{prefix}help'):
                    await message.channel.send(f'``` {prefix}help - Zeigt diese Hilfe an \n {prefix}dice Zufallszahl von 0-100 \n {prefix}roulette <BID> - Startet das Roulette, BID= black/red/number ```')
                elif command.startswith(f"{prefix}dice"):
                    Zahl = random.randint(0, 100)
                    await message.channel.send("Du hast eine " + str(Zahl) + " gewürfelt")
                elif command.startswith(f"{prefix}credits"):
                    await message.author.send("`Dieser Bot wurde von SpagettiFisch programmiert`")
                elif command.startswith(f"{prefix}test"):
                    await message.channel.send(f"+dice")
                    await message.channel.send("!test")
                elif command.startswith(f"{prefix}stop"):
                    if int(userID) == int(BotOwnerID):
                        await message.channel.send("Ja wie denn? xD \nIch könnte das ja mal probie... ")
                        print("Ich geh dann mal offline")
                        await client.close()

                    else:
                        await message.channel.send(f"NIEMALS <@{userID}>")
                elif command.startswith(f"{prefix}start"):
                    if int(userID) == int(BotOwnerID):
                        await message.channel.send(f"{prefix}test")
                    else:
                        await message.channel.send(f"denk nicht mal dran <@{userID}>")
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
#            else:
#                await message.delete()


    #Logging
        if int(Logs) == 1:
            Nachricht = message.content
            Autor = message.author
            Channel = message.channel
            tempus = str(message.created_at).split(".")
            Guild = message.guild
            tempus.pop()
            Datum = str(tempus).split(" ")[0].replace("['", "")
            Zeit = str(tempus).split(" ")[1].replace("']", "")

            l = open("logs.txt", "a")
            l.writelines(f'{Autor} hat in {Channel}, auf dem Server {Guild} am {Datum} um {Zeit} "{Nachricht}" geschrieben. \n')
            l.close()


    async def on_message_edit(self, before, after):
        if int(Logs) == 1:
            if before.author != client.user:
                Nachricht_alt = before.content
                Nachricht_neu = after.content
                tempus = str(after.edited_at).split('.')
                tempus.pop()
                print(tempus)
                Datum = str(tempus).split(" ")[0].replace("['", "")
                Zeit = str(tempus).split(" ")[1].replace("']", "")

                l = open('logs.txt', 'a')
                l.writelines(f'{before.author} hat in {after.channel} auf {after.guild} am {Datum} um {Zeit} von "{Nachricht_alt}" zu "{Nachricht_neu}" bearbeitet. \n')
                l.close()







client = MyClient()
client.run(token)