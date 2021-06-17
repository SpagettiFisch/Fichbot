import discord, json
from functions import if_abfragen
c = open("BotFiles/config.json")
json_data = json.load(c)
token = json_data["token"]

class MyClient(discord.Client):

    async def on_ready(self):
        await if_abfragen.if_ready(client)

    async def on_message(self, message):
        await if_abfragen.if_message(message, client)

    async def on_message_edit(self, before, after):
        await if_abfragen.if_edit(before, after, client)

    async def on_message_delete(self, message):
        await if_abfragen.if_delete(message, client)

client = MyClient()
client.run(token)