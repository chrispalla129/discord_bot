import os
import random
import discord

from dotenv import load_dotenv
from discord.ext import commands
from discord.ext.commands import has_permissions, CheckFailure

# copyright julius breindl and not christian cp palladino
global leader
global bulletPos
global curPos
players = list()
state = None
global is_up
global punishment


async def init(ctx, channel, punish):
    global leader
    global bulletPos
    global curPos
    global state
    global punishment

    if punish == "ban": punishment = "ban"

    elif punish == "kick": punishment = "kick"
    else: punishment = channel.send(f"{ctx.message.author.mention} has been deaded")

    if state is not None:
        await channel.send("Game already in progress.")
        return

    # only leader can begin game
    leader = ctx.message.author

    # bullet position and firing position, firing position will increment until it wraps during play
    bulletPos = random.randint(1, 6)
    curPos = random.randint(1, 6)
    state = "join"
    players.append(leader)
    await channel.send("Game Initialized! Join with '$roulette join' to play.")


async def join(ctx, channel):
    global players
    global state

    if state == "join" and len(players) <= 6 and ctx.message.author not in players:
        players.append(ctx.message.author)
        await ctx.message.add_reaction("\U0001F595")
    elif state is None: await channel.send("Game not initialized. Please use '$roulette init' first.")
    elif state == "in progress": await channel.send("Game already in progress.")
    elif ctx.message.author in players: await ctx.send(f"You're already in pal {ctx.message.author.mention}")
    else: await channel.send("Error.")


async def start(channel):
    global is_up
    global state
    global players

    if state != "join":
        await channel.send("Game not in joining state. Use $roulette init first")
        return
    if len(players) < 2:
        await channel.send("Not enough players, need at least 2 to play.")
        return

    state = "in progress"
    random.shuffle(players)
    is_up = players.pop(0)
    players.append(is_up)
    await channel.send(f"{is_up.mention} is up.")


async def bang(ctx, channel):
    global is_up
    global bulletPos
    global curPos
    global state
    global punishment

    if state != "in progress":
        await channel.send("Game must be in progress.")
        return

    if ctx.message.author != is_up: await channel.send(f"It's not your turn yet {ctx.message.author.mention}, calm down.")
    else:
        # if you lose, punish
        if bulletPos == curPos:
            try:
                if punishment == "ban": await ctx.message.author.ban()
                elif punishment == "kick": await ctx.message.author.kick()
                await channel.send(f"{ctx.message.author.mention} lost")
            except:
                await ctx.send(f"{ctx.message.author.mention} lost, but I am unable to punish them. They smell really bad though.")
                print(response)
            await end()
        # increment the current position, put the next person up, and put the person who just went is at the end
        else:
            curPos += 1
            if curPos > 6: curPos = 1
            is_up = players.pop(0)
            players.append(is_up)
            await channel.send(f"{is_up.mention} is up.")


async def end():
    global leader
    global bulletPos
    global curPos
    global players
    global state
    global is_up

    leader = None
    bulletPos = None
    curPos = None
    players = list()
    state = None
    is_up = None
