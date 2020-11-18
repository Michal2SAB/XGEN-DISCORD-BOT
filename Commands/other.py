# Importing some necessary modules
import discord
from discord.ext.commands import Bot
from discord.ext import commands
from discord.ext import *
from configparser import ConfigParser
from Tools import spinners as s
import os

class Other(commands.Cog):
    def __init__(self, bot):
        self.imgs = ('inner.png', 'outer.png', 'spinner.png')
        
        # Extracting variables from config file
        config_object = ConfigParser()
        config_object.read("config.ini")
        self.AdminVar = config_object["ADMIN"]

    # Handling the apis command
    @commands.command(aliases=['apis', 'apiurls'])
    async def xgenapis(self, ctx):
        embed=discord.Embed(title="List of all useful (public) XGen API's.", description="[Create XGen Account](http://api.xgenstudios.com/?method=xgen.users.add&username=&password=)\n\n[Change XGen Username (Blastrage method)](http://api.xgenstudios.com/?method=xgen.users.changeName&username=&password=&new_username=)\n\n[Verify Your XGen Account](http://api.xgenstudios.com/?method=xgen.users.addEmail&username=&password=&email_address=)\n\n[Change Your XGen Account Password](http://api.xgenstudios.com/?method=xgen.users.changePassword&username=&password=&new_password=)\n\n[Lookup SA User Stats](http://api.xgenstudios.com/?method=xgen.stickarena.stats.get&username=)\n\n[Lookup Boxhead User Stats](http://api.xgenstudios.com/?method=xgen.boxhead.users.stats&username=)\n\n[Lookup User Stats From Other XGen Games](http://api.xgenstudios.com/?method=xgen.stats.get&username=)\n\n[Lookup Data For User's Custom Map (SA)](http://api.xgenstudios.com/?method=xgen.stickarena.maps.get&username=&slot_id=)", color=0x24262B)
        await ctx.send(embed=embed)

    # Handling the highscores command
    @commands.command(aliases=['hs', 'leaderboard', 'lb'])
    async def highscores(self, ctx):
        embed=discord.Embed(title="List Of SA Highscores", description="[Current Highscores (Season)](http://www.xgenstudios.com/stickarena/highscore/)\n\n[Current Highscores (Overall Stats)](http://www.xgenstudios.com/stickarena/highscore/?date=all)\n\n[Highscores Right Before The Reset](http://www.xgenstudios.com/stickarena/highscore/?date=2017-08-31)", color=0x24262B)
        await ctx.send(embed=embed)
    
    # Handling the forums command
    @commands.command(aliases=['forumslink', 'forum', 'discourse'])
    async def forums(self, ctx):
        await ctx.send("http://discourse.xgenstudios.com")

    # Handling the maptools command
    @commands.command(aliases=['eedok'])
    async def maptools(self, ctx):
        embed=discord.Embed(title="Map Tools By Eedok", description="[Get Custom Map's Image](http://www.xgenstudios.com/eedok/samap.html)\n\n[Update Weapons Spawn Time On Your Map](http://www.xgenstudios.com/eedok/maptimers.html)\n\n[Advanced, web-based SA Map Editor](http://stickarena.epizy.com/samap.html)", color=random.randint(0, 0xffffff))
        await ctx.send(embed=embed)

    # Handling the spinners command
    @commands.command()
    async def spinners(self, ctx):
        embed=discord.Embed(title="All spinner shortcuts for !buy command.", description="oldskool | spiral |neon | radioactive\n\nskulls | minimalist | retro | buttercup\n\nthehex | yinyang | revolution | wrongway\n\nvinyl | razorblades | hollywood | rebel\n\nchance | thepro | omega | biohazard\n\ntriskelion | 1337 | glint | theplague\n\nroflmao | brainwash | shuriken | 4thdimensions\n\naffluenza | dabomb | the8bit | flux\n\ntheofficer | solar | ouroboros | stealth\n\nbullettime | baller | wakkawakka | gearsofgore\n\npyro | assassin | globe | galaxy\n\nteabag | canttouchthis | fireworks | jaws\n\nplop | dimspinner1 | dimspinner2 | fakeassassin", color=0x24262B)
        await ctx.send(embed=embed)

    # Handling the servers command
    @commands.command()
    async def servers(self, ctx):
        embed=discord.Embed(title="All server shortcuts for !users, !games and other commands.", description="2dc - 2-Dimensional Central\n\nptc - Paper Thin City\n\nfli - Fine Line Island/Flat World\n\nuofsa - U of SA/Sticktopia\n\nmobius - Mobius Metropolis/Planar Outpost\n\neu - Europe Amsterdam\n\ncartesian - Cartesian Republic\n\nsquaresville - The main server of boxhead", color=0x24262B)
        await ctx.send(embed=embed)

    # Handling the staff command
    @commands.command(aliases=['admins', 'mods'])
    async def staff(self, ctx):
        await ctx.send("http://forums.xgenstudios.com/g/moderators")

    # Handling the help command
    @commands.command()
    async def help(self, ctx):
        await ctx.send(f"Hi. I'm a Discord Bot for Stick Arena and XGenStudios. I was created by Michał and I'm currently hosted by {self.AdminVar['ADMIN']}. Type !commands for the list of all commands.")

    # Handling the commands command
    @commands.command(aliases=['commands', 'command'])
    async def cmds(self, ctx):
        embed=discord.Embed(title="All Commands", description="!stats - Lookup stats for a Stick Arena account.\n\n!statsbbh - Lookup stats for a Boxhead account.\n\n!create - Create a new XGen account.\n\n!namechange - Change your XGen username.\n\n!users - Check who's currently online in a specified Stick Arena server.\n\n!games - Check what games are currently available in a specified Stick Arena server.\n\n!gameinfo - Check info on a specified game in a specified Stick Arena server.\n\n!creator - Check who created a specified game in a specified Stick Arena server.\n\n!find - Search for user through all of Stick Arena servers.\n\n!totalstats - Check who's online in every single Stick Arena server and what games are currently opened.\n\n!servers - Server names for !users, !games, !creator and !gameinfo commands.\n\n!check - Check how a color code will look on Stick Arena (Name text and oldskool)\n\n!randomcolor - Generate random sa color (to request only working color code, type !randomcolor valid)\n\n!buy - Buy any Stick Arena spinner of any color code.\n\n!spinners - List of SA spinners that you can purchase with bot. (For !buy command).\n\n!validate - Check if a color code will have a red glitch in Stick Arena lobby.\n\n!staff - Give link to current XGen staff forum thread.\n\n!forums - Request for XGen forums link.\n\n!highscores - Request for all Stick Arena highscores links.\n\n!xgenapis - Request a list of all (useful) XGen apis.\n\n!maptools - Request for available Stick Arena map tools.\n\n!prems - Lookup premium items for a boxhead account.\n\n!oldstats - Check stats for an account before the dumb reset.\n\n!oldstatsbbh - Check stats for a boxhead account before the reset.", color=0x24262B)
        embed.add_field(name="Bot Creator", value="Michal")
        await ctx.send(embed=embed)

    # Handling the pro command
    @commands.command(aliases=['thepro'])
    async def pro(self, ctx, RGB1, RGB2):
        try:
            theImage = s.gen(RGB1, RGB2, 'pro')
            await ctx.message.channel.send(file=discord.File(theImage))
            for imag in self.imgs:
                os.remove(imag)
        except Exception as e:
            print(e)

    # Handling the oldskool command
    @commands.command(aliases=['os'])
    async def oldskool(self, ctx, RGB1, RGB2):
        try:
            theImage = s.gen(RGB1, RGB2, 'oldskool')
            await ctx.message.channel.send(file=discord.File(theImage))
            for imag in self.imgs:
                os.remove(imag)
        except Exception as e:
            print(e)

# Load the command & make it work
def setup(bot):
    bot.add_cog(Other(bot))
