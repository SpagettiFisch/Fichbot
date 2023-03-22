import discord
import random
import json
import sqlite3
from functions import Blacklist, Commands, custom, status as Status, React, xp, log

c = open("BotFiles/config.json")
json_data = json.load(c)
prefix = json_data["prefix"] #Prefix for Bot Commands
Logs = json_data["Logs"] #should Logging be enabled
BotOwnerID = json_data["Bot_Owner_ID"] #ID of the person who can use all Bot Commands
CommandChannelID = json_data["Command_Channel_ID"] #the Channel ID for the most Bot Commands
VerifyMessageID = json_data["Verify_Message_ID"] #the message ID used for reaction verification
VerifyChannelID = json_data["Verify_Channel_ID"] # the Channel ID used for reaction verification
bl = json_data["Blacklist"]
#b = open("BotFiles/Blacklist", "r")
#blacklist = b.read()

con = sqlite3.connect("BotFiles/BotThings.sqlite")
cur = con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS users (id number PRIMARY KEY, username text, nickname text, color text, avatar text, experience number)")
cur.execute("CREATE TABLE IF NOT EXISTS customcommands (trigger text PRIMARY KEY, command text)")
cur.execute("CREATE TABLE IF NOT EXISTS zitate (zitat text PRIMARY KEY, person text, jahr number)")
cur.execute("CREATE TABLE IF NOT EXISTS reactionRoles (name text PRIMARY KEY, channel_id number, message_id number, info text, emoji text, role_id number)")


async def if_ready(bot, commands, slash):
    with open("BotFiles/status", "r") as status_file:
        status = status_file.read()
        await Status.Status(status, bot, discord, status_file)
    print('Status set')
    #person = await bot.fetch_user(734868946825510933)
    bot.remove_command("help")
    await Commands.OwnerCommands(bot, commands, slash)
    print('Loaded restricted commands')
    await Commands.ChatCommands(bot, prefix, cur, con, slash)
    print('Loaded commands')
    await Commands.LinkCommands(bot, slash)
    print('Loaded links')
    await custom.reactionEvent(con, cur, bot, slash)
    print(f'{bot.user} has connected to Discord!')


async def if_message(message, bot):
    #generell message infos
    id = str(message).split(' ')[12]
    userID = id.split('=')[1]
    cid = str(message).split(' ')[3]
    ChannelID = cid.split('=')[1]
    command = message.content.lower()
    #blacklsit, xp and random reactions
    if bl:
        await Blacklist.Blacklist(message, userID, command, blacklist)
    if not "direct message with" in str(message.channel).lower():
        await xp.XP(message, userID, cur, con)
    elif message.author != bot.user:
        await React.react(random, ChannelID, CommandChannelID, message)
    
    #Logging
    if Logs:
        str(message.created_at).split(".").pop()
        try:
            date = str(str(message.created_at).split(".")).split(" ")[0].replace("['", "")
            time = str(str(message.created_at).split(".")).split(" ")[1].replace("']", "")
            l = open("BotFiles/logs.txt", "a")
            l.writelines(f'\n{message.author} hat in {message.channel}, auf dem Server {message.guild} am {date} um {time} "{message.content}" geschrieben.')
            l.close()
        except:
            l = open("BotFiles/logs.txt", "a")
            l.writelines(f'\nFEHLER "{message.content}" von {message.author}')
            l.close()

