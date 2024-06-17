import discord
from discord.ext import commands

class hacker11111111111(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    """Welcome commands"""
  
    def help_custom(self):
		      emoji = '<:Incite_Server:1251971256342024322>'
		      label = "Server Commands"
		      description = "Show You Server Commands"
		      return emoji, label, description

    @commands.group()
    async def __Server__(self, ctx: commands.Context):
        """`setup` , `setup staff` , `setup mod` , `setup sm` , `setup homie` , `setup admin` , `setup config` , `staff` , `mod` , `sm` , `homie` , `admin` , `remove staff` , `remove mod` , `remove sm` , `remove homie` , `remove admin` , `ar` , `ar create` , `ar delete` , `ar edit` , `ar config` """

