import requests, time, random, sys, re, math

async def Witz(requests, message):
    witz = requests.get("https://v2.jokeapi.dev/joke/Any?lang=de&format=txt&type=twopart")
    witz = witz.text
    witz = witz.splitlines()
    witz = [witz[0], witz[2]]
    witz = str(witz).replace("['", "").replace("']", "")
    await message.channel.send(witz.replace("', '", "").replace(".", ". ").replace("?", "? ").replace("!", "! "))

async def Dice(command, random, message):
    try:
        Zahlen = command.split(' ')[1]
        Zahl1 = Zahlen.split(',')[0]
        Zahl2 = Zahlen.split(',')[1]
        Zahl = random.randint(int(Zahl1), int(Zahl2))
    except:
        Zahl = random.randint(1, 6)
        await message.channel.send("Falsche Eingabe, ZufallszaHl zwischen 1 und 6")
    await message.channel.send(f"Du hast eine {Zahl} gewürfelt")

async def Roulette(random, message, userID, discord, cur, con, prefix):
    try:
        gesetzt = message.content.split(' ')[2]
    except:
        gesetzt = 0
 
    uxp = cur.execute(f"SELECT experience FROM users WHERE id = {userID}")
    uxp = cur.fetchall()
    uxp = str(uxp).removeprefix("[(").removesuffix(",)]")

    try:
        if float(uxp) < float(gesetzt):
            await message.channel.send(f"Du hast nicht genügend XP \nGebe {prefix}xp ein, um deine xp zu sehen!")
            gesetzt = 0
    except ValueError:
        await message.channel.send(f"ungültiger Einsatz: {gesetzt}")
    except:
        gesetzt = 0


    bid = message.content.split(' ')[1]
    bid_param = -3


    if bid.lower() == "black":
        bid_param = -1
        farbe = True
    elif bid.lower() == "red":
        bid_param = -2
        farbe = True
    else:
        try:
            bid_param = int(bid)
            farbe = False
        except:
            farbe = False
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


    if farbe:
        multiplier = 1.5
    else:
        multiplier = 3

    user_name = str(message.author).split('#')[0]
    
    if won:
        erhalten = float(multiplier) * float(gesetzt)
        xp_gewonnen = float(erhalten) - float(gesetzt)

        cur.execute(f"UPDATE users SET experience = experience + {xp_gewonnen} WHERE id = {userID}")
        con.commit()

        embed = discord.Embed(title=user_name,
                                color=discord.Colour(0x15f00a))
        if not gesetzt == 0:
            embed.add_field(name="GEWONNEN",
                            value=f"Du hast {xp_gewonnen} XP gewonnen")
        else:
            embed.add_field(name="GEWONNEN",
                            value=f"Du hast gewonnen")

    else:
        cur.execute(f"UPDATE users SET experience = experience - {gesetzt} WHERE id = {userID}")
        con.commit()

        embed = discord.Embed(title=user_name,
                            
                            color=discord.Colour(0xf00a0a))
        if not gesetzt == 0:
            embed.add_field(name="VERLOREN",
                            value=f"Du hast {gesetzt} XP verloren ")

        else:
            embed.add_field(name="VERLOREN",
                            value=f"Du hast verloren ")
    await message.channel.send(embed=embed)




async def Credits(message):
    await message.author.send("`Dieser Bot wurde von SpagettiFisch programmiert`")

