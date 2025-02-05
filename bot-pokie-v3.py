# This example requires the 'members' and 'message_content' privileged intents to function.

import requests
import os
import discord
from discord.ext import commands
import random
from password import llave

description = '''Aquí se muestran varios comandos de utilidad.'''

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='/', description=description, intents=intents)


@bot.event
async def on_ready():
    print(f'Iniciado sesión como {bot.user} (ID: {bot.user.id})')
    print('------')


@bot.command()
async def sumar(ctx, left: int, right: int):
    """Suma dos números separados."""
    await ctx.send(left + right)

@bot.command()
async def meme(ctx):
    """Genera memes alatorios"""
    img = random.choice ( os.listdir ( 'images' ) )
    with open(f'images/{img}', 'rb') as f:
        # ¡Vamos a almacenar el archivo de la biblioteca Discord convertido en esta variable!
        picture = discord.File(f)
    # A continuación, podemos enviar este archivo como parámetro.
    await ctx.send(file=picture)

@bot.command()
async def animales(ctx):
    """genera animales alatorios"""
    img = random.choice ( os.listdir ( 'animales' ) )
    with open(f'animales/{img}', 'rb') as f:
        # ¡Vamos a almacenar el archivo de la biblioteca Discord convertido en esta variable!
        picture = discord.File(f)
    # A continuación, podemos enviar este archivo como parámetro.
    await ctx.send(file=picture)
    

@bot.command()
async def contrazeña(ctx, Num: int = 5):
    """Te da una contrazeña a la que le puedes poner un largo."""
    await ctx.send(f'Esta es la contraseña:{llave(Num)}')

@bot.command()
async def roll(ctx, dice: str):
    """Lanza un dado en formato NdN."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send('El formato tiene que estar en NdN!')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await ctx.send(result)


@bot.command(description='Para cuando quieras ajustar cuentas de otra manera')
async def elegir(ctx, *choices: str):
    """Elige entre múltiples opciones."""
    await ctx.send(random.choice(choices))


@bot.command()
async def repetir(ctx, times: int, content='repitiendo...'):
    """Repite un mensaje varias veces."""
    for i in range(times):
        await ctx.send(content)


@bot.command()
async def joined(ctx, member: discord.Member):
    """Dice cuando un miembro se unió."""
    await ctx.send(f'{member.name} se unió {discord.utils.format_dt(member.joined_at)}')


def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('duck')
async def duck(ctx):
    '''Genera imagenes random de Patos'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)

def get_dog_image_url():    
    url = 'https://random.dog/woof.json'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('dog')
async def dog(ctx):
    '''Muestra imagenes random de Perros'''
    image_url = get_dog_image_url()
    await ctx.send(image_url)

def get_anime_image_url():    
    url = 'https://api.waifu.pics/sfw/waifu'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('anime')
async def dog(ctx):
    '''Muestra imagenes random de anime'''
    image_url = get_anime_image_url()
    await ctx.send(image_url)


def get_pokemon_image_url():
    pokemon_id = random.randint(1, 898)
    image_url = f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/{pokemon_id}.png"
    return image_url

@bot.command('pokemon')
async def pokemon(ctx):
    '''Muestra imagenes de Pokemones'''
    image_url = get_pokemon_image_url()
    await ctx.send(image_url)
    

def get_fox_image_image():    
    image = ' https://randomfox.ca/floof/'
    res = requests.get(image)
    data = res.json()
    return data['image']


@bot.command('fox')
async def fox(ctx):
    '''Muestra imagenes random de Zorros'''
    image_url = get_fox_image_image()
    await ctx.send(image_url)


@bot.group()
async def cool(ctx):
    """Dice si un usuario es genial.

    En realidad, esto sólo comprueba si se está invocando un subcomando.
    """
    if ctx.invoked_subcommand is None:
        await ctx.send(f'No, {ctx.subcommand_passed} no es cool')


bot.run('token')
