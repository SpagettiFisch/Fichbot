import discord
import random
import json
import sys
import time
import requests
import math
import sqlite3
from functions import Blacklist, status, cmd, OwnerCMD, React, xp, customCommands, log

c = open("BotFiles/config.json")
json_data = json.load(c)
prefix = json_data["prefix"] #Preifx for Bot Commands
Logs = json_data["Logs"] #should Logging be enabled
BotOwnerID = json_data["Bot_Owner_ID"] #ID of the person who can use all Bot Commands
CommandChannelID = json_data["Command_Channel_ID"] #the Channel ID for the most Bot Commands
VerifyMessageID = json_data["Verify_Message_ID"] #the message ID used for reaction verification
VerifyChannelID = json_data["Verify_Channel_ID"] # the Channel ID used for reaction verification
bl = json_data["Blacklist"]
b = open("BotFiles/Blacklist", "r")
blacklist = b.read()

con = sqlite3.connect("BotFiles/BotThings.sqlite")
cur = con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS users (id number PRIMARY KEY, username text, nickname text, color text, avatar text, experience number)")
cur.execute("CREATE TABLE IF NOT EXISTS customcommands (trigger text PRIMARY KEY, command text)")
cur.execute("CREATE TABLE IF NOT EXISTS zitate (zitat text PRIMARY KEY, person text, jahr number)")


async def if_ready(client):
    print("Ich habe mich eingeloggt.")

    s = open("BotFiles/status", "r")
    Status = s.read()
    await status.status(Status, client, discord, s)
    s.close()
    person = await client.fetch_user(734868946825510933)



async def if_message(message, client):

    id = str(message).split(' ')[12]
    userID = id.split('=')[1]
    cid = str(message).split(' ')[3]
    ChannelID = cid.split('=')[1]
    command = message.content.lower()
    if bl:
        await Blacklist.Blacklist(message, userID, command, blacklist)
    if not "direct message with" in str(message.channel).lower():
        await xp.XP(message, userID, cur, con)



    if message.author != client.user:
        await React.ReacT(random, ChannelID, CommandChannelID, message)
        if message.content.startswith(prefix):
            await customCommands.check_commands(command, cur, prefix, message)

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
                    await cmd.Zitat(message, client, BotOwnerID, cur, con)

                #Owner Commands
            elif int(ChannelID) == int(830343228502048808) or str(message.channel) == "Direct Message with SpagettiFisch#7613":


                if int(userID) == int(BotOwnerID):


                    if command.startswith(f"{prefix}status"):
                        Status = message.content
                        s = open("BotFiles/status", "w")
                        await status.status(Status, client, discord, s)



                    elif command.startswith(f"{prefix}add "):
                        await customCommands.add_command(message, cur, con, prefix)



                    elif command.startswith(f"{prefix}delete "):
                        await customCommands.delete_command(cur, con, message, prefix, command, sqlite3)



                    elif command.startswith(f"{prefix}stop"):
                        if int(userID) == int(BotOwnerID):
                            await OwnerCMD.Stop(sys, client, message)



                    elif command.startswith(f"{prefix}dm"):
                        await OwnerCMD.DM(client, command, message)



                    elif command.startswith(f"{prefix}ki"):
                        await OwnerCMD.KI(command, message, client)



                    elif command.startswith(f"{prefix}uxp"):
                        await xp.user_xp_request(message, math, client, discord, cur)



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






    #Logging
        if Logs:
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



async def if_edit(before, after, client):
    if Logs:
            if before.author != client.user:
                await log.edit_log(client, before, after, discord)
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



async def if_delete(message, client):
    if Logs:
            await log.delete_log(client, message, discord)