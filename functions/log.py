async def edit_log(client, before, after, discord):
    mod_channel = await client.fetch_channel(836542316273467403)
    content = before.content
    userid = str(before).split()[12]
    userid = userid.split('=')[1]
    user = await client.fetch_user(userid)
    avatar = user.avatar_url


    embed = discord.Embed(title=f"{user}",
                        color=0xc41616)
    embed.set_thumbnail(url=f"{avatar}")

    embed.add_field(name="Vorher",
                    value=content,
                    inline=False)

    embed.add_field(name="Nachher",
                    value=str(after.content))

    await mod_channel.send(embed=embed)


async def delete_log(client, message, discord):
    mod_channel = await client.fetch_channel(836542316273467403)
    content = message.content
    user = message.author
    avatar = user.avatar_url


    embed = discord.Embed(title=f"{user}",
                        color=0xc41616)
    embed.set_thumbnail(url=f"{avatar}")

    embed.add_field(name="Nachricht",
                    value=content,
                    inline=False)

    await mod_channel.send(embed=embed)
