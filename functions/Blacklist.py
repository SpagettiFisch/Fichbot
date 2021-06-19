async def Blacklist(message, userID, command, blacklist):
    count = 0
    Inhalt = command.replace('.', '').replace(' ', '').replace('-', '').replace('_', '').replace('\n', '').replace(',', '')
    checking = True 
    while True:
        if checking == True:
            B = blacklist.splitlines(False)
            Anzahl = len(B)
            bw = B.pop(count)
            count += 1
            if bw.replace('\n', '') in Inhalt:
                await message.delete()
            elif count == Anzahl:
                checking = False
        else:
            return
