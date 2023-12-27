import os
import discord
from dotenv import load_dotenv
from discord.ext import commands


# Load discord token from environment
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

# Create discord client
client = discord.Client(intents=discord.Intents.default()) # Intents change what events our bots can respond to, for now we will use the default

@client.event # This is called a "Decorator" it signifies that this method responds to a client event with the same name as the function
async def on_ready():
    guild = client.guilds[0] # Because we are only connected to one Guild, we can get the first guild in the "guilds" list
    print(f"{client.user} is online on {guild.name}!") # Prints a message to the console when a successfuly connection is made

# Run the bot
client.run(TOKEN)

bot = commands.Bot(command_prefix='!')

@client.event
async def on_message(message):
    # ignore messages from the bot itself
    if message.author == bot.user:
        return

    # check if the message mentions the bot
    if bot.user in message.mentions:
        # send a response
        await message.channel.send("Hello, {}!".format(message.author.mention))

bot.run("MTA4ODQ1NzM1OTE0MTEwOTc5Mg.GDV2bu.WLXzpw-SDbcGvvVJsB_gNpClB4cVQNQHEzcA5s")
