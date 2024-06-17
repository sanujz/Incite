import discord
from discord import app_commands
from discord.ext import commands
from discord.ext.commands import Context
from utils.Tools import *
import json


class Server(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    async def add_role(self, *, role: int, member: discord.Member):
        if member.guild.me.guild_permissions.manage_roles:
            role = discord.Object(id=int(role))
            await member.add_roles(role, reason="Incite | Role Added ")

    async def remove_role(self, *, role: int, member: discord.Member):
        if member.guild.me.guild_permissions.manage_roles:
            role = discord.Object(id=int(role))
            await member.remove_roles(role, reason="Incite | Role Removed")
 

    @commands.hybrid_command(name="staff",
                             description="Gives the staff role to the user .",
                             aliases=['official'],
                             help="Gives the staff role to the user .")
    @blacklist_check()
    @ignore_check()
    @commands.has_permissions(administrator=True)
    async def _staff(self, context: Context, member: discord.Member) -> None:
        if data := getConfig(context.guild.id):
            lol = data['reqrole']
            own = data['staff']  
            role = context.guild.get_role(own)
            if data["reqrole"] != None:
                req = context.guild.get_role(lol)
                if context.author == context.guild.owner or req in context.author.roles:
                    if data["staff"] != None:
                        if role not in member.roles:
                            await self.add_role(role=own, member=member)
                            
                            hacker = discord.Embed(
                description=
                f"<:Incite_Success:1251971018033987654> | Successfully Given <@&{own}> To {member.mention}",
                color=0x2f3136)
                            hacker.set_author(name=f"{context.author}",
                              icon_url=f"{context.author.avatar}")
                            await context.send(embed=hacker)
                        elif role in member.roles:
                            await self.remove_role(role=own, member=member)
                            hacker6 = discord.Embed(
                description=
                f"<:Incite_Success:1251971018033987654> | Successfully Removed <@&{own}> From {member.mention}",
                color=0x2f3136)
                            hacker6.set_author(name=f"{context.author}",
                              icon_url=f"{context.author.avatar}")
                            await context.send(embed=hacker6)                             
                    else:
                        hacker1 = discord.Embed(
                description=
                f"<:Incite_Failure:1251971011855913011> | Staff role is not setuped in {context.guild.name}",
                color=0x2f3136)
                        hacker1.set_author(name=f"{context.author}",
                               icon_url=f"{context.author.avatar}")
                        hacker1.set_thumbnail(url=f"{context.author.avatar}")
                        await context.send(embed=hacker1)
                else:
                    hacker3 = discord.Embed(
                description=
                f"<:Incite_Failure:1251971011855913011> | You need {req.mention} to run this command .",
                color=0x2f3136)
                    hacker3.set_author(name=f"{context.author}",
                               icon_url=f"{context.author.avatar}")
                    
                    await context.send(embed=hacker3)

            else:
                hacker4 = discord.Embed(
                description=
                f"<:Incite_Failure:1251971011855913011> | Req role is not setuped in {context.guild.name}",
                color=0x2f3136)
                hacker4.set_author(name=f"{context.author}",
                               icon_url=f"{context.author.avatar}")
                
                await context.send(embed=hacker4)  


    @commands.hybrid_command(name="mod",
                             description="Gives the mod role to the user .",
                             aliases=['moderator', 'ma'],
                             help="Gives the mod role to the user .")
    @blacklist_check()
    @ignore_check()
    @commands.has_permissions(administrator=True)
    async def _mod(self, context: Context, member: discord.Member) -> None:
        if data := getConfig(context.guild.id):
            lol = data['reqrole']
            own = data['mod']  
            role = context.guild.get_role(own)
            if data["reqrole"] != None:
                req = context.guild.get_role(lol)
                if context.author == context.guild.owner or req in context.author.roles:
                    if data["mod"] != None:
                        if role not in member.roles:
                            await self.add_role(role=own, member=member)
                            
                            hacker = discord.Embed(
                description=
                f"<:Incite_Success:1251971018033987654> | Successfully Given <@&{own}> To {member.mention}",
                color=0x2f3136)
                            hacker.set_author(name=f"{context.author}",
                              icon_url=f"{context.author.avatar}")
                            await context.send(embed=hacker)
                        elif role in member.roles:
                            await self.remove_role(role=own, member=member)
                            hacker6 = discord.Embed(
                description=
                f"<:Incite_Success:1251971018033987654> | Successfully Removed <@&{own}> From {member.mention}",
                color=0x2f3136)
                            hacker6.set_author(name=f"{context.author}",
                              icon_url=f"{context.author.avatar}")
                            await context.send(embed=hacker6)       
                    else:
                        hacker1 = discord.Embed(
                description=
                f"<:Incite_Failure:1251971011855913011> | Mod role is not setuped in {context.guild.name}",
                color=0x2f3136)
                        hacker1.set_author(name=f"{context.author}",
                               icon_url=f"{context.author.avatar}")
                        hacker1.set_thumbnail(url=f"{context.author.avatar}")
                        await context.send(embed=hacker1)
                else:
                    hacker3 = discord.Embed(
                description=
                f"<:Incite_Failure:1251971011855913011> | You need {req.mention} to run this command .",
                color=0x2f3136)
                    hacker3.set_author(name=f"{context.author}",
                               icon_url=f"{context.author.avatar}")
                    
                    await context.send(embed=hacker3)

            else:
                hacker4 = discord.Embed(
                description=
                f"<:Incite_Failure:1251971011855913011> | Req role is not setuped in {context.guild.name}",
                color=0x2f3136)
                hacker4.set_author(name=f"{context.author}",
                               icon_url=f"{context.author.avatar}")
                
                await context.send(embed=hacker4)  
    
    @commands.hybrid_command(name="homie",
                             description="Gives the homie role to the user .",
                             help="Gives the homie role to the user .")
    @blacklist_check()
    @ignore_check()
    @commands.has_permissions(administrator=True)
    async def _homie(self, context: Context, member: discord.Member) -> None:
        if data := getConfig(context.guild.id):
            lol = data['reqrole']
            own = data['homie']  
            role = context.guild.get_role(own)
            if data["reqrole"] != None:
                req = context.guild.get_role(lol)
                if context.author == context.guild.owner or req in context.author.roles:
                    if data["homie"] != None:
                        if role not in member.roles:
                            await self.add_role(role=own, member=member)
                            
                            hacker = discord.Embed(
                description=
                f"<:Incite_Success:1251971018033987654> | Successfully Given <@&{own}> To {member.mention}",
                color=0x2f3136)
                            hacker.set_author(name=f"{context.author}",
                              icon_url=f"{context.author.avatar}")
                            await context.send(embed=hacker)
                        elif role in member.roles:
                            await self.remove_role(role=own, member=member)
                            hacker6 = discord.Embed(
                description=
                f"<:Incite_Success:1251971018033987654> | Successfully Removed <@&{own}> From {member.mention}",
                color=0x2f3136)
                            hacker6.set_author(name=f"{context.author}",
                              icon_url=f"{context.author.avatar}")
                            await context.send(embed=hacker6)       
                    else:
                        hacker1 = discord.Embed(
                description=
                f"<:Incite_Failure:1251971011855913011> | homie role is not setuped in {context.guild.name}",
                color=0x2f3136)
                        hacker1.set_author(name=f"{context.author}",
                               icon_url=f"{context.author.avatar}")
                        hacker1.set_thumbnail(url=f"{context.author.avatar}")
                        await context.send(embed=hacker1)
                else:
                    hacker3 = discord.Embed(
                description=
                f"<:Incite_Failure:1251971011855913011> | You need {req.mention} to run this command .",
                color=0x2f3136)
                    hacker3.set_author(name=f"{context.author}",
                               icon_url=f"{context.author.avatar}")
                    
                    await context.send(embed=hacker3)

            else:
                hacker4 = discord.Embed(
                description=
                f"<:Incite_Failure:1251971011855913011> | Req role is not setuped in {context.guild.name}",
                color=0x2f3136)
                hacker4.set_author(name=f"{context.author}",
                               icon_url=f"{context.author.avatar}")
                
                await context.send(embed=hacker4)


    @commands.hybrid_command(name="adminadd",
                             description="Gives the admin role to the user .",
                             help="Gives the admin role to the user .")
    @blacklist_check()
    @commands.has_permissions(administrator=True)
    async def _adminadd(self, context: Context, member: discord.Member) -> None:
        if data := getConfig(context.guild.id):
            lol = data['reqrole']
            own = data['adminadd']
            role = context.guild.get_role(own)  
            if data["reqrole"] != None:
                req = context.guild.get_role(lol)
                if context.author == context.guild.owner or req in context.author.roles:
                    if data["adminadd"] != None:
                        if role not in member.roles:
                            await self.add_role(role=own, member=member)
                            
                            hacker = discord.Embed(
                description=
                f"<:Incite_Success:1251971018033987654> | Successfully Given <@&{own}> To {member.mention}",
                color=0x2f3136)
                            hacker.set_author(name=f"{context.author}",
                              icon_url=f"{context.author.avatar}")
                            await context.send(embed=hacker)
                        elif role in member.roles:
                            await self.remove_role(role=own, member=member)
                            hacker6 = discord.Embed(
                description=
                f"<:Incite_Success:1251971018033987654> | Successfully Removed <@&{own}> From {member.mention}",
                color=0x2f3136)
                            hacker6.set_author(name=f"{context.author}",
                              icon_url=f"{context.author.avatar}")
                            await context.send(embed=hacker6)       
                    else:
                        hacker1 = discord.Embed(
                description=
                f"<:Incite_Failure:1251971011855913011> | Admin role is not setuped in {context.guild.name}",
                color=0x2f3136)
                        hacker1.set_author(name=f"{context.author}",
                               icon_url=f"{context.author.avatar}")
                        hacker1.set_thumbnail(url=f"{context.author.avatar}")
                        await context.send(embed=hacker1)
                else:
                    hacker3 = discord.Embed(
                description=
                f"<:Incite_Failure:1251971011855913011> | You need {req.mention} to run this command .",
                color=0x2f3136)
                    hacker3.set_author(name=f"{context.author}",
                               icon_url=f"{context.author.avatar}")
                    
                    await context.send(embed=hacker3)

            else:
                hacker4 = discord.Embed(
                description=
                f"<:Incite_Failure:1251971011855913011> | Req role is not setuped in {context.guild.name}",
                color=0x2f3136)
                hacker4.set_author(name=f"{context.author}",
                               icon_url=f"{context.author.avatar}")
                
                await context.send(embed=hacker4)

    
    @commands.hybrid_command(name="sm",
                             description="Gives the server manager role to the user .",
                             aliases=['servermanager'],
                             help="Gives the server manager role to the user .")
    @ignore_check()
    @blacklist_check()
    @commands.has_permissions(administrator=True)
    async def _sm(self, context: Context, member: discord.Member) -> None:
        if data := getConfig(context.guild.id):
            lol = data['reqrole']
            own = data['servermanager'] 
            role = context.guild.get_role(own) 
            if data["reqrole"] != None:
                req = context.guild.get_role(lol)
                if context.author == context.guild.owner or req in context.author.roles:
                    if data["servermanager"] != None:
                        if role not in member.roles:
                            await self.add_role(role=own, member=member)
                            
                            hacker = discord.Embed(
                description=
                f"<:Incite_Success:1251971018033987654> | Successfully Given <@&{own}> To {member.mention}",
                color=0x2f3136)
                            hacker.set_author(name=f"{context.author}",
                              icon_url=f"{context.author.avatar}")
                            await context.send(embed=hacker)
                        elif role in member.roles:
                            await self.remove_role(role=own, member=member)
                            hacker6 = discord.Embed(
                description=
                f"<:Incite_Success:1251971018033987654> | Successfully Removed <@&{own}> From {member.mention}",
                color=0x2f3136)
                            hacker6.set_author(name=f"{context.author}",
                              icon_url=f"{context.author.avatar}")
                            await context.send(embed=hacker6)       
                    else:
                        hacker1 = discord.Embed(
                description=
                f"<:Incite_Failure:1251971011855913011> | Server manager role is not setuped in {context.guild.name}",
                color=0x2f3136)
                        hacker1.set_author(name=f"{context.author}",
                               icon_url=f"{context.author.avatar}")
                        hacker1.set_thumbnail(url=f"{context.author.avatar}")
                        await context.send(embed=hacker1)
                else:
                    hacker3 = discord.Embed(
                description=
                f"<:Incite_Failure:1251971011855913011> | You need {req.mention} to run this command .",
                color=0x2f3136)
                    hacker3.set_author(name=f"{context.author}",
                               icon_url=f"{context.author.avatar}")
                    
                    await context.send(embed=hacker3)

            else:
                hacker4 = discord.Embed(
                description=
                f"<:Incite_Failure:1251971011855913011> | Req role is not setuped in {context.guild.name}",
                color=0x2f3136)
                hacker4.set_author(name=f"{context.author}",
                               icon_url=f"{context.author.avatar}")
                
                await context.send(embed=hacker4)


    
    @commands.hybrid_group(name="setup",
                           description="Setups custom roles for the server .",
                           help="Setups custom roles for the server .")
    @blacklist_check()
    @ignore_check()
    @commands.has_permissions(administrator=True)
    async def set(self, context: Context):
        if context.subcommand_passed is None:
            await context.send_help(context.command)
            context.command.reset_cooldown(context)

    @set.command(name="staff",
                 description="Setups staff role for the server .",
                 help="Setups staff role for the server .")
    @blacklist_check()
    @ignore_check()
    @commands.has_permissions(administrator=True)
    @app_commands.describe(role="Role to be added")
    async def staff(self, context: Context, role: discord.Role) -> None:
        if context.author == context.guild.owner or context.author.top_role.position > context.guild.me.top_role.position:
            if data := getConfig(context.guild.id):

                data['staff'] = role.id
                updateConfig(context.guild.id, data)
                hacker = discord.Embed(
                    description=
                    f"<:Incite_Success:1251971018033987654> | Successfully Setuped `Staff` Role To {role.mention}",
                    color=0x2f3136)
                hacker.set_author(name=f"{context.author}",
                                  icon_url=f"{context.author.avatar}")
                hacker.set_thumbnail(url=f"{context.author.avatar}")
                await context.send(embed=hacker)
        else:
            hacker5 = discord.Embed(
                description=
                """```yaml\n - You must have administrator permission.\n - Your top role should be above my top role.```""",
                color=0x2f3136)
            hacker5.set_author(name=f"{context.author.name}",
                               icon_url=f"{context.author.avatar}")
            await context.send(embed=hacker5)

    @set.command(name="mod",
                 description="Setups mod role for the server .",
                 help="Setups mod role for the server .")
    @blacklist_check()
    @ignore_check()
    @commands.has_permissions(administrator=True)
    @app_commands.describe(role="Role to be added")
    async def mod(self, context: Context, role: discord.Role) -> None:
        if context.author == context.guild.owner or context.author.top_role.position > context.guild.me.top_role.position:
            if data := getConfig(context.guild.id):

                data['mod'] = role.id
                updateConfig(context.guild.id, data)
                hacker = discord.Embed(
                    description=
                    f"<:Incite_Success:1251971018033987654> | Successfully Setuped `mod` Role To {role.mention}",
                    color=0x2f3136)
                hacker.set_author(name=f"{context.author}",
                                  icon_url=f"{context.author.avatar}")
                hacker.set_thumbnail(url=f"{context.author.avatar}")
                await context.send(embed=hacker)
        else:
            hacker5 = discord.Embed(
                description=
                """```yaml\n - You must have administrator permission.\n - Your top role should be above my top role.```""",
                color=0x2f3136)
            hacker5.set_author(name=f"{context.author.name}",
                               icon_url=f"{context.author.avatar}")
            await context.send(embed=hacker5)

    @set.command(name="homie",
                 description="Setups homie role for the server .",
                 help="Setups homie role for the server .")
    @blacklist_check()
    @ignore_check()
    @commands.has_permissions(administrator=True)
    @app_commands.describe(role="Role to be added")
    async def homie(self, context: Context, role: discord.Role) -> None:
        if context.author == context.guild.owner or context.author.top_role.position > context.guild.me.top_role.position:
            if data := getConfig(context.guild.id):

                data['homie'] = role.id
                updateConfig(context.guild.id, data)
                hacker = discord.Embed(
                    description=
                    f"<:Incite_Success:1251971018033987654> | Successfully Setuped `homie` Role To {role.mention}",
                    color=0x2f3136)
                hacker.set_author(name=f"{context.author}",
                                  icon_url=f"{context.author.avatar}")
                hacker.set_thumbnail(url=f"{context.author.avatar}")
                await context.send(embed=hacker)
        else:
            hacker5 = discord.Embed(
                description=
                """```yaml\n - You must have administrator permission.\n - Your top role should be above my top role.```""",
                color=0x2f3136)
            hacker5.set_author(name=f"{context.author.name}",
                               icon_url=f"{context.author.avatar}")
            await context.send(embed=hacker5)

    @set.command(name="adminadd",
                 description="Setups admin role for the server .",
                 help="Setups admin role for the server .")
    @blacklist_check()
    @ignore_check()
    @commands.has_permissions(administrator=True)
    @app_commands.describe(role="Role to be added")
    async def adminadd(self, context: Context, role: discord.Role) -> None:
        if context.author == context.guild.owner or context.author.top_role.position > context.guild.me.top_role.position:
            if data := getConfig(context.guild.id):

                data['adminadd'] = role.id
                updateConfig(context.guild.id, data)
                hacker = discord.Embed(
                    description=
                    f"<:Incite_Success:1251971018033987654> | Successfully Setuped `adminadd` Role To {role.mention}",
                    color=0x2f3136)
                hacker.set_author(name=f"{context.author}",
                                  icon_url=f"{context.author.avatar}")
                hacker.set_thumbnail(url=f"{context.author.avatar}")
                await context.send(embed=hacker)
        else:
            hacker5 = discord.Embed(
                description=
                """```yaml\n - You must have administrator permission.\n - Your top role should be above my top role.```""",
                color=0x2f3136)
            hacker5.set_author(name=f"{context.author.name}",
                               icon_url=f"{context.author.avatar}")
            await context.send(embed=hacker5)

    @set.command(name="sm",
                 description="Setups server manager role for the server .",
                 help="Setups server manager role for the server .")
    @blacklist_check()
    @ignore_check()
    @commands.has_permissions(administrator=True)
    @app_commands.describe(role="Role to be added")
    async def sm(self, context: Context, role: discord.Role) -> None:
        if context.author == context.guild.owner or context.author.top_role.position > context.guild.me.top_role.position:
            if data := getConfig(context.guild.id):

                data['servermanager'] = role.id
                updateConfig(context.guild.id, data)
                hacker = discord.Embed(
                    description=
                    f"<:Incite_Success:1251971018033987654> | Successfully Setuped `sm` Role To {role.mention}",
                    color=0x2f3136)
                hacker.set_author(name=f"{context.author}",
                                  icon_url=f"{context.author.avatar}")
                hacker.set_thumbnail(url=f"{context.author.avatar}")
                await context.send(embed=hacker)
        else:
            hacker5 = discord.Embed(
                description=
                """```yaml\n - You must have administrator permission.\n - Your top role should be above my top role.```""",
                color=0x2f3136)
            hacker5.set_author(name=f"{context.author.name}",
                               icon_url=f"{context.author.avatar}")
            await context.send(embed=hacker5)



    @set.command(name="config",
                 description="Shows custom role settings for the server .",
                 aliases=['show'],
                 help="Shows custom role settings for the server .")
    @blacklist_check()
    @ignore_check()
    @commands.has_permissions(administrator=True)
    async def rsta(self, context: Context) -> None:
        if data := getConfig(context.guild.id):
            staff = data['staff']
            mod = data['mod']
            homie = data['homie']
            adminadd = data['adminadd']
            sms = data['servermanager']

            if data["staff"] != None:
                stafff = discord.utils.get(context.guild.roles, id=staff)
                staffr = stafff.mention
            else:
                staffr = "Staff role is not set"
            if data["mod"] != None:
                modl = discord.utils.get(context.guild.roles, id=mod)
                modr = modl.mention
            else:
                modr = "Mod role is not set"
            if data["homie"] != None:
                homiep = discord.utils.get(context.guild.roles, id=homie)
                homier = homiep.mention
            else:
                homier = "Homie role is not set"
            if data["adminadd"] != None:
                adminaddt = discord.utils.get(context.guild.roles, id=adminadd)
                adminaddr = adminaddt.mention
            else:
                adminaddr = "Admin role is not set"
            if data["servermanager"] != None:
                servermanagerr = discord.utils.get(context.guild.roles, id=sms)
                servermanagerr = servermanagerr.mention
            else:
                servermanagerr = "Server manager role is not set"



            embed = discord.Embed(
                title=f"Custom roles Settings For {context.guild.name}",
                color=0x2f3136)
            embed.add_field(
                name="<:Incite_Arrow:1252133991281070110> Staff Role:",
                value=f"{staffr}",
                inline=False)
            embed.add_field(
                name="<:Incite_Arrow:1252133991281070110> Mod Role:",
                value=f"{modr}",
                inline=False)
            embed.add_field(name="<:Incite_Arrow:1252133991281070110> Homie Role:",
                            value=f"{homier}",
                            inline=False)
            embed.add_field(
                name="<:Incite_Arrow:1252133991281070110> Admin Role:",
                value=f"{adminaddr}",
                inline=False)
            embed.add_field(
                name="<:Incite_Arrow:1252133991281070110> Servermanager Role:",
                value=f"{servermanagerr}",
                inline=False)
            #embed.set_thumbnail(url = f"{context.author.avatar}")
            await context.send(embed=embed)



    @set.command(name="reqrole",
                 description="setup reqrole for custom role commands .",
                 aliases=['r'],
                 help="setup reqrole for custom role commands .")
    @blacklist_check()
    @ignore_check()
    @commands.cooldown(1, 4, commands.BucketType.user)
    @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
    @commands.guild_only()
    @commands.has_permissions(administrator=True)
    async def req_role(self, ctx, role: discord.Role):
        data = getConfig(ctx.guild.id)
        data["reqrole"] = role.id
        if ctx.author == ctx.guild.owner or ctx.author.top_role.position > ctx.guild.me.top_role.position:
            updateConfig(ctx.guild.id, data)
            hacker4 = discord.Embed(
                color=0x2f3136,
                
                description=
                f"<:Incite_Success:1251971018033987654> | Reqiured role to run custom role commands is set to {role.mention} For {ctx.guild.name}"
            )
            await ctx.reply(embed=hacker4, mention_author=False)

        else:
            hacker5 = discord.Embed(
                description=
                """```yaml\n - You must have administrator permission.\n - Your top role should be above my top role.```""",
                color=0x2f3136)
            hacker5.set_author(name=f"{ctx.author.name}",
                               icon_url=f"{ctx.author.avatar}")
            await ctx.reply(embed=hacker5, mention_author=False)


            




    @commands.hybrid_group(name="remove",
                           description="remove roles",
                           aliases=['r'])
    @blacklist_check()
    @ignore_check()
    @commands.has_permissions(administrator=True)
    async def remove(self, context: Context):
        if context.subcommand_passed is None:
            await context.send_help(context.command)
            context.command.reset_cooldown(context)

    @remove.command(name="staff",
                    description="Removes the staff role from the member .",
                    aliases=['official'],
                    help="Removes the staff role from the member .")
    @blacklist_check()
    @ignore_check()
    @commands.has_permissions(administrator=True)
    @app_commands.describe(member="member to remove staff")
    async def rstaff(self, context: Context, member: discord.Member) -> None:
        if data := getConfig(context.guild.id):
            role = data['staff']
            await self.remove_role(role=role, member=member)
            hacker = discord.Embed(
                description=
                f"<:Incite_Success:1251971018033987654> | Successfully Removed <@&{role}> From {member.mention}",
                color=0x2f3136)
            hacker.set_author(name=f"{context.author}",
                              icon_url=f"{context.author.avatar}")
            hacker.set_thumbnail(url=f"{context.author.avatar}")
            await context.send(embed=hacker)

    @remove.command(name="mod",
                    description="Removes the mod role from the member .",
                    aliases=['moderator', 'ma'],
                    hep="Removes the mod role from the member .")
    @blacklist_check()
    @ignore_check()
    @commands.has_permissions(administrator=True)
    @app_commands.describe(member="member to remove mod")
    async def rmod(self, context: Context, member: discord.Member) -> None:
        if data := getConfig(context.guild.id):
            role = data['mod']
            await self.remove_role(role=role, member=member)
            hacker = discord.Embed(
                description=
                f"<:Incite_Success:1251971018033987654> | Successfully Removed <@&{role}> From {member.mention}",
                color=0x2f3136)
            hacker.set_author(name=f"{context.author}",
                              icon_url=f"{context.author.avatar}")
            hacker.set_thumbnail(url=f"{context.author.avatar}")
            await context.send(embed=hacker)

    @remove.command(name="homie",
                    description="Removes the homie role from the member .",
                    help="Removes the homie role from the member .")
    @blacklist_check()
    @ignore_check()
    @commands.has_permissions(administrator=True)
    @app_commands.describe(member="member to remove homie")
    async def rhomie(self, context: Context, member: discord.Member) -> None:
        if data := getConfig(context.guild.id):
            role = data['homie']
            await self.remove_role(role=role, member=member)
            hacker = discord.Embed(
                description=
                f"<:Incite_Success:1251971018033987654> | Successfully Removed <@&{role}> From {member.mention}",
                color=0x2f3136)
            hacker.set_author(name=f"{context.author}",
                              icon_url=f"{context.author.avatar}")
            hacker.set_thumbnail(url=f"{context.author.avatar}")
            await context.send(embed=hacker)

    @remove.command(name="adminadd",
                    description="Removes the admin role from the member .",
                    help="Removes the admin role from the member .")
    @blacklist_check()
    @ignore_check()
    @commands.has_permissions(administrator=True)
    @app_commands.describe(member="member to remove admin")
    async def radminadd(self, context: Context, member: discord.Member) -> None:
        if data := getConfig(context.guild.id):
            role = data['adminadd']
            await self.remove_role(role=role, member=member)
            hacker = discord.Embed(
                description=
                f"<:Incite_Success:1251971018033987654> | Successfully Removed <@&{role}> From {member.mention}",
                color=0x2f3136)
            hacker.set_author(name=f"{context.author}",
                              icon_url=f"{context.author.avatar}")
            hacker.set_thumbnail(url=f"{context.author.avatar}")
            await context.send(embed=hacker)

    @remove.command(name="sm",
                    description="Removes the server manager role from the member .",
                    aliases=['servermanager'],
                    help="Removes the server manager role from the member .")
    @blacklist_check()
    @ignore_check()
    @commands.has_permissions(administrator=True)
    @app_commands.describe(member="member to remove sm")
    async def rsm(self, context: Context, member: discord.Member) -> None:
        if data := getConfig(context.guild.id):
            role = data['servermanager']
            await self.remove_role(role=role, member=member)
            hacker = discord.Embed(
                description=
                f"<:Incite_Success:1251971018033987654> | Successfully Removed <@&{role}> From {member.mention}",
                color=0x2f3136)
            hacker.set_author(name=f"{context.author}",
                              icon_url=f"{context.author.avatar}")
            hacker.set_thumbnail(url=f"{context.author.avatar}")
            await context.send(embed=hacker)



    @commands.group(name="autoresponder",
                    invoke_without_command=True,
                    aliases=['ar'])
    @blacklist_check()
    @ignore_check()
    async def _ar(self, ctx: commands.Context):
        if ctx.subcommand_passed is None:
            await ctx.send_help(ctx.command)
            ctx.command.reset_cooldown(ctx)

    @_ar.command(name="create")
    @commands.has_permissions(administrator=True)
    @blacklist_check()
    @ignore_check()
    async def _create(self, ctx, name, *, message):
        if ctx.author == ctx.guild.owner or ctx.author.top_role.position > ctx.guild.me.top_role.position:
            with open("autoresponse.json", "r") as f:
                autoresponse = json.load(f)
            numbers = []
            if str(ctx.guild.id) in autoresponse:
                for autoresponsecount in autoresponse[str(ctx.guild.id)]:
                    numbers.append(autoresponsecount)
                if len(numbers) >= 20:
                    hacker6 = discord.Embed(
                    
                    description=
                    f"<:Incite_Failure:1251971011855913011> You can\'t add more than 20 autoresponses in {ctx.guild.name}",
                    color=0x2f3136)
                    hacker6.set_author(name=f"{ctx.author}",
                                   icon_url=f"{ctx.author.avatar}")
                    hacker6.set_thumbnail(url=f"{ctx.author.avatar}")
                    return await ctx.send(embed=hacker6)
            if str(ctx.guild.id) in autoresponse:
                if name in autoresponse[str(ctx.guild.id)]:
                    hacker = discord.Embed(
                    
                    description=
                    f"<:Incite_Failure:1251971011855913011> The autoresponse with the `{name}` is already in {ctx.guild.name}",
                    color=0x2f3136)
                    hacker.set_author(name=f"{ctx.author}",
                                  icon_url=f"{ctx.author.avatar}")
                    hacker.set_thumbnail(url=f"{ctx.author.avatar}")
                    return await ctx.send(embed=hacker)
            if str(ctx.guild.id) in autoresponse:
                autoresponse[str(ctx.guild.id)][name] = message
                with open("autoresponse.json", "w") as f:
                    json.dump(autoresponse, f, indent=4)
                hacker1 = discord.Embed(
                description=
                f"<a:black_Lnl:1002204507985432666> | Successfully Created Autoresponder in {ctx.guild.name} with the `{name}`",
                color=0x2f3136)
                hacker1.set_author(name=f"{ctx.author}",
                               icon_url=f"{ctx.author.avatar}")
                hacker1.set_thumbnail(url=f"{ctx.author.avatar}")
                return await ctx.reply(embed=hacker1)
            data = {
            name: message,
            }
            autoresponse[str(ctx.guild.id)] = data
            with open("autoresponse.json", "w") as f:
                json.dump(autoresponse, f, indent=4)
                hacker2 = discord.Embed(

                description=
                f"<a:black_Lnl:1002204507985432666> | Successfully Created Autoresponder  in {ctx.guild.name} with the `{name}`",
                color=0x2f3136)
                hacker2.set_author(name=f"{ctx.author}",
                               icon_url=f"{ctx.author.avatar}")
                hacker2.set_thumbnail(url=f"{ctx.author.avatar}")
                return await ctx.reply(embed=hacker2)
            
        else:
            hacker5 = discord.Embed(
                description=
                """```yaml\n - You must have administrator permission.\n - Your top role should be above my top role.```""",
                color=0x2f3136)
            hacker5.set_author(name=f"{ctx.author.name}",
                               icon_url=f"{ctx.author.avatar}")

            await ctx.send(embed=hacker5, mention_author=False)
                
                    
                    

            
            
        

    @_ar.command(name="delete")
    @commands.has_permissions(administrator=True)
    @blacklist_check()
    @ignore_check()
    async def _delete(self, ctx, name):
        with open("autoresponse.json", "r") as f:
            autoresponse = json.load(f)

        if str(ctx.guild.id) in autoresponse:
            if name in autoresponse[str(ctx.guild.id)]:
                del autoresponse[str(ctx.guild.id)][name]
                with open("autoresponse.json", "w") as f:
                    json.dump(autoresponse, f, indent=4)
                hacker1 = discord.Embed(
                    
                    description=
                    f"<a:black_Lnl:1002204507985432666> | Successfully Deleted Autoresponder in {ctx.guild.name} with the `{name}`",
                    color=0x2f3136)
                hacker1.set_author(name=f"{ctx.author}",
                                   icon_url=f"{ctx.author.avatar}")
                hacker1.set_thumbnail(url=f"{ctx.author.avatar}")
                return await ctx.reply(embed=hacker1)
            else:
                hacker = discord.Embed(
                    
                    description=
                    f"<:Incite_Failure:1251971011855913011> No Autoresponder Found With The Name `{name}` In {ctx.guild.name}",
                    color=0x2f3136)
                hacker.set_author(name=f"{ctx.author}",
                                  icon_url=f"{ctx.author.avatar}")
                hacker.set_thumbnail(url=f"{ctx.author.avatar}")
                return await ctx.reply(embed=hacker)
        else:
            hacker2 = discord.Embed(
                
                description=
                f"<:Incite_Failure:1251971011855913011> There is no Autoresponder in {ctx.guild.name}",
                color=0x2f3136)
            hacker2.set_author(name=f"{ctx.author}",
                               icon_url=f"{ctx.author.avatar}")
            hacker2.set_thumbnail(url=f"{ctx.author.avatar}")
            return await ctx.reply(embed=hacker2)

    @_ar.command(name="config")
    @commands.has_permissions(administrator=True)
    @blacklist_check()
    @ignore_check()
    async def _config(self, ctx):
        with open("autoresponse.json", "r") as f:
            autoresponse = json.load(f)
        autoresponsenames = []
        guild = ctx.guild
        if str(ctx.guild.id) in autoresponse:
            for autoresponsecount in autoresponse[str(ctx.guild.id)]:
                autoresponsenames.append(autoresponsecount)
            embed = discord.Embed(color=0x2f3136)
            st, count = "", 1
            for autoresponse in autoresponsenames:
                st += f"`{'0' + str(count) if count < 20 else count}. `    **{autoresponse.upper()}**\n"
                test = count
                count += 1

                embed.title = f"{test} Autoresponders In {guild}"
        embed.description = st
        embed.set_author(name=f"{ctx.author}", icon_url=f"{ctx.author.avatar}")
        embed.set_thumbnail(url=f"{ctx.author.avatar}")
        await ctx.send(embed=embed)

    @_ar.command(name="edit")
    @commands.has_permissions(administrator=True)
    @blacklist_check()
    async def _edit(self, ctx, name, *, message):
        with open("autoresponse.json", "r") as f:
            autoresponse = json.load(f)
        if str(ctx.guild.id) in autoresponse:
            if name in autoresponse[str(ctx.guild.id)]:
                autoresponse[str(ctx.guild.id)][name] = message
                with open("autoresponse.json", "w") as f:
                    json.dump(autoresponse, f, indent=4)
                hacker1 = discord.Embed(
                    
                    description=
                    f"<a:black_Lnl:1002204507985432666> | Successfully Edited Autoresponder in {ctx.guild.name} with the `{name}`",
                    color=0x2f3136)
                hacker1.set_author(name=f"{ctx.author}",
                                   icon_url=f"{ctx.author.avatar}")
                hacker1.set_thumbnail(url=f"{ctx.author.avatar}")
                return await ctx.send(embed=hacker1)
        else:
            hacker2 = discord.Embed(
                
                description=
                f"<:Incite_Failure:1251971011855913011> No Autoresponder Found With The Name `{name}` In {ctx.guild.name}",
                color=0x2f3136)
            hacker2.set_author(name=f"{ctx.author}",
                               icon_url=f"{ctx.author.avatar}")
            hacker2.set_thumbnail(url=f"{ctx.author.avatar}")
            return await ctx.send(embed=hacker2)

    @commands.Cog.listener()
    async def on_message(self, message: discord.Message) -> None:
        if message.author == self.bot.user:
            return
        try:
            if message is not None:
                with open("autoresponse.json", "r") as f:
                    autoresponse = json.load(f)
                if str(message.guild.id) in autoresponse:
                    ans = autoresponse[str(
                        message.guild.id)][message.content.lower()]
                    return await message.channel.send(ans)
        except:
            pass