async def Help(message, prefix, discord, command):

    if command.startswith(f"{prefix}help commands") or command.startswith(f"{prefix}help cmd") or command.startswith(f"{prefix}help command") or command.startswith(f"{prefix}help cmds"):
        embed = discord.Embed(title="Command Help",
                              colour=discord.Colour(0x9324b5),
                              description="Hier seht ihr alle Commands für Normalfischliche:")
        embed.add_field(name=f"{prefix}dice <Zahl1>,<Zahl2>",
                        value="_würfelt eine Zahl von Zahl 1 bis Zahl 2 oder falls das nicht klappt zwischen 1 und 6_",
                        inline=False)
        embed.add_field(name=f"{prefix}witz",
                        value="_Gibt einen sehr schlechten Witz, den man nicht ernst nehmen sollte, aus._",
                        inline=False)
        embed.add_field(name=f"{prefix}roulette <BID> <Einsatz>",
                        value="_Startet das Roulette \nBID = black/red/beliebige Zahl \nEinsatz = beliebige Zahl, darf aber nicht höher sein, als deine XP, der Einsatz kann weggelassen werden_",
                        inline=False)
        embed.add_field(name=f"{prefix}list",
                        value="_Listet alle Custom Commands auf._",
                        inline=False)
        embed.add_field(name=f"{prefix}addzitat <Person> <Jahr> <Zitat>",
                        value="_Erstellt eine Anfrage zum Hinzufügen eines neuen Zitates._",
                        inline=False)
        embed.add_field(name=f"{prefix}translate <Sprache> <Text>",
                        value="_Übersetzt den eingegebenen Text in eine gewählte Verschlüsselung_",
                        inline=False)

    elif command.startswith(f"{prefix}help links"):
        embed = discord.Embed(title="Link Help",
                              colour=discord.Colour(0x9324b5),
                              description="Hier seht ihr alle Links:")
        embed.add_field(name=f"{prefix}fichbot",
                        value="Informationen zu mir",
                        inline=False)
        embed.add_field(name=f"{prefix}github",
                        value="Github Account von SpagettiFisch",
                        inline=False)
        embed.add_field(name=f"{prefix}twitch",
                        value="Twitch Account von SpagettiFisch",
                        inline=False)
        embed.add_field(name=f"{prefix}ston",
                        value="Twitch Account von Ston",
                        inline=False)
        embed.add_field(name=f"{prefix}slumpfus",
                        value="Twitch Account von Slumpfus",
                        inline=False)
        embed.add_field(name=f"{prefix}credits",
                        value="Das wird meinen Programmierer leaken :c",
                        inline=False)

    else:
        embed = discord.Embed(title="help",
                              colour=discord.Colour(0x9324b5),
                              description="Ich habe verschiedene Help Commands:")
        embed.add_field(name="!help commands/command/cmds/cmd",
                        value="_zeigt die Hilfe für Commands an_",
                        inline=False)
        embed.add_field(name="!help links",
                        value="_zeigt die Hilfe für Links und Credits an_",
                        inline=False)
    await message.channel.send(embed=embed)



async def Zitat(message, client, owner, cur, con):
    owner = await client.fetch_user(owner)
    person = message.content.split()[1]
    jahr = message.content.split()[2]
    zitat = message.content.split(' ', 3)[3]
    if owner != message.author:
        z = open("BotFiles/zitattemp.txt", "a+")
        z.write(f"{person} {jahr} {zitat} @{message.author}\n")
        z.close()
        await owner.send(f"{zitat} - {person} {jahr} @{message.author}")
        await message.channel.send("Zitat Anfrage an meinen Meister geschickt")

    else:
        cur.execute(f"INSERT OR IGNORE INTO zitate VALUES ('{zitat}','{person}',{jahr})")
        con.commit()
        await message.channel.send("Zitat hinzugefügt")



async def confirm_zitat(con, cur, message):
    count = 0
    z = open("BotFiles/zitattemp.txt", "r")
    try:
        number = int(message.content.split()[1])
    except:
        number = False

    zitate = z.readlines()

    for zz in zitate:
        zz = zz.split('@')[0]
        zz = zz.replace('\n', '')
        count += 1
        person = zz.split()[0].removesuffix(' ')
        jahr = zz.split()[1].removesuffix(' ')
        zitat = zz.split(' ', 2)[2].removesuffix(' ')
        if count == number:
            cur.execute(f"INSERT OR IGNORE INTO zitate VALUES ('{zitat}','{person}',{jahr})")
            con.commit()
        elif not number:
            cur.execute(f"INSERT OR IGNORE INTO zitate VALUES ('{zitat}','{person}',{jahr})")
            con.commit()
    z.close()
    await message.channel.send("Zitat(e) erfolgreich bestätigt.")



