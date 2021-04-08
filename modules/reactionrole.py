import discord

welcome_channel_id = 782636285725900840
class MyClient(discord.Client):

    async def on_ready(self):
        welcome_channel = client.get_channel(welcome_channel_id)
        print("Ich habe mich eingeloggt. Beep Bop.")



    async def on_raw_reaction_add(self, reaction):
        guild = client.get_guild(reaction.guild_id)
        user = reaction.member
        if str(user) == client.user:
            print("aha")
            return
        elif reaction.channel_id != welcome_channel_id:
            print("falscher Channel")
            return

        if user != client.user:
            if str(reaction.emoji) == "💯":
                await user.add_roles(discord.utils.get(guild.roles, name="Animal Crossing"))
            if str(reaction.emoji) == "🟫":
                await user.add_roles(discord.utils.get(guild.roles, name="Minecraft"))
            else:
                return

    async def on_raw_reaction_remove(self, reaction):
        guild = client.get_guild(reaction.guild_id)
        userID = reaction.user_id
        print(userID)
        #print(guild)
        #print(reaction)
        user = client.get_user(int(reaction.user_id))
        print(user)


        if str(user) == client.user:
            print("aha")
            return
        elif reaction.channel_id != welcome_channel_id:
            print("Falscher Channel")
            return

        if user != client.user:
            if str(reaction.emoji) == "💯":
                await user.remove_roles(discord.utils.get(guild.roles, name="Animal Crossing"))
            if str(reaction.emoji) == "🟫":
                await user.remove_roles(discord.utils.get(guild.roles, name="Minecraft"))
            else:
                return




client = MyClient()
client.run((open('../token', 'r').read()))
