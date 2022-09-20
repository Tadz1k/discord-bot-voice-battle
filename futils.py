import os
import random


def get_sounds_list():
    sound_list = []
    for sound in os.listdir('sounds'):
        sound_list.append(sound)
    return sound_list

def get_random_sound():
    sound_list = get_sounds_list()
    random_pick = random.randint(0, len(sound_list)-1)
    return sound_list[random_pick]

