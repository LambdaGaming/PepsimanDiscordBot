import discord

Drinks = [
	"coke",
	"sprite",
	"coca-cola",
	"coca cola",
	"lemonade",
	"fanta",
	"beer",
	"surge",
	"vault",
	"water", 
	"tropicana",
	"bleach",
	"vodka",
	"dr pepper",
	"dr. pepper",
	"mtn dew",
	"mountain dew"
]

GoodDrinks = [
	"pep",
	"pepsi",
	"bepis"
]

class MyClient( discord.Client ):
	async def on_ready( self ):
		print( 'Logged in as {0}!'.format( self.user ) )

	async def on_message( self, message ):
		usertag = str( message.author.id )
		split = message.content.split( " " )
		offenseFile = open( "data/drinkoffenses/" + usertag + ".json", "w+" )
		if message.author.bot: return
		if split[0] == "!pepsiman":
			try:
				if split[1] == " ":
					await message.channel.send( "Yes? What do you want?" )
				elif split[1] == "givepepsi":
					await message.channel.send( 'https://media.giphy.com/media/s0s2S5MhxBD4A/giphy.gif' )
				elif split[1] == "showlatestoffense":
					await message.channel.send( "Last recorded message containing a drink offense: " + "`" + offenseFile.read() + "`" )
				return
			except IndexError:
				await message.channel.send( "Yes? What do you want?" )
				return
		for item in Drinks:
			if item in message.content.lower():
				await message.channel.send( "YOU FOOL! HOW DARE YOU DRINK " + item.upper() + " INSTEAD OF PEPSI!" )
				offenseFile.write( message.content )
				break
		for item in GoodDrinks:
			if item in message.content.lower():
				await message.channel.send( "https://i.pinimg.com/originals/30/da/4e/30da4e74b1d08a8b65c1dcbbae44b546.jpg" )
		offenseFile.close()
		cooldown = False

try:
	token = open( "token.txt" )
	client = MyClient()
	client.run( token.read() )
except:
	print( "Failed to open token file. File doesn't exist." )