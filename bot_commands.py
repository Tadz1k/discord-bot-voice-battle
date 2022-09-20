import asyncio
from pydoc import cli
import discord
from discord.ext import commands
from discord.ext.audiorec import NativeVoiceClient
from discord import FFmpegAudio


#own imports
import futils
import settings



@commands.command()
async def help(ctx):
    embed=discord.Embed(title="help", url="https://google.pl/", description="Bot do gier głosowych. Komendy:\n$siema - sprawdzenie, czy bot żyje\n$join - dołączenie do kanału\n$disconnect - rozłączenie z kanałem\n$round_start - rozpoczęcie rundy singleplayer", color=discord.Color.blue())
    await ctx.send(embed=embed)

@commands.command()
async def siema(ctx):
    await ctx.send("yo")

@commands.command()
async def join(ctx):
    channel: discord.VoiceChannel = ctx.author.voice.channel
    if ctx.voice_client is not None:
        return await ctx.voice_client.move_to(channel)
    await channel.connect(cls=NativeVoiceClient)

@commands.command()
async def disconnect(ctx):
    await ctx.voice_client.disconnect()

@commands.command()
async def round_start(ctx):
    voice = await ctx.author.voice.channel.connect()
    await ctx.send(ctx.message.author)
    play_round_sound_sequence(voice, 0)



#other functions
def play_round_sound_sequence(voice, index):
    if(index < len(settings.voice_sequence)):
        voice.play(discord.FFmpegPCMAudio(executable=settings.ffmpeg_path, source=settings.voice_sequence[index]),after = lambda x=None: play_round_sound_sequence(voice,index+1))
    else:
        return
    


def setup(client):
    client.add_command(siema)
    client.add_command(help)
    client.add_command(join)
    client.add_command(disconnect)
    client.add_command(round_start)


