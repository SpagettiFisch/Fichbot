async def Blacklist(message, userID, command, blacklist):
    content = command.replace('.', '').replace(' ', '').replace('-', '').replace('_', '').replace('\n', '').replace(',', '')
    for word in blacklist.splitlines(False):
        if word.replace('\n', '') in content:
            await message.delete()