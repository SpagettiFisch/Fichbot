async def Stop(sys, client, message):
    await message.channel.send("Ja wie denn? xD \nIch könnte das ja mal probie... ")
    print("Ich geh dann mal offline")
    client.clear()
    await client.close()
    await sys.exit()

async def DM(client, command, message):
    Person = await client.fetch_user(command.split('+')[1])
    Nachricht = message.content.split('+')[2]
    await Person.send(Nachricht)
    await message.channel.send("gesendet^^")
    if not "Direct Message with" in str(message.channel):
        await message.delete()

async def KI(command, message, client):
    Channel = await client.fetch_channel(command.split('+')[1])
    Nachricht = message.content.split('+')[2]
    await Channel.send(Nachricht)
    await message.channel.send("gesendet^^")
    if not "Direct Message with" in str(message.channel):
        await message.delete()