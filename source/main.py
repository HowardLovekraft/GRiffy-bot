import os
import disnake
from disnake.ext import commands
from dotenv import load_dotenv
from icecream import ic

dotenv_path = "env\\env.env"
load_dotenv(dotenv_path=dotenv_path)

bot = commands.Bot(command_prefix="!", intents=disnake.Intents.all(), test_guilds=[817468953793658892])
TOKEN = os.getenv("TOKEN")

@bot.command()
@commands.is_owner()
async def load(ctx, extension):
    bot.load_extension(f"cogs.{extension}")

@bot.command()
@commands.is_owner()
async def unload(ctx, extension):
    bot.unload_extension(f"cogs.{extension}")

@bot.command()
@commands.is_owner()
async def reload(ctx, extension):
    bot.reload_extension(f"cogs.{extension}")

for filename in os.listdir("cogs"):
    if filename.endswith(".py"):
        bot.load_extension(f"cogs.{filename[:-3]}")

@bot.event
async def on_ready():
    ic(f"Bot {bot.user} is ready to work!")

bot.run(TOKEN)
