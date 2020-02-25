import os
import random
import discord
from dotenv import load_dotenv
from discord.ext import commands
from discord.ext.commands import has_permissions, CheckFailure
from src import Client

global leader
global bulletPos
global curPos
global players
global state
global is_up


async def init(ctx):
    global leader
    global bulletPos
    global curPos
    global state

    if state is None:
        ctx.send("Game already in progress.")
        return

    # only leader can begin game
    leader = ctx.message.author

    # bullet position and firing position, firing position will increment until it wraps during play
    bulletPos = random.randint(1, 6)
    curPos = random.randint(1, 6)
    state = "join"
    await ctx.send("Game Initialized! Join with '--roulette join' to play.")


async def join(ctx):
    global players
    global state

    if state == "join": players.append(ctx.message.author)
    elif state is None: await ctx.send("Game not initialized. Please use '--roulette init' first.")
    elif state == "in progress": await ctx.send("Game already in progress.")
    else: await ctx.send("Error.")


async def start(ctx):
    global is_up
    global state

    state = "in progress"
    random.shuffle(players)
    is_up = players.pop(0)
    players.append(is_up)
    await ctx.send(f"@{is_up} is up.")


async def bang(ctx):
    global is_up
    global bulletPos
    global curPos

    if ctx.message.author != is_up: await ctx.message(f"It's not your turn yet @{ctx.message.author}, calm down.")
    else:
        # if you lose, you get kicked
        if bulletPos == curPos:
            await member.kick(ctx.message.author)
            await ctx.message(f"{ctx.message.author} lost")

        # increment the current position, put the next person up, and put the person who just went is at the end
        else:
            curPos += 1
            if curPos > 6: curPos = 1
            is_up = players.pop(0)
            players.append(is_up)
            await ctx.message(f"@{is_up} is up.")
