import re
import discord
from pathlib import Path
from discord.ext import commands

intents = discord.Intents.all()
bot = commands.Bot( command_prefix = "!", intents = intents )

Drinks = [ "coke", "sprite", "coca-cola", "coca cola", "lemonade", "fanta", "beer", "surge", "vault", "water",
"tropicana", "bleach", "vodka", "dr pepper", "dr. pepper", "mtn dew", "mountain dew", "gfuel", "g fuel", "wine",
"alcohol", "milk", "juice", "respawn", "lava", "magma", "gasoline", "oil" ]
GoodDrinks = [ "pep", "pepsi", "bepis" ]

def findWord( word ):
	return re.compile( r'\b({0})\b'.format( word ), flags = re.IGNORECASE ).search

@bot.event
async def on_ready():
	print( "Logged in as {0}!".format( bot.user ) )

@bot.event
async def on_message( message ):
	if message.author.bot: return
	if message.content.startswith( "!pepsiman" ):
		await bot.process_commands( message )
		return
	if "sprite cranberry" in message.content.lower():
		await message.channel.send( "Well, it's not Pepsi, but I'll let it slide.\nhttps://i.ytimg.com/vi/J8JoBttIy_c/maxresdefault.jpg" )
		return
	for item in Drinks:
		if findWord( item )( message.content ) is not None:
			await message.channel.send( "YOU FOOL! HOW DARE YOU DRINK " + item.upper() + " INSTEAD OF PEPSI!" )
			Path( "data/drinkoffenses" ).mkdir( parents = True, exist_ok = True )
			offenseDir = "data/drinkoffenses/" + str( message.author.id ) + ".txt"
			if Path( offenseDir ).exists():
				previousOffenses = open( offenseDir, "r" )
				offenseNum = int( previousOffenses.read() )
				previousOffenses.close()
				offenseFile = open( offenseDir, "w+" )
				offenseFile.write( str( offenseNum + 1 ) )
				offenseFile.close()
			else:
				offenseFile = open( offenseDir, "w+" )
				offenseFile.write( "1" )
				offenseFile.close()
			return
	for item in GoodDrinks:
		if item in message.content.lower():
			await message.channel.send( "https://i.pinimg.com/originals/30/da/4e/30da4e74b1d08a8b65c1dcbbae44b546.jpg" )
			return

@bot.group( invoke_without_command = True, ignore_extra = True )
async def pepsiman( ctx ):
	await ctx.send( "Yes? What do you want?" )

@pepsiman.command()
async def givepepsi( ctx ):
	await ctx.send( "https://i.kym-cdn.com/photos/images/original/000/995/571/fab.gif" )

@pepsiman.command()
async def totaloffenses( ctx, member: discord.Member = None ):
	if member is not None:
		if Path( "data/drinkoffenses/" + str( member.id ) + ".txt" ).exists():
			offenseFile = open( "data/drinkoffenses/" + str( member.id ) + ".txt", "r" )
			await ctx.send( "Total number of offenses committed by " + member.name + ": " + offenseFile.read() )
			offenseFile.close()
		else:
			await ctx.send( "Total number of offenses committed by " + member.name + ": 0" )
		return
	else:
		if Path( "data/drinkoffenses/" + str( ctx.message.author.id ) + ".txt" ).exists():
			offenseFile = open( "data/drinkoffenses/" + str( ctx.message.author.id ) + ".txt", "r" )
			await ctx.send( "Total number of offenses committed by " + ctx.message.author.name + ": " + offenseFile.read() )
			offenseFile.close()
		else:
			await ctx.send( "Total number of offenses committed by " + ctx.message.author.name + ": 0" )
		return

try:
	token = open( "settings/token.txt" )
	bot.run( token.read() )
except Exception as e:
	print( "An error occurred while loading the bot: " + str( e ) )