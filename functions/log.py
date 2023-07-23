async def edit_log(client, before, after, discord):
    embed = discord.Embed(title=f"{await client.fetch_user(str(before).split()[12].split('=')[1])}",
                        color=0xc41616)
    embed.set_thumbnail(url=f"{await client.fetch_user(str(before).split()[12].split('=')[1]).avatar_url}")

    embed.add_field(name="Vorher",
                    value=before.content,
                    inline=False)

    embed.add_field(name="Nachher",
                    value=str(after.content))

    await str(before).split()[12].split('=')[1].send(embed=embed)


async def delete_log(client, message, discord):
    embed = discord.Embed(title=f"{message.author}",
                        color=0xc41616)
    embed.set_thumbnail(url=f"{message.author.avatar_url}")

    embed.add_field(name="Nachricht",
                    value=message.content,
                    inline=False)

    await (await client.fetch_channel(836542316273467403)).send(embed=embed)


async def name_log(client, user, name_after, name_before, art, discord):
    embed = discord.Embed(title=f"{user}",
                        description=art,
                        color=0xc41616)
    embed.set_thumbnail(url=f"{user.avatar_url}")

    embed.add_field(name="Vorher",
                    value=name_before,
                    inline=False)

    embed.add_field(name="Nachher",
                    value=name_after)

    await (await client.fetch_channel(836542316273467403)).send(embed=embed)