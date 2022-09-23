import asyncio
from distutils.log import info
import imp
from pydoc import cli
import discord
from discord.ext import commands
from discord.ext.audiorec import NativeVoiceClient
from discord import FFmpegAudio
import time
import random
import threading

#own imports
import futils
import settings

result_available = threading.Event()

@commands.command()
async def help(ctx):
    embed=discord.Embed(title="help", url="https://google.pl/", description="Bot do gier głosowych. Komendy:\n$siema - sprawdzenie, czy bot żyje\n$join - dołączenie do kanału\n$disconnect - rozłączenie z kanałem\n$round_start - rozpoczęcie rundy singleplayer", color=discord.Color.blue())
    await ctx.send(embed=embed)

@commands.command()
async def siema(ctx):
    await ctx.send("yo")

@commands.command()
async def disconnect(ctx):
    await ctx.voice_client.disconnect()

@commands.command()
async def round_start(ctx):
    # Play sound sequence and disconnect
    voice = await ctx.author.voice.channel.connect()
    await ctx.send(ctx.message.author)
    sound_duration_seconds = futils.get_sound_duration(settings.voice_sequence[1])
    thread = threading.Thread(target=play_round_sound_sequence(voice, 0, ctx))
    thread.start()
    result_available.wait()
    await ctx.voice_client.disconnect()
    #Start recording - reconnect for change encoder



#other functions
def play_round_sound_sequence(voice, index, ctx):
    '''
    LEN = 3
    index = 0 -- info
    index = 1 -- sound
    index = 2 -- peep
    index = 3 -- disconnect
    '''
    if(index < len(settings.voice_sequence)):
        voice.play(discord.FFmpegPCMAudio(executable=settings.ffmpeg_path, source=settings.voice_sequence[index]),after = lambda _: play_round_sound_sequence(voice,index+1, ctx))
    else:
        result_available.set()
        return 1
    


def setup(client):
    client.add_command(siema)
    client.add_command(help)
    client.add_command(disconnect)
    client.add_command(round_start)


