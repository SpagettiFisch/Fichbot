async def add_command(message, cur, con, prefix):
    trigger = str(message.content.lower().split(' ')[1]).removeprefix(prefix)

    kommando = message.content.split(' ', 2)[2]

    cur.execute(f"INSERT INTO customcommands VALUES ('{trigger}','{kommando}')")
    con.commit()
    await message.channel.send("Befehl hinzugefügt")



async def check_commands(command, cur, prefix, message):
    commands = cur.execute(f"SELECT trigger FROM customcommands")
    commands = cur.fetchall()
    for cc in commands:
        cc = str(cc).removeprefix("('").removesuffix("',)")

        if command.startswith(f"{prefix}{cc}"):
            text = cur.execute(f"SELECT command FROM customcommands WHERE trigger = '{cc}'")
            text = cur.fetchall()
            text = str(text).removeprefix("[('").removesuffix("',)]")

            await message.channel.send(text)



async def delete_command(cur, con, message, prefix, command, sqlite3):
    befehl = command.split()[1]
    befehl = befehl.removeprefix(prefix)
    try:
        cur.execute(f"DELETE FROM customcommands WHERE trigger = '{befehl}'")
        con.commit()
        await message.channel.send(f"Der Befehl {befehl} wurde erfolgreich gelöscht")
    except sqlite3.OperationalError:
        await message.channel.send(f"Kein Befehl mit dem Namen {befehl}")
    except:
        await message.channel.send("Da ist ein Fehler aufgetreten :/")



async def list_commands(cur, message, discord, prefix):
    commands = cur.execute(f"SELECT trigger FROM customcommands")
    commands = cur.fetchall()

    embed = discord.Embed(title="Custom Commands",
                        description="Hier werden alle aktiven custom Commands aufgelistet.",
                        color=0x9721eb)

    for cc in commands:
        cc = str(cc).removeprefix("('").removesuffix("',)")

        text = cur.execute(f"SELECT command FROM customcommands WHERE trigger = '{cc}'")
        text = cur.fetchall()
        text = str(text).removeprefix("[('").removesuffix("',)]")

        befehl = f"{prefix}{cc}"

        embed.add_field(name=befehl,
                        value=f"{text}",
                        inline=False)
    
    await message.channel.send(embed=embed)

async def reactionEvent(con, cur, bot, slash):
    @bot.command()
    async def init(ctx: slash.Context, name, channel_id, info, emoji, event, role_id = None, message_id = 0):
        reaction_role = False
        if str(event) == 'custom':
            pass
        elif str(event) == 'role':
            reaction_role = True
        else:
            await ctx.respong("Unknown Event")

        if reaction_role:
            cur.execute(f'''INSERT OR IGNORE INTO reactionRoles VALUES ('{name}', {channel_id}, {message_id}, '{info}', '{emoji}', {role_id})''')
            con.commit()
            channel = await bot.fetch_channel(channel_id)
            await channel.send(info)
            await ctx.message.delete()