#        if message.content.startswith(prefix):
#            await customCommands.check_commands(command, cur, prefix, message)
"""
            #not Chat Commands
            if int(ChannelID) == int(CommandChannelID):
                if command.startswith(f"{prefix}list"):
                    await customCommands.list_commands(cur, message, discord, prefix)

                elif command.startswith(f'{prefix}help'):
                    await cmd.Help(message, prefix, discord, command)

                elif command.startswith(f"{prefix}xp"):
                    await xp.xp_request(message, math, discord, userID, cur)

                elif command.startswith(f"{prefix}credits"):
                    await cmd.Credits(message)

                elif command.startswith(f"{prefix}addzitat"):
                    await cmd.Zitat(message, bot, BotOwnerID, cur, con)

                elif command.startswith(f"{prefix}translate"):
                    await cmd.translator(message, command, re)

                elif command.startswith(f"{prefix}wiggle"):
                    await cmd.wiggle(message)
                    
                elif command.startswith(f"{prefix}level"):
                    await xp.check_level(math, userID, cur, discord, message)

                #Owner Commands
            elif int(ChannelID) == int(830343228502048808) or str(message.channel) == "Direct Message with SpagettiFisch#7613":


                if int(userID) == int(BotOwnerID):


                    if command.startswith(f"{prefix}status"):
                        Status = message.content
                        s = open("BotFiles/status", "w")
                        await status.status(Status, bot, discord, s)



                    elif command.startswith(f"{prefix}add "):
                        await customCommands.add_command(message, cur, con, prefix)



                    elif command.startswith(f"{prefix}delete "):
                        await customCommands.delete_command(cur, con, message, prefix, command, sqlite3)



                    elif command.startswith(f"{prefix}stop"):
                        if int(userID) == int(BotOwnerID):
                            await OwnerCMD.Stop(sys, bot, message)



                    elif command.startswith(f"{prefix}dm"):
                        await OwnerCMD.DM(bot, command, message)



                    elif command.startswith(f"{prefix}ki"):
                        await OwnerCMD.KI(command, message, bot)



                    elif command.startswith(f"{prefix}uxp"):
                        await xp.user_xp_request(message, math, bot, discord, cur)



                    elif command.startswith(f"{prefix}addxp"):
                        await xp.add_xp(message, cur, con, math)



                    elif command.startswith(f"{prefix}removexp"):
                        await xp.remove_xp(message, cur, con, math)



                    elif command.startswith(f"{prefix}resetxp"):
                        await xp.reset_xp(message, cur, con)



                    elif command.startswith(f"{prefix}confirm"):
                        await cmd.confirm_zitat(con, cur, message)



                    elif command.startswith(f"{prefix}deletetemp"):
                        await cmd.delete_zitat_temp(message)



                    elif command.startswith(f"{prefix}delzitat"):
                        await cmd.zitat_loeschen(message, cur, con)



            #Chat Commands
            elif command.startswith(f"{prefix}witz"):
                await cmd.Witz(requests, message)



            elif command.startswith(f"{prefix}dice"):
                await cmd.Dice(command, random, message)



            elif command.startswith(f"{prefix}zitat"):
                await cmd.zitat_abfrage(message, cur, random)



            elif command.startswith(f"{prefix}roulette "):
                await cmd.Roulette(random, message, userID, discord, cur, con, prefix)



            elif command.startswith(f"{prefix}github"):
                await cmd.Github(message)



            elif command.startswith(f"{prefix}fichbot"):
                await cmd.Fichbot(message, time)



            elif command.startswith(f"{prefix}twitch"):
                await cmd.Twitch(message)



            elif command.startswith(f"{prefix}ston"):
                await cmd.Ston(message)



            elif command.startswith(f"{prefix}slumpfus"):
                await cmd.Slumpfus(message)
"""





async def if_edit(before, after, bot):
    if Logs:
            if before.author != bot.user:
                await log.edit_log(bot, before, after, discord)
                try:
                    str(after.edited_at).split('.').pop()
                    date = str(str(after.edited_at).split('.')).split(" ")[0].replace("['", "")
                    time = str(str(after.edited_at).split('.')).split(" ")[1].replace("']", "")
                    l = open('BotFiles/logs.txt', 'a')
                    l.writelines(f'\n{before.author} hat in {after.channel} auf {after.guild} am {date} um {time} von "{before.content}" zu "{after.content}" bearbeitet.')
                    l.close()
                except:
                    l = open("BotFiles/logs.txt", "a")
                    l.writelines(
                        f'\nFEHLER(BEARBEITET) "{after.content}" von {before.author}')
                    l.close()



async def if_delete(message, bot):
    if Logs:
            await log.delete_log(bot, message, discord)



async def if_member_update(before, after, bot):
    mod_channel = await bot.fetch_channel(836542316273467403)
    if int(before.id) == 542693392245719050 and str(before.status) != str(after.status) and str(after.status) == "online":
        if str(before.status) == "idle":
            await mod_channel.send("<@477352031561187328> Cykloni ist zurück!")
            #await after.send("wb")
        elif str(before.status) == "dnd":
            pass
            #await after.send("Nicht mehr rot uwu")
        else: 
            await mod_channel.send("<@477352031561187328> Cyklon ist daaaaa!")
            #await after.send("Heyuuuuuuuuuu Großer!\nGrüße von deinem kleinen Fischi!")

    elif str(before.nick) != str(after.nick):
        if "database" in str(after.nick).lower() or "drop" in str(after.nick).lower():
            await log.name_log(bot, after, after.nick, before.nick, "Nickname", discord)

        elif "database" in str(after).lower() or "drop" in str(after).lower():
            await log.name_log(bot, after, after, before, "Username", discord)



async def if_reaction_add(bot):
    pass