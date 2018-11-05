
import discord
from discord.ext import commands
import asyncio

bot=commands.Bot(command_prefix='m!')

@bot.event
async def on_ready():
	print('The bot is ready!')
	print(bot.user.name)
	print(bot.user.id)
	print('----------------------------')

@bot.command()
async def help():
	await bot.say(''')
@bot.command()
async def hi():
	await bot.say('hello')

@bot.command()
async def you want some():
	await bot.say('no u')

@bot.command()
async def meme():
	await bot.say('SKINNY PENIS')
	@bot.command()
async def no u():
	await bot.say('listen your gay')	
	@bot.command()
async def help():
	await bot.say('owner:safey is gay
discordID 5107
commands m!
hi meme you want some no u ')	
bot.run('NTAzNDQyMTI3NjI0MjA4Mzk1.Dq26xg.j7_57wgIbB3Z8nPtyRwWS1_Kv3A')