async def delete_zitat_temp(message):
    z = open("BotFiles/zitattemp.txt", "w+")
    z.write('')
    z.close()
    await message.channel.send("Temporäre Zitate wurden gelöscht.")



async def zitat_abfrage(message, cur, random):
    zitate = cur.execute("SELECT * FROM zitate")
    zitate = cur.fetchall()
    anzahl = len(zitate)
    random = random.randint(1, anzahl)
    count = 0

    for zz in zitate:
        count += 1
        zz = list(zz)
        if count == random:
            zitat = zz.pop(0)
            person = zz.pop(0)
            jahr = zz.pop(0)

            await message.channel.send(f"> {zitat}\n~{person} {jahr}")



async def zitat_loeschen(message, cur, con):
    zitat = message.content.split(' ', 1)[1]
    cur.execute(f"DELETE FROM zitate WHERE zitat = '{zitat}'")
    con.commit()
    await message.channel.send("Zitat gelöscht")



async def wiggle(message):
    for i in range(5):
        await message.author.send("bigger wiggle\nbigger wiggle\nbigger wiggle\n bigger wiggle\n  bigger wiggle\n   bigger wiggle\n     bigger wiggle\n       bigger wiggle\n         bigger wiggle\n            bigger wiggle\n               bigger wiggle\n                  bigger wiggle\n                     bigger wiggle\n                        bigger wiggle\n                           bigger wiggle\n                              bigger wiggle\n                                 bigger wiggle\n                                    bigger wiggle\n                                       bigger wiggle\n                                         bigger wiggle\n                                           bigger wiggle\n                                             bigger wiggle\n                                              bigger wiggle\n                                               bigger wiggle\n                                                bigger wiggle\n                                                bigger wiggle\n                                                bigger wiggle\n                                                bigger wiggle\n                                               bigger wiggle\n                                              bigger wiggle\n                                             bigger wiggle\n                                           bigger wiggle\n                                         bigger wiggle\n                                       bigger wiggle\n                                    bigger wiggle\n                                 bigger wiggle\n                              bigger wiggle\n                           bigger wiggle\n                        bigger wiggle\n                     bigger wiggle\n                  bigger wiggle\n               bigger wiggle\n            bigger wiggle\n         bigger wiggle\n       bigger wiggle\n     bigger wiggle\n   bigger wiggle\n  bigger wiggle\n bigger wiggle")
    await message.channel.send("Wiggle gesendet")



async def translator(message, command, re):
    caesar = {"a": "b", "b": "c", "c": "d", "d": "e", "e": "f", "f": "g", "g": "h", "h": "i", "i": "j", "j": "k", "k": "l", "l": "m", "m": "n", "n": "o", "o": "p", "p": "q", "q": "r", "r": "s", "s": "t", "t": "u", "u": "v", "v": "w", "w": "x", "x": "y", "y": "z", "z": "a", "ä": "ö", "ö": "ü", "ü": "ä", "A": "B", "B": "C", "C": "D", "D": "E", "E": "F", "F": "G", "G": "H", "H": "I", "I": "J", "J": "K", "K": "L", "L": "M", "M": "N", "N": "O", "O": "P", "P": "Q", "Q": "R", "R": "S", "S": "T", "T": "U", "U": "V", "V": "W", "W": "X", "X": "Y", "Y": "Z", "Z": "A", "Ä": "Ö", "Ö": "Ü", "Ü": "Ä", "0": "1", "1": "2", "2": "3", "3": "4", "4": "5", "5": "6", "6": "7", "7": "8", "8": "9", "9": "0"}
    morse = { 'A':'.-', 'B':'-...', 'C':'-.-.', 'D':'-..', 'E':'.', 'F':'..-.', 'G':'--.', 'H':'....', 'I':'..', 'J':'.---', 'K':'-.-', 'L':'.-..', 'M':'--', 'N':'-.', 'O':'---', 'P':'.--.', 'Q':'--.-', 'R':'.-.', 'S':'...', 'T':'-', 'U':'..-', 'V':'...-', 'W':'.--', 'X':'-..-', 'Y':'-.--', 'Z':'--..', '1':'.----', '2':'..---', '3':'...--', '4':'....-', '5':'.....', '6':'-....', '7':'--...', '8':'---..', '9':'----.', '0':'-----', ',':'--..--', '.':'.-.-.-', '?':'..--..', '/':'-..-.', '-':'-....-', '(':'-.--.', ')':'-.--.-', ' ': '/'}
    try:
        sprache = command.split()[1]
        content = message.content.split(' ', 2)[2]
        translated_text = ""
    except:
        await message.channel.send(f"Fehlende Argumente :c \nDu musst '!translate <Sprache> <Text>' verwenden")

    if str(sprache) == "caesar":
        for letter in content:
            if re.match("[a-zA-Z0-9ä-üÄ-Ü]", letter):
                translated_text += str(caesar[letter])
            else:
                translated_text += letter

    elif str(sprache) == "morse":
        for letter in content:
            if re.match("[[a-zA-Z0-9ä-üÄ-Ü:.,? ]", letter):
                translated_text += f"{str(morse[letter.upper()])} "
            else:
                translated_text += letter
    
    else:
        await message.channel.send(f"Die angegebene Sprache ({sprache}) existiert nicht :/\nEs gibt zur Zeit nur caesar und morse!")
        await message.delete()
        return
    
    try:
        await message.author.send(f"{content} → {translated_text}")
    except:
        await message.channel.send("Nachricht konnte nicht gesendet werden")
    finally:
        await message.delete()


    #Links
