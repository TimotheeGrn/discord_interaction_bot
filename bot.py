import discord
from discord.ext import commands
from discord import app_commands
import calendar
import time
import random
import datetime

your_discord_server_id = "place your discord server id here (whithout "")"
ts = calendar.timegm(time.gmtime())


intents = discord.Intents().all()
bot = commands.Bot(command_prefix="!", intents=intents)


intents.message_content = True
intents.guilds = True
intents.members = True

client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)


@bot.event
async def on_ready():
    print("Bot running with:")
    print("Username: ", bot.user.name)
    print("User ID: ", bot.user.id)

    try:
        synced = await bot.tree.sync(guild=discord.Object(id=your_discord_server_id))
        print("Synced", len(synced), "commands")
    except Exception as e:
        print(e)
    await bot.change_presence(activity=discord.Game(name="Open Security"))


@bot.tree.command(guild=discord.Object(id=your_discord_server_id),
                  name="help", description="Commande d'aide du bot")
async def help_slash(interaction: discord.Interaction):
    await interaction.response.send_message("```Ceci est le bot officiel du serveur Discord Open Security.\nLe bot est encore en développement et a été développé par @_yueag.```", ephemeral=True)

@bot.tree.command(guild=discord.Object(id=your_discord_server_id), name="website", description="Afficher l'url de notre site")
async def website_slash(interaction: discord.Interaction):
    await interaction.response.send_message(f"Salut {interaction.user.display_name},\nVoici l'url de notre site : http://open-security.rf.gd/", ephemeral=True)

@bot.tree.command(guild=discord.Object(id=your_discord_server_id), name="avatar", description="Affiche ton avatar")
async def avatar_slash(interaction: discord.Interaction):
    await interaction.response.send_message(interaction.user.display_avatar, ephemeral=True)

#@bot.tree.command(guild=discord.Object(id=1230881650829951078), name="mp", description="mp")
#async def mp_slash(interaction: discord.Interaction):
#    await interaction.user.send("hi")
#    await interaction.response.send_message(f"Un message privé t'a été envoyé {interaction.user.display_name}!", ephemeral=True)



@bot.tree.command(guild=discord.Object(id=your_discord_server_id), name="suggest", description="Faire une suggestion")
async def suggest_slash(interaction: discord.Interaction, suggest: str):
    await interaction.response.send_message(f"{interaction.user.mention} propose une suggestion.\n Sa suggestion :\n```{suggest}```")



@bot.tree.command(guild=discord.Object(id=your_discord_server_id), name="set_presence", description="Configurer la rich presence du bot")
async def set_presence(interaction: discord.Interaction, état: str):
    new_activity = discord.Activity(
        type=discord.ActivityType.playing,
        name=état,
    )
    await bot.change_presence(activity=new_activity)
    await interaction.response.send_message("Présence mise à jour !", ephemeral=True)


bot.run('your discord bot token')
