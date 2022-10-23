import requests
from threading import *



def GetPokemonName(pokemon):
    apiLink = requests.get(f"https://pokeapi.glitch.me/v1/pokemon/{pokemon}")
    data = apiLink.json()[0]['name']
    return data

def GetPokemonType(pokemon):
    apiLink = requests.get(f"https://pokeapi.glitch.me/v1/pokemon/{pokemon}")
    data = apiLink.json()[0]['types'][0]
    return data

def GetPokemonID(pokemon):
    apiLink = requests.get(f"https://pokeapi.glitch.me/v1/pokemon/{pokemon}")
    data = apiLink.json()[0]['number']
    return data

def GetPokemonSprite(pokemon):
    apiLink = requests.get(f"https://pokeapi.glitch.me/v1/pokemon/{pokemon}")
    data = apiLink.json()[0]['sprite']
    return data


