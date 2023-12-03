import discord

from discord import option
from discord.ext import commands
from dotenv import load_dotenv
from os import getenv

from constants import EXEC_ROLE_NAME

load_dotenv()

TOKEN = getenv("DISCORD_TOKEN")
GUILD = int(getenv("GUILD_ID"))

intents = discord.Intents.default()
intents.message_content = True
bot = discord.Bot(intents=intents)


@bot.slash_command(
    name="admin-message",
    description="Send an admin message through JamBot. The message will be sent to the specified channel.",
)
@option("message", description="The message to send.")
@option("channel", description="The channel to send the message to.")
@commands.has_role(EXEC_ROLE_NAME)
async def admin_message(ctx, message: str, channel: discord.TextChannel):
    try:
        await channel.send(message)
        ctx.respond("Message sent!")
    except Exception as e:
        print(e)
        ctx.respond("An error occurred. Please try again.")


@bot.event
async def on_ready():
    print(f"{bot.user} is ready and online!")


bot.run(TOKEN)
