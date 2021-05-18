import discord

async def XP(message, userID, cur, con):
    Laenge = len(message.content)
    Laenge /= 25
    if Laenge > 25:
        Laenge = 25
    XPs = Laenge

    try:
        cur.execute(f"INSERT INTO users VALUES ({userID},'{str(message.author).split('#')[0]}','{message.author.nick}','{message.author.color}','{str(message.author.avatar_url).removeprefix('https://').removesuffix('?size=1024')}','{XPs}')")
        con.commit()
    except:
        cur.execute(f"UPDATE users SET experience = experience + {XPs}, color = '{message.author.color}', nickname = '{message.author.nick}', avatar = '{str(message.author.avatar_url).removeprefix('https://').removesuffix('?size=1024')}', username = '{str(message.author).split('#')[0]}' WHERE id = {userID}")
        con.commit()


async def xp_request(message, math, discord, userID, cur):
    try:
        userxp = cur.execute(f"SELECT experience FROM users WHERE id = {userID}")
        userxp = cur.fetchall()
        userxp = str(userxp).removesuffix(",)]").removeprefix("[(")

        farbe = cur.execute(f"SELECT color FROM users WHERE id = {userID}")
        farbe = cur.fetchall()
        farbe = f'''0x{str(farbe).removesuffix("',)]").removeprefix("[('#")}'''
        farbe = int(farbe, 0)

        nick = cur.execute(f"SELECT nickname FROM users WHERE id = {userID}")
        nick = cur.fetchall()
        nick = str(nick).removesuffix("',)]").removeprefix("[('")

    except:
        await message.channel.send("Benutzer nicht vorhanden")
        return



    try:
        roundedXP = math.floor(float(userxp))

    except:
        await message.channel.send("sorry :ccc \nDu hast wohl nicht genug XP")
        return

    user_name = str(message.author).split('#')[0]

    if nick == "None":
        embed = discord.Embed(title=str(user_name),
                            color=farbe)
    else:
        embed = discord.Embed(title=str(user_name),
                            color=farbe,
                            description=nick)

    embed.add_field(name="XP",
                    value=roundedXP)
    await message.channel.send(embed=embed)



async def user_xp_request(message, math, client, discord, cur):
    userid = message.content.split(' ')[1]

    user = await client.fetch_user(userid)

    try:
        userxp = cur.execute(f"SELECT experience FROM users WHERE id = {userid}")
        userxp = cur.fetchall()
        userxp = str(userxp).removesuffix(",)]").removeprefix("[(")

        farbe = cur.execute(f"SELECT color FROM users WHERE id = {userid}")
        farbe = cur.fetchall()
        farbe = f'''0x{str(farbe).removesuffix("',)]").removeprefix("[('#")}'''
        farbe = int(farbe, 0)

        nick = cur.execute(f"SELECT nickname FROM users WHERE id = {userid}")
        nick = cur.fetchall()
        nick = str(nick).removesuffix("',)]").removeprefix("[('")

    except:
        await message.channel.send("Benutzer nicht vorhanden")
        return



    try:
        roundedXP = math.floor(float(userxp))

    except:
        await message.channel.send("der User hat nicht genügend XP")
        return

    user_name = str(user).split('#')[0]


    if nick == "None":
        embed = discord.Embed(title=str(user_name),
                            color=farbe)
    else:
        embed = discord.Embed(title=str(user_name),
                            color=farbe,
                            description=nick)

    embed.add_field(name="XP",
                    value=roundedXP)
    await message.channel.send(embed=embed)



