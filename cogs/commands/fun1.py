import discord
from discord.ext import commands


class hacker111111111(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    """Fun commands"""
  
    def help_custom(self):
		      emoji = '<:Incite_Fun:1252170258727440384> '
		      label = "Fun Commands"
		      description = "Show You Fun Commands"
		      return emoji, label, description

    @commands.group()
    async def __Fun__(self, ctx: commands.Context):
        """` tickle` , `kiss` , `hug` , `slap` , `pat` , `feed` , `pet` , `howgay`, `howtall`, `howfat`, `howsmart`, `battery`, `person`, `iq` , `job`, `slots` , ` penis` , `meme` , `cat` , `iplookup`"""
