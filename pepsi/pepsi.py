import re
from discord.ext import commands

bot = commands.Bot( command_prefix = "!" )

Drinks = [ "coke", "sprite", "coca-cola", "coca cola", "lemonade", "fanta", "beer", "surge", "vault", "water",  "tropicana", "bleach", "vodka", "dr pepper", "dr. pepper", "mtn dew", "mountain dew" ]
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
	for item in Drinks:
		if findWord( item )( message.content ) is not None:
			await message.channel.send( "YOU FOOL! HOW DARE YOU DRINK " + item.upper() + " INSTEAD OF PEPSI!" )
			offenseFile = open( "data/drinkoffenses/" + str( message.author.id ) + ".txt", "w+" )
			offenseFile.write( message.content )
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
async def latestoffense( ctx ):
	offenseFile = open( "data/drinkoffenses/" + str( ctx.message.author.id ) + ".txt", "r" )
	await ctx.send( "Last recorded message containing a drink offense: " + "`" + offenseFile.read() + "`" )
	offenseFile.close()

try:
	token = open( "settings/token.txt" )
	bot.run( token.read() )
except Exception as e:
	print( "An error occurred while loading the bot: " + str( e ) )