async def add_xp(message, cur, con, math):
    cur = con.cursor()

    try:
        userid = message.content.split(' ')[1]
        
        userxp = cur.execute(f"SELECT experience FROM users WHERE id = {userid}")
        userxp = cur.fetchall()
        userxp = str(userxp).removesuffix(",)]").removeprefix("[(")

        farbe = cur.execute(f"SELECT color FROM users WHERE id = {userid}")
        farbe = cur.fetchall()
        farbe = f'''0x{str(farbe).removesuffix("',)]").removeprefix("[('#")}'''
        farbe = int(farbe, 0)

        nick = cur.execute(f"SELECT nickname FROM users WHERE id = {userid}")
        nick = cur.fetchall()
        nick = str(nick).removesuffix("',)]").removeprefix("[('")

        user = cur.execute(f"SELECT username FROM users WHERE id = {userid}")
        user = cur.fetchall()
        user_name = str(user).removesuffix("',)]").removeprefix("[('")


    except:
        await message.channel.send("Benutzer nicht vorhanden")
        return


    try:
        added = message.content.split(' ')[2]
    except:
        await message.channel.send("Fehlender Parameter: XP")
        return
    userxp = float(userxp) + float(added)
    
    cur.execute(f"UPDATE users SET experience = experience + {float(added)} WHERE id = {userid}")
    con.commit

    

    roundedXP = math.floor(float(userxp))

    if nick == "None":
        embed = discord.Embed(title=str(user_name),
                            color=farbe)
    else:
        embed = discord.Embed(title=str(user_name),
                            color=farbe,
                            description=nick)

    embed.add_field(name="XP",
                    value=roundedXP)
    await message.channel.send(embed=embed)



async def remove_xp(message, cur, con, math):
    try:
        userid = message.content.split(' ')[1]
        
        userxp = cur.execute(f"SELECT experience FROM users WHERE id = {userid}")
        userxp = cur.fetchall()
        userxp = str(userxp).removesuffix(",)]").removeprefix("[(")

        farbe = cur.execute(f"SELECT color FROM users WHERE id = {userid}")
        farbe = cur.fetchall()
        farbe = f'''0x{str(farbe).removesuffix("',)]").removeprefix("[('#")}'''
        farbe = int(farbe, 0)

        nick = cur.execute(f"SELECT nickname FROM users WHERE id = {userid}")
        nick = cur.fetchall()
        nick = str(nick).removesuffix("',)]").removeprefix("[('")

        user = cur.execute(f"SELECT username FROM users WHERE id = {userid}")
        user = cur.fetchall()
        user_name = str(user).removesuffix("',)]").removeprefix("[('")


    except:
        await message.channel.send("Benutzer nicht vorhanden")
        return


    try:
        added = message.content.split(' ')[2]
    except:
        await message.channel.send("Fehlender Parameter: XP")
        return

    userxp = float(userxp) - float(added)
    
    cur.execute(f"UPDATE users SET experience = experience - {float(added)} WHERE id = {userid}")
    con.commit

    

    roundedXP = math.floor(float(userxp))

    if nick == "None":
        embed = discord.Embed(title=str(user_name),
                            color=farbe)
    else:
        embed = discord.Embed(title=str(user_name),
                            color=farbe,
                            description=nick)

    embed.add_field(name="XP",
                    value=roundedXP)
    await message.channel.send(embed=embed)



async def reset_xp(message, cur, con):
    try:
        userid = message.content.split(' ')[1]
        
        userxp = cur.execute(f"SELECT experience FROM users WHERE id = {userid}")
        userxp = cur.fetchall()
        userxp = str(userxp).removesuffix(",)]").removeprefix("[(")

        farbe = cur.execute(f"SELECT color FROM users WHERE id = {userid}")
        farbe = cur.fetchall()
        farbe = f'''0x{str(farbe).removesuffix("',)]").removeprefix("[('#")}'''
        farbe = int(farbe, 0)

        nick = cur.execute(f"SELECT nickname FROM users WHERE id = {userid}")
        nick = cur.fetchall()
        nick = str(nick).removesuffix("',)]").removeprefix("[('")

        user = cur.execute(f"SELECT username FROM users WHERE id = {userid}")
        user = cur.fetchall()
        user_name = str(user).removesuffix("',)]").removeprefix("[('")


    except:
        await message.channel.send("Benutzer nicht vorhanden")
        return

    
    cur.execute(f"UPDATE users SET experience = 0 WHERE id = {userid}")
    con.commit


    if nick == "None":
        embed = discord.Embed(title=str(user_name),
                            color=farbe)
    else:
        embed = discord.Embed(title=str(user_name),
                            color=farbe,
                            description=nick)

    embed.add_field(name="XP",
                    value=0)
    await message.channel.send(embed=embed)
