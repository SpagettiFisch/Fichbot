import discord
import random
import json
import sys
import time
import requests

c = open("BotFiles/config.json")
json_data = json.load(c)
token = json_data["token"] #Token of the Discord Bot
prefix = json_data["prefix"] #Preifx for Bot Commands
Logs = json_data["Logs"] #1 is True, each other number is False
BotOwnerID = json_data["Bot_Owner_ID"] #ID of the person who can use all Bot Commands
CommandChannelID = json_data["Command_Channel_ID"] #the Channel ID for the most Bot Commands
VerifyMessageID = json_data["Verify_Message_ID"] #the message ID used for reaction verification
VerifyChannelID = json_data["Verify_Channel_ID"] # the Channel ID used for reaction verification
b = open("BotFiles/Blacklist", "r")

#blacklist
async def blacklist(self, message, userID, command):
    print(1)
    count = 0
    for x in b:
        count += 1
        if x.replace('\n', '') in command:
            await message.delete()
            print("gelöscht")
#            if count == 1:
#                await message.channel.send(f"<@{userID}> hat das N-Wort benutzt. STEINIGT IHN!")
        else:
            pass


class MyClient(discord.Client):

    #einloggen
    async def on_ready(self):
        print("Ich habe mich eingeloggt.")
        #change Status
        s = open("BotFiles/status", "r")
        Status = s.read()
        try:
            if str(Status).lower().split("_", 3)[1] == "game":
                await client.change_presence(
                    activity=discord.Game(name=f"{str(Status).split('_', 2)[2]}"))

            elif str(Status).lower().split("_", 3)[1] == "stream":
                await client.change_presence(
                    activity=discord.Streaming(name=f"{str(Status).split('_', 5)[2]}",
                                               url=f"{str(Status).split('_', 5)[3]}"))

            elif str(Status).lower().split("_", 3)[1] == "listen":
                await client.change_presence(
                    activity=discord.Activity(type=discord.ActivityType.listening,
                                              name=f"{str(Status).split('_', 5)[2]}"))

            elif str(Status).lower().split("_", 3)[1] == "watch":
                await client.change_presence(
                    activity=discord.Activity(type=discord.ActivityType.watching,
                                              name=f"{str(Status).split('_', 5)[2]}"))
        except:
            print("Ungültiger Status")
            pass
        s.close()
        try:
            Person = await client.fetch_user()
            while True:
                await Person.send("ping")
        except:
            pass

    async def on_message(self, message):
        id = str(message).split(' ')[12]
        userID = id.split('=')[1]
        cid = str(message).split(' ')[3]
        ChannelID = cid.split('=')[1]
        react = random.randint(0, 500)
        command = message.content.lower()
        await blacklist(self, message, userID, command)


    #Bot Commands
        if message.author == client.user:
            return
        elif str(message.author) == "Reyana#7046":
            await message.add_reaction("🍞")
        #react = 249
        elif react == 249:
            if  int(ChannelID) != int(CommandChannelID):
                await message.add_reaction("🧐")
            pass
        elif message.content.startswith(prefix):

            #not Chat Commands
            if int(ChannelID) == int(CommandChannelID):
                if command.startswith(f'{prefix}help'):
                    await message.channel.send(f'``` {prefix}help - Zeigt diese Hilfe an \n {prefix}dice <Zahl 1>,<Zahl 2> würfelt eine Zahl von Zahl 1 bis Zahl 2 \n {prefix}roulette <BID> - Startet das Roulette, BID= black/red/number ```')
                elif command.startswith(f"{prefix}credits"):
                    await message.author.send("`Dieser Bot wurde von SpagettiFisch programmiert`")

                #Owner Commands
            elif int(ChannelID) == int(830343228502048808) or str(message.channel) == "Direct Message with SpagettiFisch#8888":
                if int(userID) == int(BotOwnerID):
                    if message.content.startswith(f"{prefix}status"):
                        s = open("BotFiles/status", "w")
                        try:
                            if str(message.content).lower().split("_", 3)[1] == "game":
                                await client.change_presence(
                                    activity=discord.Game(name=f"{str(message.content).split('_', 2)[2]}"))
                                if not "Direct Message with" in str(message.channel):
                                    await message.delete()
                                await message.channel.send("Status geändert")
                                s.writelines(message.content)

                            if str(message.content).lower().split("_", 3)[1] == "stream":
                                await client.change_presence(
                                    activity=discord.Streaming(name=f"{str(message.content).split('_', 5)[2]}",
                                                               url=f"{str(message.content).split('_', 5)[3]}"))
                                if not "Direct Message with" in str(message.channel):
                                    await message.delete()
                                await message.channel.send("Status geändert")
                                s.writelines(message.content)

                            if str(message.content).lower().split("_", 3)[1] == "listen":
                                await client.change_presence(
                                    activity=discord.Activity(type=discord.ActivityType.listening,
                                                              name=f"{str(message.content).split('_', 5)[2]}"))
                                if not "Direct Message with" in str(message.channel):
                                    await message.delete()
                                await message.channel.send("Status geändert")
                                s.writelines(message.content)

                            if str(message.content).lower().split("_", 3)[1] == "watch":
                                await client.change_presence(
                                    activity=discord.Activity(type=discord.ActivityType.watching,
                                                              name=f"{str(message.content).split('_', 5)[2]}"))
                                if not "Direct Message with" in str(message.channel):
                                    await message.delete()
                                await message.channel.send("Status geändert")
                                s.writelines(message.content)

                        except:
                            embed = discord.Embed(title="!status `<option>`", colour=discord.Colour(0xbef134))
                            embed.add_field(name="game", value="`!status_game_<custom game name>`", inline=False)
                            embed.add_field(name="stream", value="`!status_stream_<custum Stream Name>`_`<Stream URL>`",
                                            inline=False)
                            embed.add_field(name="listen", value="`!status_listen_<custon song name>`", inline=False)
                            embed.add_field(name="watch", value="`!status_watch_<custom video name>`", inline=False)
                            embed.add_field(name="auto", value="!status auto", inline=False)

                            await message.channel.send(embed=embed)
                        s.close()
                    elif command.startswith(f"{prefix}stop"):
                        if int(userID) == int(BotOwnerID):
                            await message.channel.send("Ja wie denn? xD \nIch könnte das ja mal probie... ")
                            print("Ich geh dann mal offline")
                            client.clear()
                            await client.close()
                            await sys.exit()
                        else:
                            await message.channel.send(f"NIEMALS <@{userID}>")
                    elif command.startswith(f"{prefix}test"):
                        await message.channel.send(f"+dice")
                        await message.channel.send("!test")
                    elif command.startswith(f"{prefix}start"):
                        if int(userID) == int(BotOwnerID):
                            await message.channel.send(f"{prefix}test")
                        else:
                            await message.channel.send(f"denk nicht mal dran <@{userID}>")
                    elif command.startswith(f"{prefix}dm"):
                        Person = await client.fetch_user(command.split('+')[1])
                        Nachricht = message.content.split('+')[2]
                        await Person.send(Nachricht)
                        if not "Direct Message with" in str(message.channel):
                            await message.delete()
                    elif command.startswith(f"{prefix}ki"):
                        Channel = await client.fetch_channel(command.split('+')[1])
                        Nachricht = message.content.split('+')[2]
                        await Channel.send(Nachricht)
                        if not "Direct Message with" in str(message.channel):
                            await message.delete()

            #Chat Commands
            elif command.startswith(f"{prefix}witz"):
                witz = requests.get("https://v2.jokeapi.dev/joke/Any?lang=de&format=txt&type=twopart")
                witz = witz.text
                witz = witz.splitlines()
                witz = [witz[0], witz[2]]
                witz = str(witz).replace("['", "").replace("']", "")
                await message.channel.send(witz.replace("', '", ""))
            elif command.startswith(f"{prefix}dice "):
                Zahlen = command.split(' ')[1]
                Zahl1 = Zahlen.split(',')[0]
                Zahl2 = Zahlen.split(',')[1]
                Zahl = random.randint(int(Zahl1), int(Zahl2))
                await message.channel.send(f"Du hast eine {Zahl} gewürfelt")
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
            #Links
            elif command.startswith(f"{prefix}github"):
                await message.channel.send("Hier geht es zum Github Profil von SpagettiFisch: https://github.com/SpagettiFisch")
            elif command.startswith(f"{prefix}fichbot"):
                await message.channel.send("Das bin ich. Was gibt es? Um zu sehen, was ich alles tolles kann, schreib einfach !help")
                time.sleep(3)
                await message.channel.send("Meinen Code findest du natürlich auch auf Github: https://github.com/SpagettiFisch/Fichbot")
            elif command.startswith(f"{prefix}twitch"):
                await message.channel.send("Falls er irgendwann mal streamen sollte, wirst du ihn hier finden: https://www.twitch.tv/spagettifisch2")
            elif command.startswith(f"{prefix}ston"):
                await message.channel.send("Das ist ein ganz einsamer Stein, besuch ihn doch mal ;) https://www.twitch.tv/der_ston")
            elif command.startswith(f"{prefix}slumpfus"):
                await message.channel.send("Geht mal zum lieben Slumpfus rüber, lasst einen Follow und Liebe da, dann kann der Fisch endlich seine Bits loswerden^^ https://www.twitch.tv/slumpfus")



    #Logging
        if int(Logs) == 1:
            Nachricht = message.content
            Autor = message.author
            Channel = message.channel
            tempus = str(message.created_at).split(".")
            Guild = message.guild
            tempus.pop()
            try:
                Datum = str(tempus).split(" ")[0].replace("['", "")
                Zeit = str(tempus).split(" ")[1].replace("']", "")
                l = open("BotFiles/logs.txt", "a")
                l.writelines(f'\n{Autor} hat in {Channel}, auf dem Server {Guild} am {Datum} um {Zeit} "{Nachricht}" geschrieben.')
                l.close()
            except:
                l = open("BotFiles/logs.txt", "a")
                l.writelines(f'\nFEHLER "{Nachricht}" von {Autor}')
                l.close()

    async def on_message_delete(self, message):
        print(message)
        if int(Logs) == 1:
            Nachricht = message.content
            Autor = message.author
            Channel = message.channel
            tempus = str(message.created_at).split(".")
            Guild = message.guild
            tempus.pop()
            Datum = str(tempus).split(" ")[0].replace("['", "")
            Zeit = str(tempus).split(" ")[1].replace("']", "")
            try:

                l = open("BotFiles/logs.txt", "a")
                l.writelines(
                    f'\n{Autor} hat in {Channel}, auf dem Server {Guild} am {Datum} um {Zeit} "{Nachricht}" geschrieben.')
                l.close()
            except:
                l = open("BotFiles/logs.txt", "a")
                l.writelines(
                    f'FEHLER "\n{Nachricht}" von {Autor}')
                l.close()


    async def on_message_edit(self, before, after):
        if int(Logs) == 1:
            if before.author != client.user:
                Nachricht_alt = before.content
                Nachricht_neu = after.content
                try:

                    tempus = str(after.edited_at).split('.')
                    tempus.pop()
                    Datum = str(tempus).split(" ")[0].replace("['", "")
                    Zeit = str(tempus).split(" ")[1].replace("']", "")
                    l = open('BotFiles/logs.txt', 'a')
                    l.writelines(f'\n{before.author} hat in {after.channel} auf {after.guild} am {Datum} um {Zeit} von "{Nachricht_alt}" zu "{Nachricht_neu}" bearbeitet.')
                    l.close()
                except:
                    l = open("BotFiles/logs.txt", "a")
                    l.writelines(
                        f'\nFEHLER(BEARBEITET) "{Nachricht_neu}" von {before.author}')
                    l.close()


    #Verification
    async def on_raw_reaction_add(self, reaction):
        guild = client.get_guild(reaction.guild_id)
        user = reaction.member
        member = user
        ReactionMessageID = str(reaction).split(' ')[1].split('=')[1]

        if int(ReactionMessageID) != int(VerifyMessageID):
            return

        elif reaction.channel_id != int(VerifyChannelID):
            print("falscher Channel")
            return

        elif user != client.user:
            if str(reaction.emoji) == "🖥":
                await member.add_roles(discord.utils.get(guild.roles, name="Mortus"))
            elif str(reaction.emoji) == "🤖":
                await member.add_roles(discord.utils.get(guild.roles, name="Bot"))
            elif str(reaction.emoji) == "🫂":
                await member.add_roles(discord.utils.get(guild.roles, name="Mensch... vielleicht.."))
            else:
                return


    async def on_raw_reaction_remove(self, reaction):
        guild = client.get_guild(reaction.guild_id)
        member = await guild.fetch_member(int(reaction.user_id))
        user = await client.fetch_user(int(reaction.user_id))
        ReactionMessageID = str(reaction).split(' ')[1].split('=')[1]

        if int(ReactionMessageID) != int(VerifyMessageID):
            return
        elif int(reaction.channel_id) != int(VerifyChannelID):
            return

        elif user != client.user:
            if str(reaction.emoji) == "🖥":
                await member.remove_roles(discord.utils.get(guild.roles, name="Mortus"))
            elif str(reaction.emoji) == "🤖":
                await member.remove_roles(discord.utils.get(guild.roles, name="Bot"))
            elif str(reaction.emoji) == "🫂":
                await member.remove_roles(discord.utils.get(guild.roles, name="Mensch... vielleicht.."))
            else:
                return

client = MyClient()
client.run(token)