############MODULES#############
import discord
import requests
import aiohttp
import datetime
import random
from discord.ext import commands
from random import randint
from utils.Tools import *
from core import Cog, Astroz, Context
#14
#snipe | editsnipe | tickle | kiss | hug | slap | pat | feed | pet | howgay | slots | penis | meme | cat

from pathlib import Path
import json

PICKUP_LINES = json.loads(Path("pikup.json").read_text("utf8"))


def RandomColor():
    randcolor = discord.Color(random.randint(0x000000, 0xFFFFFF))
    return randcolor


class Fun(commands.Cog):

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

    @blacklist_check()
    @ignore_check()
    @commands.command()
    async def tickle(self, ctx, user: discord.Member = None):
        if user is None:
            await ctx.send("")
        else:
            r = requests.get("https://nekos.life/api/v2/img/tickle")
            res = r.json()
            embed = discord.Embed(
                timestamp=datetime.datetime.utcnow(),
                description=f"{ctx.author.mention} tickle {user.mention}",
                color=0x2f3136)
            embed.set_image(url=res['url'])
            embed.set_footer(text=f"{ctx.guild.name}")
            await ctx.send(embed=embed)
            
    @commands.command()
    @blacklist_check()
    @ignore_check()
    @commands.bot_has_permissions(embed_links=True)
    @commands.cooldown(1, 5, commands.BucketType.member)
    @commands.max_concurrency(1, per=commands.BucketType.user)
    async def kiss(self, ctx: Context, *, member: discord.Member = None):
        """Kiss pics?"""
        async with aiohttp.ClientSession() as session:
            data = await session.get(f"{self.url}/{ctx.command.name}")

        json = await data.json()
        url = json["url"]
        em = discord.Embed(
            title=f"{ctx.author} kisses {member if member else ''}",
            color=ctx.author.color,
            timestamp=datetime.utcnow(),
        )
        em.set_image(url=url)
        em.set_footer(text=f"{ctx.author}")

        await ctx.reply(embed=em)



    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(usage="hug <member>")
    @blacklist_check()
    @ignore_check()
    async def hug(self, ctx, user: discord.Member = None):
        """Hug someone (or yourself)."""
        async with aiohttp.ClientSession() as cs:
            async with cs.get("https://some-random-api.ml/animu/hug") as r:
                res = await r.json()
                imgUrl = res["link"]
        embed = discord.Embed(
            title=
            f'{ctx.author.name} hugs {f"themselves. 😔" if user is None else f"{user.name} <a:KEKW_bruh:1033548765883289691>"}',
            color=0x2f3136,
        ).set_image(url=imgUrl)
        await ctx.send(embed=embed)

    @commands.command(name="slap",
                      help="Slap mentioned user .",
                      usage="Slap <member>")
    @blacklist_check()
    @ignore_check()
    async def slap(self, ctx, user: discord.Member = None):
        if user is None:
            await ctx.send("")
        else:
            r = requests.get("https://nekos.life/api/v2/img/slap")
            res = r.json()
            embed = discord.Embed(
                timestamp=datetime.datetime.utcnow(),
                color=0x2f3136,
                description=f"{ctx.author.mention} slapped {user.mention}",
            )
            embed.set_image(url=res['url'])
            embed.set_footer(text=f"{ctx.guild.name}")
            await ctx.send(embed=embed)

    @commands.command(name="pat",
                      help="Pat mentioned user .",
                      usage="Pat <member>")
    @blacklist_check()
    @ignore_check()
    async def pat(self, ctx, user: discord.Member = None):
        if user is None:
            await ctx.send("")
        else:
            r = requests.get("https://some-random-api.ml/animu/pat")
            res = r.json()
            embed = discord.Embed(
                timestamp=datetime.datetime.utcnow(),
                description=f"{ctx.author.mention} pats {user.mention}",
                color=0x2f3136)
            embed.set_image(url=res['url'])
            embed.set_footer(text=f"{ctx.guild.name}")
            await ctx.send(embed=embed)

    @commands.command(name="feed",
                      help="Feed mentioned user .",
                      usage="Feed <member>")
    @blacklist_check()
    @ignore_check()
    async def feed(self, ctx, user: discord.Member = None):
        if user is None:
            await ctx.send("")
        else:
            r = requests.get("https://nekos.life/api/v2/img/feed")
            res = r.json()
            embed = discord.Embed(
                timestamp=datetime.datetime.utcnow(),
                description=f"{ctx.author.mention} feeds {user.mention}",
                color=0x2f3136)
            embed.set_image(url=res['url'])
            embed.set_footer(text=f"{ctx.guild.name}")
            await ctx.send(embed=embed)

    @commands.command(name="pet", usage="Pet <member>")
    @blacklist_check()
    @ignore_check()
    async def pet(self, ctx, user: discord.Member = None):
        if user is None:
            await ctx.send("")
        else:
            r = requests.get("https://nekos.life/api/v2/img/pat")
            res = r.json()
            embed = discord.Embed(
                timestamp=datetime.datetime.utcnow(),
                description=f"{ctx.author.mention} pets {user.mention}",
                color=0x2f3136)
            embed.set_image(url=res['url'])
            embed.set_footer(text=f"{ctx.guild.name}")
            await ctx.send(embed=embed)

    @commands.command(name="howgay",
                      aliases=['gay'],
                      help="check someone gay percentage",
                      usage="Howgay <person>")
    @blacklist_check()
    @ignore_check()
    async def howgay(self, ctx, *, person):
        embed = discord.Embed(color=0x2f3136)
        responses = [
            '50', '75', '25', '1', '3', '5', '10', '65', '60', '85', '30',
            '40', '45', '80', '100', '150', '1000'
        ]
        embed.description = f'**{person} is {random.choice(responses)}% Gay** :rainbow:'
        embed.set_footer(text=f'How gay are you? - {ctx.author.name}')
        await ctx.send(embed=embed)

    @commands.command(name="howfat",
                      aliases=['fat'],
                      help="Check someone's fat percentage",
                      usage="Howfat <person>")
    @blacklist_check()
    @ignore_check()
    async def howfat(self, ctx, *, person):
        embed = discord.Embed(color=0x2f3136)
        responses = {
            '5': 'Slim',
            '10': 'Lean',
            '20': 'Average',
            '25': 'Healthy',
            '30': 'Chubby',
            '40': 'Overweight',
            '50': 'Obese',
            '60': 'Very Obese',
            '70': 'Extremely Obese',
            '80': 'Morbidly Obese',
            '90': 'Super Obese',
            '100': 'Ultra Obese'
        }
        fat_percentage = random.choice(list(responses.keys()))
        fat_name = responses[fat_percentage]
        embed.description = f"**{person} is {fat_name}**"
        embed.set_footer(text=f"How fat are you? - {ctx.author.name}")
        await ctx.send(embed=embed)

    @commands.command(name="howtall",
                      aliases=['height'],
                      help="Check someone's height",
                      usage="Howtall <person>")
    @blacklist_check()
    @ignore_check()
    async def howtall(self, ctx, *, person):
        embed = discord.Embed(color=0x2f3136)
        heights = {
            'minion': 'Short like a minion',
            'short': 'Short',
            'average': 'Average height',
            'tall': 'Tall',
            'giant': 'Giant (reaching for the clouds)'
        }
        height_category = random.choice(list(heights.keys()))
        height_description = heights[height_category]
        embed.description = f"**{person} is {height_description}**"
        embed.set_footer(text=f"How tall are you? - {ctx.author.name}")
        await ctx.send(embed=embed)

    @commands.command(name="iq",
                      aliases=['howsmart'],
                      help="Check someone's IQ",
                      usage="IQ <person>")
    @blacklist_check()
    @ignore_check()
    async def iq(self, ctx, *, person):
        embed = discord.Embed(color=0x2f3136)
        iq_scores = {
            'genius': 160,
            'very_high': 140,
            'above_average': 120,
            'average': 100,
            'below_average': 80,
            'very_low': 60,
            'not_sure': 'Unknown',
            'dumb': '0',
            'slow': '40'

        }
        iq_category = random.choice(list(iq_scores.keys()))
        iq_value = iq_scores[iq_category]
        embed.description = f"**{person}'s IQ is {iq_value}** 🧠"
        embed.set_footer(text=f"How smart are you? - {ctx.author.name}")
        await ctx.send(embed=embed)

    @commands.command(name="job",
                      aliases=['profession'],
                      help="Check someone's profession",
                      usage="Job <person>")
    @blacklist_check()
    @ignore_check()
    async def job(self, ctx, *, person):
        embed = discord.Embed(color=0x2f3136)
        professions = [
            "Engineer",
            "Doctor",
            "Influencer",
            "Real Estate Agent",
            "Teacher",
            "Personal Assistant (P.A.)",
            "Professional Sport Player",
            "Musician",
            "Drug Dealer",  # Note: This is illegal and unethical.
            "Uber Driver",
            "Cashier",
            "Scammer",  # Note: Also illegal and unethical.
            "Stripper",
            "Unemployment",  # Not a profession, but a situation
            "Cotton Picker"
        ]
        random_profession = random.choice(professions)
        embed.description = f"**{person}'s profession is {random_profession}**"
        embed.set_footer(text=f"What's your profession? - {ctx.author.name}")
        await ctx.send(embed=embed)

    @commands.command(name="personality",
                      aliases=['person'],
                      help="Check if someone is rude or friendly",
                      usage="Personality <person>")
    @blacklist_check()
    @ignore_check()
    async def personality(self, ctx, *, person):
        embed = discord.Embed(color=0x2f3136)
        personalities = {
            'rude': 'Rude (watch out for sharp edges)',
            'friendly': 'Friendly (a warm smile and open arms)',
            'mysterious': 'Mysterious (keeps you guessing)',
            'charming': 'Charming (smooth talker)',
            'quirky': 'Quirky (unique and delightful)',
            'aloof': 'Aloof (a bit distant)',
            'optimistic': 'Optimistic (glass half full)',
            'cynical': 'Cynical (glass half empty)',
            'eccentric': 'Eccentric (coloring outside the lines)',
            'reserved': 'Reserved (quiet and thoughtful)'
        }
        personality_category = random.choice(list(personalities.keys()))
        personality_description = personalities[personality_category]
        embed.description = f"**{person} is {personality_description}**"
        embed.set_footer(text=f"What's your personality? - {ctx.author.name}")
        await ctx.send(embed=embed)

    @commands.command(name="checkbattery",
                      aliases=['battery'],
                      help="check someone's battery percentage",
                      usage="checkbattery <person>")
    @blacklist_check()
    @ignore_check()
    async def howbattery(self, ctx, *, person):
        embed = discord.Embed(color=0x2f3136)
        responses = [
            '50', '75', '25', '1', '3', '5', '10', '65', '60', '85', '30',
            '40', '45', '80', '100', '150', '1000'
        ]
        battery_percent = random.choice(responses)
        if battery_percent == '100':
            embed.description = f"**{person}'s battery is charged to a magical 100%!**"
        else:
            embed.description = f"**{person} has {battery_percent}% battery remaining. Charge up!**"
        embed.set_footer(text=f"How's your battery? - {ctx.author.name}")
        await ctx.send(embed=embed)

    @commands.command(name="randomquestion",
                      aliases=['question'],
                      help="get a random question",
                      usage="randomquestion")
    async def random_question(self, ctx):
        questions = [
            "What impact do you think artificial intelligence will have on the job market in the next decade?",
            "If you could travel back in time to any historical event, which one would you choose and why?",
            "What's the most interesting book you've read recently?",
            "If you could have any superpower, what would it be and how would you use it?",
            "What's your favorite memory from childhood?",
            "If you could visit any country in the world, where would you go?",
            "What's the best piece of advice you've ever received?",
            "If you could meet any famous person (dead or alive), who would it be?",
            "What's a skill you'd like to learn or improve?",
            "What's your favorite way to relax and unwind?",
            "If you could have dinner with any fictional character, who would it be?",
            "What's a hobby or interest you've always wanted to pursue?",
            "What's something you're grateful for today?",
            "If you could change one thing about the world, what would it be?",
            "What's a goal you're currently working towards?",
            "What's a topic you'd love to learn more about?",
            "If you could time travel to the future, what year would you visit?",
            "What's a fun fact about yourself?",
            "What's a challenge you've overcome?",
            "If you could invent a new holiday, what would it celebrate?",
            "What's the most adventurous thing you've ever done?",
            "If you could instantly master any musical instrument, which one would you choose?",
            "What's a movie or TV show that you can watch over and over again without getting bored?",
            "If you could have a conversation with any historical figure, who would it be and what would you ask them?",
            "What's your favorite type of cuisine, and why?",
            "If you could live in any fictional world, which one would you pick?",
            "What's a skill you wish you had learned earlier in life?",
            "If you could switch lives with someone for a day, who would it be and why?",
            "What's the best piece of advice you've ever received from a friend or family member?",
            "If you could visit any natural wonder (e.g., Grand Canyon, Northern Lights), where would you go?",
            "What's a book that has had a significant impact on your perspective?",
            "If you could time travel to witness any historical event, which one would you choose?",
            "What's a hobby or interest you've recently taken up or want to explore?",
            "If you could eliminate one daily annoyance, what would it be?",
            "What's a place you've always dreamed of traveling to?",
            "If you could attend any major event (past or future), what would it be?",
            "What's a childhood memory that still brings a smile to your face?",
            "If you could meet any fictional character in real life, who would it be?",
            "What's a goal you've set for yourself this year?",
            "If you could invent a new flavor of ice cream, what would it taste like?"
        ]
        random_question = random.choice(questions)
        await ctx.send(f"Here's a random question: **{random_question}**!")

    @commands.command(name="slots")
    @blacklist_check()
    @ignore_check()
    async def slots(self, ctx):
        emojis = "🍎🍊🍐🍋🍉🍇🍓🍒"
        a = random.choice(emojis)
        b = random.choice(emojis)
        c = random.choice(emojis)
        slotmachine = f"[ {a} {b} {c} ]\n{ctx.author.mention}"
        if (a == b == c):
            await ctx.send(embed=discord.Embed(
                title="Slot machine",
                description=f"{slotmachine} All Matching! You Won!",
                color=0x2f3136))
        elif (a == b) or (a == c) or (b == c):
            await ctx.send(embed=discord.Embed(
                title="Slot machine",
                description=f"{slotmachine} 2 Matching! You Won!",
                color=0x2f3136))
        else:
            await ctx.send(embed=discord.Embed(
                title="Slot machine",
                description=f"{slotmachine} No Matches! You Lost!",
                color=0x2f3136))

    @commands.command(name="penis",
                      aliases=['dick'],
                      help="Check someone`s dick`s size .",
                      usage="Dick [member]")
    @blacklist_check()
    @ignore_check()
    async def penis(self, ctx, user: discord.Member = None):
        if user is None:
            user = ctx.author
        size = random.randint(1, 15)
        dong = ""
        for _i in range(0, size):
            dong += "="
        em = discord.Embed(title=f"**{user}'s** Dick size",
                           description=f"8{dong}D",
                           color=0x2f3136)
        em.set_footer(text=f'whats {user} dick size?')
        await ctx.send(embed=em)

    @commands.command(name="meme", help="give you a meme", usage="meme")
    @blacklist_check()
    @ignore_check()
    async def meme(self, ctx):
        embed = discord.Embed(title="""Take some memes""", color=0x2f3136)
        async with aiohttp.ClientSession() as cs:
            async with cs.get(
                    'https://www.reddit.com/r/dankmemes/new.json?sort=hot'
            ) as r:
                res = await r.json()
                embed.set_image(url=res['data']['children'][random.randint(
                    0, 25)]['data']['url'])
                embed.set_footer(text=f'Random Meme:')
                #embed.set_footer(text=f'Random Meme:')
                await ctx.send(embed=embed)

    @commands.command(name="cat", usage="cat")
    @blacklist_check()
    @ignore_check()
    async def cat(self, ctx):
        embed = discord.Embed(title="""Here's a cat""", color=0x2f3136)
        async with aiohttp.ClientSession() as cs:
            async with cs.get('http://aws.random.cat/meow') as r:
                res = await r.json()
                embed.set_image(url=res['file'])
                embed.set_footer(text=f'Random Cats:')
                await ctx.send(embed=embed)

    @commands.hybrid_command(name="iplookup",
                             aliases=['ip', 'ipl'],
                             help="shows info about an ip",
                             usage="Iplookup [ip]")
    @blacklist_check()
    @ignore_check()
    async def iplookup(self, ctx, *, ip):
        async with aiohttp.ClientSession() as a:
            async with a.get(f"http://ipwhois.app/json/{ip}") as b:
                c = await b.json()
                try:
                    coordj = ''.join(f"{c['latitude']}" + ", " +
                                     f"{c['longitude']}")
                    embed = discord.Embed(
                        title="IP: {}".format(ip),
                        description=
                        f"```txt\n\nLocation Info:\nIP: {ip}\nIP Type: {c['type']}\nCountry, Country code: {c['country']} ({c['country_code']})\nPhone Number Prefix: {c['country_phone']}\nRegion: {c['region']}\nCity: {c['city']}\nCapital: {c['country_capital']}\nLatitude: {c['latitude']}\nLongitude: {c['longitude']}\nLat/Long: {coordj} \n\nTimezone Info:\nTimezone: {c['timezone']}\nTimezone Name: {c['timezone_name']}\nTimezone (GMT): {c['timezone_gmt']}\nTimezone (GMT) offset: {c['timezone_gmtOffset']}\n\nContractor/Hosting Info:\nASN: {c['asn']}\nISP: {c['isp']}\nORG: {c['org']}\n\nCurrency:\nCurrency type: {c['currency']}\nCurrency Code: {c['currency_code']}\nCurrency Symbol: {c['currency_symbol']}\nCurrency rates: {c['currency_rates']}\nCurrency type (plural): {c['currency_plural']}```",
                        color=0x2f3136)
                    embed.set_footer(
                        text='Thanks For Using Incite',
                        icon_url=
                        "https://cdn.discordapp.com/avatars/1251900087932817471/37e598149a590bec31c732ee263960fd.png?size=1024"
                    )
                    await ctx.send(embed=embed)
                except KeyError:
                    embed = discord.Embed(
                        description=
                        "KeyError has occured, perhaps this is a bogon IP address, or invalid IP address?",
                        color=0x2f3136)
                    await ctx.send(embed=embed)


############################




    @commands.command()
    async def pickupline(self, ctx: Context) -> None:
        """
        Gives you a random pickup line.
        Note that most of them are very cheesy.
        """
        random_line = random.choice(PICKUP_LINES["lines"])
        embed = discord.Embed(
            title=":cheese: Your pickup line :cheese:",
            description=random_line["line"],
            color=ctx.author.color,
        )
        embed.set_thumbnail(
            url=random_line.get("image", PICKUP_LINES["placeholder"]))
        await ctx.send(embed=embed)
