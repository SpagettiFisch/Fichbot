async def Status(status, client, discord, s):
    try:
        if str(status).lower().split()[1] == "game":
            await client.change_presence(
                activity=discord.Game(name=f"{str(status).split(' ', 2)[2]}"))

        elif str(status).lower().split()[1] == "stream":
            await client.change_presence(
                activity=discord.Streaming(name=f"{str(status).split(' ', 2)[2]}",
                                            url=f"https://twitch.tv/{str(status).split(' ', 2)[2]}"))

        elif str(status).lower().split()[1] == "listen":
            await client.change_presence(
                activity=discord.Activity(type=discord.ActivityType.listening,
                                            name=f"{str(status).split(' ', 2)[2]}"))

        elif str(status).lower().split()[1] == "watch":
            await client.change_presence(
                activity=discord.Activity(type=discord.ActivityType.watching,
                                            name=f"{str(status).split(' ', 2)[2]}"))
        elif "mode='w'" in str(s):
            s.writelines(str(status))
    except:
        print("Ungültiger Status")
        pass