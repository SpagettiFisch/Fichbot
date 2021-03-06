async def status(Status, client, discord, s):
    try:
        if str(Status).lower().split()[1] == "game":
            await client.change_presence(
                activity=discord.Game(name=f"{str(Status).split(' ', 2)[2]}"))

        elif str(Status).lower().split()[1] == "stream":
            await client.change_presence(
                activity=discord.Streaming(name=f"{str(Status).split(' ', 2)[2]}",
                                            url=f"https://twitch.tv/{str(Status).split(' ', 2)[2]}"))

        elif str(Status).lower().split()[1] == "listen":
            await client.change_presence(
                activity=discord.Activity(type=discord.ActivityType.listening,
                                            name=f"{str(Status).split(' ', 2)[2]}"))

        elif str(Status).lower().split()[1] == "watch":
            await client.change_presence(
                activity=discord.Activity(type=discord.ActivityType.watching,
                                            name=f"{str(Status).split(' ', 2)[2]}"))
        elif "mode='w'" in str(s):
            s.writelines(str(Status))
    except:
        print("Ungültiger Status")
        pass