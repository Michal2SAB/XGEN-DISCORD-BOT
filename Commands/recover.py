# Importing some necessary modules
import discord
from discord.ext.commands import Bot
from discord.ext import commands
from discord.ext import *
import requests
from requests.exceptions import Timeout

@commands.command(aliases=['lostacc', 'lost', 'recov'])
async def recover(ctx, email):
    requests.packages.urllib3.disable_warnings()
    try:    
        PostData = {"email": email}
        URLData = requests.post("https://secure.xgenstudios.com/ballistick/recover.php", data=PostData, timeout=10, verify=False).text
 
        if "Check" in URLData:
            await ctx.send("Check your e-mail for further instructions on how to reset your password.")
        elif "associated":
            await ctx.send("There is no account associated with that e-mail address.")
        else:
            await ctx.send("Something went wrong, try again.")
        
    except Timeout:
        await ctx.send(ctx.message.author.mention + " Your request timed out, try again.")
    except Exception as Error:
        print(Error)

# Make the command load & work
def setup(bot):
    bot.add_command(recover)

@recover.error
async def recover_error(error, ctx):
    return await error.send(error.message.author.mention + " Format: !recover [email]")
