import os
import random
import mutagen
from mutagen.wave import WAVE
import utils


def get_sounds_list():
    sound_list = []
    for sound in os.listdir('sounds'):
        sound_list.append(sound)
    return sound_list

def get_random_sound():
    sound_list = get_sounds_list()
    random_pick = random.randint(0, len(sound_list)-1)
    return sound_list[random_pick]

def get_sound_duration(sound_path):
    audio = WAVE(sound_path)
    audio_info = audio.info
    audio_len = int(audio_info.length)
    hours, mins, seconds = utils.calculate_sound_duration(audio_len)
    return seconds