async def Fichbot(message, time):
    await message.channel.send(
        "Das bin ich. Was gibt es? Um zu sehen, was ich alles tolles kann, schreib einfach !help \nIch bin ungefähr <t:1594212810:R> erschaffen worden!")
    time.sleep(3)
    await message.channel.send(
        "Meinen Code findest du natürlich auch auf Github: https://github.com/SpagettiFisch/Fichbot\nEr ist übrigens SEHR gut! ~Cyklon_3000, 2021")

async def Github(message):
    await message.channel.send(
        "Hier geht es zum Github Profil von SpagettiFisch: https://github.com/SpagettiFisch")

async def Twitch(message):
    await message.channel.send(
        "Falls er irgendwann mal streamen sollte, wirst du ihn hier finden: https://www.twitch.tv/spagettifisch2")

async def Ston(message):
    await message.channel.send(
        "Das ist ein ganz einsamer Stein, besuch ihn doch mal ;) https://www.twitch.tv/der_ston")

async def Slumpfus(message):
    await message.channel.send(
        "Geht mal zum lieben Slumpfus rüber, lasst einen Follow und Liebe da, dann kann der Fisch endlich seine Bits loswerden^^ "
        "https://www.twitch.tv/slumpfus")


async def OwnerCommands(bot, commands):
    @bot.command(hidden = True)
    @commands.has_role("Fisch")
    async def stop(ctx):
        await ctx.channel.send("Ja wie denn? xD \nIch könnte das ja mal probie... ")
        print("Ich geh dann mal offline")
        bot.clear()
        await bot.close()
        await sys.exit(1)

    @bot.command(hidden=True)
    @commands.has_role("Fisch")
    async def clear(ctx, number):
        messages = await ctx.channel.history(limit=int(number)).flatten()
        for message in messages:
            await message.delete()

    @bot.command(hidden = True, aliases = ["dm"])
    @commands.has_role("Fisch")
    async def DirectMessage(ctx, user, message):
        #Person = await bot.fetch_user(ctx.split('+')[1])
        #Nachricht = ctx.content.split('+')[2]
        await user.send(message)
        await ctx.channel.send("gesendet^^")
        if not "Direct Message with" in str(ctx.channel):
            await ctx.delete()

    @bot.command(hidden = True, aliases = ["ai", "ki"])
    @commands.has_role("Fisch")
    async def ArtifactialIntelligence(ctx, channelid, message):
        channel = await bot.fetch_channel(channelid)
        await channel.send(message)
        await ctx.channel.send("gesendet^^")
        if not "Direct Message with" in str(ctx.channel): 
            await ctx.delete()