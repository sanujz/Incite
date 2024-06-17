import discord
from discord.utils import *
import aiohttp
from core import Astroz, Cog
import json
from utils.Tools import *
from discord.ext import commands



headers = {'Authorization': 'Bot OTMxODE2Njk0Nzg2MTcwODkw.GkzHLL.7XEh31zCKnMRUmSxDIg6P4m-HMitx7zdWlJ-RE'}

class Autorole2(Cog):
    def __init__(self, bot: Astroz):
        self.bot = bot



    @Cog.listener()
    async def on_member_join(self, member):
        data = getDB(member.guild.id)
        arb = data["autorole"]["bots"]
        arh = data["autorole"]["humans"]
        if arb == []:
            return
        else:
            if member.bot != True:
                async with aiohttp.ClientSession(headers=headers, connector=None) as session:
                    for role in arh:
                        try:
                            async with session.put(f"https://discord.com/api/v10/guilds/{member.guild.id}/members/{member.id}/roles/{int(role)}", json={'reason': "Incite | Auto Role"}) as req:
                                print(req.status)
                        except:
                            pass
                    
            elif member.bot:
                async with aiohttp.ClientSession(headers=headers, connector=None) as session:
                    for role in arb:
                        try:
                            async with session.put(f"https://discord.com/api/v10/guilds/{member.guild.id}/members/{member.id}/roles/{int(role)}", json={'reason': "Incite | Auto Role"}) as req:
                                print(req.status)
                        except:
                            pass