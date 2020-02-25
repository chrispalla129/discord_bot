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

    if state is None:
        ctx.send("Game already in progress.")
        return

    leader = ctx.message.author
    bulletPos = random.randint(1, 6)
    curPos = random.randint(1, 6)
    state = "join"
    await ctx.send("Game Initialized! Join with '--roulette join' to play.")


async def join(ctx, member: discord.Member):
    global players
    global state

    if state == "join": players.append(member)
    elif state is None: await ctx.send("Game not initialized. Please use 'roulette init' first.")
    elif state == "in progress": await ctx.send("Game already in progress.")
    else: await ctx.send("Error.")

async def play(ctx):


async def start(ctx):




