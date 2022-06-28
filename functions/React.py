async def react(random, ChannelID, CommandChannelID, message):
    if str(message.author) == "Reyana#7046":
        await message.add_reaction("🍞")
    elif random.randint(0, 500) == 249:
        if int(ChannelID) != int(CommandChannelID):
            await message.add_reaction("🧐")