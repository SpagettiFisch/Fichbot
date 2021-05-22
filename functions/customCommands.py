async def add_command(message, cc_cur, cc_con, prefix):
    trigger = str(message.content.lower().split(' ')[1]).removeprefix(prefix)

    kommando = message.content.split(' ', 2)[2]

    cc_cur.execute(f"INSERT INTO customcommands VALUES ('{trigger}','{kommando}')")
    cc_con.commit()
    await message.channel.send("Befehl hinzugefügt")



async def check_commands(command, cc_cur, prefix, message):
    commands = cc_cur.execute(f"SELECT trigger FROM customcommands")
    commands = cc_cur.fetchall()
    for cc in commands:
        cc = str(cc).removeprefix("('").removesuffix("',)")

        if command.startswith(f"{prefix}{cc}"):
            text = cc_cur.execute(f"SELECT command FROM customcommands WHERE trigger = '{cc}'")
            text = cc_cur.fetchall()
            text = str(text).removeprefix("[('").removesuffix("',)]")

            await message.channel.send(text)