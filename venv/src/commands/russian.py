import os
import random
import discord
from dotenv import load_dotenv
from discord.ext import commands
from discord.ext.commands import has_permissions, CheckFailure

global leader
global bulletPos
global curPos
global players
global state

async def init(ctx, member: discord.Member):
    global leader
    global bulletPos
    global curPos
    global state

    leader = ctx.message.author
    bulletPos = random.randint(1, 6)
    curPos = random.randint(1, 6)
    state = "join"
    await ctx.send("Game Initialized! Join with '--roulette join' to play.")


async def join(ctx, member: discord.Member):
    global players
    if state == "join": players.append(member)


async def start(ctx):

