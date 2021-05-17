async def XP(message, userID, cur, con):
    try:
        uxp = open(f"XPFiles/{userID}.txt", "r")
        uXP = uxp.readline()
        uxp.close()
    except:
        pass

    u = open(f"XPFiles/{userID}.txt", "w+")
    Laenge = len(message.content)
    Laenge /= 25
    if Laenge > 25:
        Laenge = 25
    try:
        neueXP = float(uXP) + float(Laenge)
    except:
        neueXP = Laenge

    u.writelines(str(neueXP))
    u.close()
    try:
        cur.execute(f"INSERT INTO users VALUES ({userID},'{str(message.author).split('#')[0]}','{message.author.nick}','{message.author.color}','{str(message.author.avatar_url).removeprefix('https://').removesuffix('?size=1024')}','{neueXP}')")
        con.commit()
    except:
        cur.execute(f"UPDATE users SET experience = experience + {Laenge}, color = '{message.author.color}', nickname = '{message.author.nick}', avatar = '{str(message.author.avatar_url).removeprefix('https://').removesuffix('?size=1024')}', username = '{str(message.author).split('#')[0]}' WHERE id = {userID}")
        con.commit()


async def xp_request(message, math, discord, random, userID):
    try:
        uxp = open(f"XPFiles/{userID}.txt", "r")
        uXP = uxp.readline()
        uxp.close()

    except:
        await message.channel.send("Benutzer nicht vorhanden")
        return


    r = lambda: random.randint(0, 255)
    Farbe = '%02X%02X%02X' % (r(), r(), r())
    Farbe = f"0x{Farbe}"
    Farbe = int(Farbe, 0)


    try:
        roundedXP = math.floor(float(uXP))

    except:
        await message.channel.send("sorry :ccc \n Du hast wohl nicht genug XP")
        return


    user_name = str(message.author).split('#')[0]
    embed = discord.Embed(title=str(user_name),
                          color=Farbe)
    embed.add_field(name="XP",
                    value=roundedXP)
    await message.channel.send(embed=embed)



async def user_xp_request(message, math, client, discord, random):
    try:
        UserID = message.content.split(' ')[1]
        user = await client.fetch_user(UserID)
        uxp = open(f"XPFiles/{UserID}.txt", "r")
        uXP = uxp.readline()
        uxp.close()

    except:
        await message.channel.send("Benutzer nicht vorhanden")
        return


    user_name = str(user).split('#')[0]

    r = lambda: random.randint(0, 255)
    farbe = '%02X%02X%02X' % (r(), r(), r())
    farbe = f"0x{farbe}"
    farbe = int(farbe, 0)


    try:
        roundedXP = math.floor(float(uXP))

    except:
        await message.channel.send(f"{user_name} hat nicht genügend XP")
        return


    embed = discord.Embed(title=user_name,
                          color=farbe)
    embed.add_field(name="XP",
                    value=roundedXP)
    await message.channel.send(embed=embed)



async def add_xp(message, random, client, discord):
    try:
        UserID = message.content.split(' ')[1]
        user = await client.fetch_user(UserID)
        uxp = open(f"XPFiles/{UserID}.txt", "r")
        uXP = uxp.readline()
        uxp.close()

    except:
        await message.channel.send("Benutzer nicht vorhanden")
        return

    user_name = str(user).split('#')[0]

    r = lambda: random.randint(0, 255)
    farbe = '%02X%02X%02X' % (r(), r(), r())
    farbe = f"0x{farbe}"
    farbe = int(farbe, 0)


    added = message.content.split(' ')[2]
    uXP = float(uXP) + int(added)


    u = open(f"XPFiles/{UserID}.txt", "w+")
    u.writelines(str(uXP))
    u.close()

    #roundedXP = math.floor(float(uXP))
    roundedXP = round(float(uXP))

    embed = discord.Embed(title=user_name,
                          color=farbe)
    embed.add_field(name="XP",
                    value=roundedXP)
    await message.channel.send(embed=embed)



async def remove_xp(message, random, client, discord):
    try:
        UserID = message.content.split(' ')[1]
        user = await client.fetch_user(UserID)
        uxp = open(f"XPFiles/{UserID}.txt", "r")
        uXP = uxp.readline()
        uxp.close()

    except:
        await message.channel.send("Benutzer nicht vorhanden")
        return

    user_name = str(user).split('#')[0]

    r = lambda: random.randint(0, 255)
    farbe = '%02X%02X%02X' % (r(), r(), r())
    farbe = f"0x{farbe}"
    farbe = int(farbe, 0)


    removed = message.content.split(' ')[2]
    uXP = float(uXP) - int(removed)

    if uXP < 0:
        uXP = 0


    u = open(f"XPFiles/{UserID}.txt", "w+")
    u.writelines(str(uXP))
    u.close()

    #roundedXP = math.floor(float(uXP))
    roundedXP = round(float(uXP))

    embed = discord.Embed(title=user_name,
                          color=farbe)
    embed.add_field(name="XP",
                    value=roundedXP)
    await message.channel.send(embed=embed)



async def reset_xp(message, random, client, discord):

    UserID = message.content.split(' ')[1]
    user = await client.fetch_user(UserID)
    user_name = str(user).split('#')[0]

    r = lambda: random.randint(0, 255)
    farbe = '%02X%02X%02X' % (r(), r(), r())
    farbe = f"0x{farbe}"
    farbe = int(farbe, 0)


    uXP = 0


    u = open(f"XPFiles/{UserID}.txt", "w+")
    u.writelines(str(uXP))
    u.close()

    embed = discord.Embed(title=user_name,
                          color=farbe)
    embed.add_field(name="XP",
                    value=uXP)
    await message.channel.send(embed=embed)