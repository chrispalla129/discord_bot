import os
from commands import russian
import discord
import youtube_dl
from discord import FFmpegAudio
from dotenv import load_dotenv
from discord.ext import commands
from discord.ext.commands import has_permissions, CheckFailure

load_dotenv()
token = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

# bot init
bot = commands.Bot('$')


# really more of a litmus test than anything, connor is the math guy for real tho.
@bot.command(name='connor')
async def connor(ctx):
    response = "The math man himself"
    await ctx.send(response)


# russian roulette game
@bot.command(name='roulette')
async def roulette(ctx, param="", punishment=""):
    sID = -1

    for channel in bot.get_all_channels():
        if channel.name.lower() == "games" or channel.name.lower() == "stuff": sID = channel.id

    '''if sID == -1:
        await ctx.send("Please make a text channel called 'games' for the bot to output into!")
        return
'''
    channel = ctx.channel
    if channel != ctx.channel:
        await ctx.send("Please use the 'games' channel for this!")
        return

    if param == "init":
        await russian.init(ctx, channel, punishment)
    elif param == "join":
        await russian.join(ctx, channel)
    elif param == "start":
        await russian.start(channel)
    elif param == "pull":
        await russian.bang(ctx, channel)
    elif param == "help" or param == "":
        await ctx.send("Welcome to russian roulette!\nInitialize the game with '$roulette init'.\nYou can specify "
                       "the punishment by adding 'ban', 'kick' or 'fun' after 'init' as well. \nOnce done, "
                       "players can join the game with '$roulette join'.\nOnce you have two or more players, start "
                       "the game with '$roulette start.\nAt this point, the bot will tell you who is up. Use "
                       "$roulette to pull the trigger, and see who loses! Good luck! ")
    else: await ctx.send("Wrong command.")


@roulette.error
async def roulette_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send("I can't kick you")


@bot.command(name="hey")
async def hey(ctx):
    voice = await ctx.message.author.voice.channel.connect()
    file = ffmpeg
    player = await voice.play(create_ytdl_player('https://www.youtube.com/watch?v=UAEpClFyGKU'))
    player.start()
    while not player.isDone():
        await asyncio.sleep(1)
    player.stop()
    await voice.disconnect()


@bot.command()
async def join(ctx):
    channel = ctx.author.voice.channel
    await channel.connect()

@bot.command()
async def leave(ctx):
    await ctx.voice_client.disconnect()


# command to kick a given user.
@bot.command(name='kick')
@has_permissions(administrator=True, manage_messages=True, manage_roles=True)
async def mod_kick(ctx, member: discord.Member, *, reason=None):
    await ctx.send(f"{member.mention} will now die")
    try:
        await member.kick(reason=reason)
        await ctx.send(f"{member.mention} is gone.")
    except MissingPermissions:
        await ctx.send(f"{member.mention} is too powerful")


# command to kick yourself from the server
@bot.command(name="sudoku")
async def sudoku(ctx):
    await ctx.message.author.kick()


@sudoku.error
async def sudoku_error(ctx):
    await ctx.send("You are too powerful to die.")


bot.run(token)