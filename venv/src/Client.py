import os
from commands import russian
import discord
from dotenv import load_dotenv
from discord.ext import commands
from discord.ext.commands import has_permissions, CheckFailure

load_dotenv()
token = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

# bot init
bot = commands.Bot('--')


@bot.command(name = 'connor')
async def connor(ctx):
    response = "The math man himself"
    await ctx.send(response)


@bot.command(name = 'roulette')
async def roulette(ctx, param):
    if param == "init":
        ctx
    elif param == "join":
        ctx
    elif param == "start":
        ctx
    else: await ctx.send("Wrong command.")
    await russian.hello(ctx)
    #await ctx.send(param)

@bot.command(name = 'kick')
@has_permissions(administrator=True, manage_messages=True, manage_roles = True)
async def mod_kick(ctx, member: discord.Member, *, reason = None):
    await ctx.send(f'{member} is a bitch')
    await member.kick(reason = reason)
    await ctx.send(f'{member} is gone.')

@mod_kick.error
async def mod_ban_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send('get the perm bub.')

bot.run(token)
