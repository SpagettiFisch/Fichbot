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

async def Roulette(random, message, userID, discord):
    try:
        gesetzt = message.content.split(' ')[2]

        uxp = open(f"XPFiles/{userID}.txt", "r")
        uXP = uxp.readline()
        uxp.close()

        if float(uXP) < float(gesetzt):
            await message.channel.send("Du hast nicht genügend XP")
            return


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

        if won:
            erhalten = float(multiplier) * float(gesetzt)
            xp_gewonnen = float(erhalten) - float(gesetzt)
            uXP = float(uXP) + float(xp_gewonnen)
            u = open(f"XPFiles/{userID}.txt", "w+")
            u.writelines(str(uXP))
            u.close()
            user_name = str(message.author).split('#')[0]
            embed = discord.Embed(title="user_name",
                                  color=discord.Colour(0x15f00a))
            embed.add_field(name="GEWONNEN",
                            value=f"Du hast {xp_gewonnen} XP bekommen^^")
        else:
            embed = discord.Embed(title="user_name",
                                  color=discord.Colour(0xf00a0a))
            embed.add_field(name="VERLOREN",
                            value=f"Du hast {gesetzt} XP verloren :(")

    except:
        await message.channel.send("Da ist ein Fehler aufgetreten :/")
        return



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
        embed.add_field(name=f"{prefix}roulette <BID>",
                        value="_Startet das Roulette (es gibt aber nix zu gewinnen ||sorry :c||), BID= black/red/beliebige Zahl_",
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


    #Links

async def Fichbot(message, time):
    await message.channel.send(
        "Das bin ich. Was gibt es? Um zu sehen, was ich alles tolles kann, schreib einfach !help")
    time.sleep(3)
    await message.channel.send(
        "Meinen Code findest du natürlich auch auf Github: https://github.com/SpagettiFisch/Fichbot")

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