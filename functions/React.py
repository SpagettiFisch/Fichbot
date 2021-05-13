async def ReacT(random, ChannelID, CommandChannelID, message):
    react = random.randint(0, 500)
    if str(message.author) == "Reyana#7046":
        await message.add_reaction("🍞")
    elif react == 249:
        if int(ChannelID) != int(CommandChannelID):
            await message.add_reaction("🧐")