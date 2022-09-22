import discord
from discord.ext import commands




if __name__ == '__main__':
    intents = discord.Intents().all()
    client = commands.Bot(command_prefix="$", intents=intents)
    client.remove_command('help')

    @client.event
    async def on_ready():
        print('logged as {}'.format(client.user))

    #Załadowanie wtyczki z komendami
    client.load_extension('bot_commands')


    client.run('MTAyMTc2MDExMDUzNzc1NjY5NA.G-3_Wz.b00t1zT-aMdP6Ux21daQVFTzy-7Gn9uJO03Hqw')