import requests, time, random, sys, re, math, discord
from discord import default_permissions

async def commands(bot):
    class MyView(discord.ui.View):
        def __init__(self):
            super().__init__(timeout=None)

        @discord.ui.button(label='Cookie Run Kingdom', custom_id="cookie_run_kingdom", style=discord.ButtonStyle.primary, emoji='<:cookierunner:1124088891935309864>')
        async def crk_button_callback(self, button, interaction):
                guild = await bot.fetch_guild(828896352465190932)
                role = discord.utils.get(guild.roles, name='Cookie Run: Kingdom')
                await interaction.user.add_roles(role)
                await interaction.response.send_message('Du hast jetzt die Cookie Run Kingdom Rolle!', ephemeral=True)

        @discord.ui.button(label='Stream Benachrichtigungen', custom_id="stream_notify", style=discord.ButtonStyle.primary, emoji='<:PanPing:753530572185403453>')
        async def stream_notify_button_callback(self, button, interaction):
                guild = await bot.fetch_guild(828896352465190932)
                role = discord.utils.get(guild.roles, name='stream notify')
                await interaction.user.add_roles(role)
                await interaction.response.send_message('Du bekommst jetzt bei Streambegin einen Ping!', ephemeral=True)
        
        @discord.ui.button(label='Benachrichtigungen', custom_id="notify", style=discord.ButtonStyle.primary, emoji='📬')
        async def notify_button_callback(self, button, interaction):
                guild = await bot.fetch_guild(828896352465190932)
                role = discord.utils.get(guild.roles, name='notify')
                await interaction.user.add_roles(role)
                await interaction.response.send_message('Du bekommst jetzt bei Serverneuigkeiten einen Ping!', ephemeral=True)

        @discord.ui.button(label='Cookie Run Kingdom', custom_id="cookie_run_kingdom_remove", style=discord.ButtonStyle.danger, emoji='<:cookierunner:1124088891935309864>', row=2)
        async def crk_remove_button_callback(self, button, interaction):
                guild = await bot.fetch_guild(828896352465190932)
                role = discord.utils.get(guild.roles, name='Cookie Run: Kingdom')
                await interaction.user.remove_roles(role)
                await interaction.response.send_message('Du hast jetzt nicht mehr die Cookie Run Kingdom Rolle!', ephemeral=True)

        @discord.ui.button(label='Stream Benachrichtigungen', custom_id="stream_notify_remove", style=discord.ButtonStyle.danger, emoji='<:PanPing:753530572185403453>', row=2)
        async def stream_notify_remove_button_callback(self, button, interaction):
                guild = await bot.fetch_guild(828896352465190932)
                role = discord.utils.get(guild.roles, name='stream notify')
                await interaction.user.remove_roles(role)
                await interaction.response.send_message('Du bekommst jetzt bei Streambegin keinen Ping mehr!', ephemeral=True)
        
        @discord.ui.button(label='Benachrichtigungen', custom_id="notify_remove", style=discord.ButtonStyle.danger, emoji='📬', row=2)
        async def notify_remove_button_callback(self, button, interaction):
                guild = await bot.fetch_guild(828896352465190932)
                role = discord.utils.get(guild.roles, name='notify')
                await interaction.user.remove_roles(role)
                await interaction.response.send_message('Du bekommst jetzt bei Serverneuigkeiten keinen Ping mehr!', ephemeral=True)

    @bot.slash_command(hidden = True, role = "Fisch")
    @default_permissions(administrator=True)
    async def self_roles(ctx, text: str):
        "specify a message for the bot to send with buttons"
        await ctx.channel.send(text, view=MyView)
        await ctx.respond('success!', ephemeral=True)
        
    @bot.slash_command(hidden = True, role = "Fisch")
    @default_permissions(administrator=True)
    async def verification(ctx, id: str, emoji: str):
        "specify a message (message ID needed!) and an emoji for the verification process"
        message = await ctx.fetch_message(id)
        await message.add_reaction(emoji)
        with open('BotFiles/verification', 'w', encoding="utf-8") as f:
            f.write(f'emoji: {emoji}\nmessage_id: {id}')
        await ctx.respond('Nachricht wurde zur Verifikation hinzugefügt!', ephemeral=True)

    @bot.slash_command()
    async def verify(ctx):
        "Verify a person and gives the verify role"
        guild = await bot.fetch_guild(828896352465190932)
        role = discord.utils.get(guild.roles, name='verifiziert')
        await ctx.author.add_roles(role)
        await ctx.respond('Erfolgreich verifiziert') 

    bot.add_view(MyView())    
