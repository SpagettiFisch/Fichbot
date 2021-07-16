import discord

async def XP(message, userID, cur, con):
    Laenge = len(message.content)
    Laenge /= 25
    if Laenge > 25:
        Laenge = 25
    XPs = Laenge

    try:
        cur.execute(f'''INSERT INTO users VALUES ({userID},'{str(message.author).split('#')[0].replace('(', '').replace("'", '').replace(')', '')}','{str(message.author.nick).replace("'", '').replace('(', '').replace(')', '')}','{message.author.color}','{str(message.author.avatar_url).removeprefix('https://').removesuffix('?size=1024')}',{XPs})''')
        con.commit()
    except:
        cur.execute(f'''UPDATE users SET experience = experience + {XPs}, color = '{message.author.color}', nickname = '{str(message.author.nick).replace("'", '').replace('(', '').replace(')', '')}', avatar = '{str(message.author.avatar_url).removeprefix('https://').removesuffix('?size=1024')}', username = '{str(message.author).split('#')[0].replace("'", '').replace('(', '').replace(')', '')}' WHERE id = {userID}''')
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

        avatar = cur.execute(f"SELECT avatar FROM users WHERE id = {userID}")
        avatar = cur.fetchall()
        avatar = avatar.pop()
        avatar = str(avatar).removeprefix("('").removesuffix("',)")

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
    
    embed.set_thumbnail(url=f"https://{avatar}")
    embed.add_field(name="XP",
                    value=roundedXP)
    await message.channel.send(embed=embed)



async def user_xp_request(message, math, client, discord, cur):
    try:
        userid = int(message.content.split(' ')[1])
        user = await client.fetch_user(userid)

    except ValueError:
        try:
            userid = int(str(message.content.split(' ')[1]).removeprefix("<@!").removesuffix(">"))
        
        except:
            await message.channel.send("ungültige Nutzer ID")
            return 
    
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

        user = await client.fetch_user(userid)
        user_name = str(user).split('#')[0]

        avatar = cur.execute(f"SELECT avatar FROM users WHERE id = {userid}")
        avatar = cur.fetchall()
        avatar = avatar.pop()
        avatar = str(avatar).removeprefix("('").removesuffix("',)")

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

    embed.set_thumbnail(url=f"https://{avatar}")
    embed.add_field(name="XP",
                    value=roundedXP)
    await message.channel.send(embed=embed)



async def add_xp(message, cur, con, math):
    cur = con.cursor()

    try:
        userid = int(message.content.split(' ')[1])

    except ValueError:
        try:
            userid = int(str(message.content.split(' ')[1]).removeprefix("<@!").removesuffix(">"))
        
        except:
            await message.channel.send("ungültige Nutzer ID")
            return 
    
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

        user = cur.execute(f"SELECT username FROM users WHERE id = {userid}")
        user = cur.fetchall()
        user_name = str(user).removesuffix("',)]").removeprefix("[('")

        avatar = cur.execute(f"SELECT avatar FROM users WHERE id = {userid}")
        avatar = cur.fetchall()
        avatar = avatar.pop()
        avatar = str(avatar).removeprefix("('").removesuffix("',)")

    except:
        await message.channel.send("Benutzer nicht vorhanden")
        return


    try:
        added = message.content.split(' ')[2]
    except:
        await message.channel.send("Fehlender Parameter: XP")
        return
    try:
        userxp = float(userxp) + float(added)

    except:
        await message.channel.send("Die XP müssen als Zahl angegeben werden.")
    
    if float(userxp) < 0:
        cur.execute(f"UPDATE users SET experience = 0 WHERE id = {userid}")
        userxp = 0
        
    else:
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

    embed.set_thumbnail(url=f"https://{avatar}")
    embed.add_field(name="XP",
                    value=roundedXP)
    await message.channel.send(embed=embed)



async def remove_xp(message, cur, con, math):
    try:
        userid = int(message.content.split(' ')[1])

    except ValueError:
        try:
            userid = int(str(message.content.split(' ')[1]).removeprefix("<@!").removesuffix(">"))
        
        except:
            await message.channel.send("ungültige Nutzer ID")
            return 
    
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

        user = cur.execute(f"SELECT username FROM users WHERE id = {userid}")
        user = cur.fetchall()
        user_name = str(user).removesuffix("',)]").removeprefix("[('")

        avatar = cur.execute(f"SELECT avatar FROM users WHERE id = {userid}")
        avatar = cur.fetchall()
        avatar = avatar.pop()
        avatar = str(avatar).removeprefix("('").removesuffix("',)")

    except:
        await message.channel.send("Benutzer nicht vorhanden")
        return


    try:
        added = message.content.split(' ')[2]
    except:
        await message.channel.send("Fehlender Parameter: XP")
        return

    try:
        userxp = float(userxp) + float(added)
    except:
        await message.channel.send("Die XP müssen als Zahl angegeben werden.")
    
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

    embed.set_thumbnail(url=f"https://{avatar}")
    embed.add_field(name="XP",
                    value=roundedXP)
    await message.channel.send(embed=embed)



async def reset_xp(message, cur, con):
    try:
        userid = int(message.content.split(' ')[1])

    except ValueError:
        try:
            userid = int(str(message.content.split(' ')[1]).removeprefix("<@!").removesuffix(">"))
        
        except:
            await message.channel.send("ungültige Nutzer ID")
            return 
    
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

        user = cur.execute(f"SELECT username FROM users WHERE id = {userid}")
        user = cur.fetchall()
        user_name = str(user).removesuffix("',)]").removeprefix("[('")

        avatar = cur.execute(f"SELECT avatar FROM users WHERE id = {userid}")
        avatar = cur.fetchall()
        avatar = avatar.pop()
        avatar = str(avatar).removeprefix("('").removesuffix("',)")

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

    embed.set_thumbnail(url=f"https://{avatar}")
    embed.add_field(name="XP",
                    value=0)
    await message.channel.send(embed=embed)




async def check_level(math, userid, cur, discord, message):

    xp = cur.execute(f"SELECT experience FROM users WHERE id = {userid}")
    xp = cur.fetchall()
    xp = xp[0][0]

    levelraw = (xp / 6) ** (1. / 3.)
    level = math.floor(levelraw)

    #length of the progressbar = 100 / bar_length
    bar_length = 5
    filledtiles = round(round((levelraw - level) * 100) / bar_length)
    progressbar = ""
    for i in range(0, filledtiles):
        progressbar += "▓"
    
    for i in range(0, int(100 / bar_length) - filledtiles):
        progressbar += "░"
        
#    print(f"XP: {xp} -> Level: {level} ({levelraw})")
#    print(progressbar)

    try:
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

        avatar = cur.execute(f"SELECT avatar FROM users WHERE id = {userid}")
        avatar = cur.fetchall()
        avatar = avatar.pop()
        avatar = str(avatar).removeprefix("('").removesuffix("',)")

    except:
        await message.channel.send("Benutzer nicht vorhanden")
        return



    if nick == "None":
        embed = discord.Embed(title=str(user_name),
                            color=farbe)
    else:
        embed = discord.Embed(title=str(user_name),
                            color=farbe,
                            description=nick)

    embed.set_thumbnail(url=f"https://{avatar}")
    embed.add_field(name="Level",
                    value=level,
                    inline=False)
    embed.add_field(name="Fortschritt",
                    value=f"{level} | {progressbar} | {level + 1}",
                    inline=False)
    await message.channel.send(embed=embed)

