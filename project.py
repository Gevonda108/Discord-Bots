import discord
import random,os
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} is cooking!')

organik = ['daun', 'kulit pisang', 'makanan sisa',
           'sayur busuk', 'nasi basi', 'tulang ikan', 
           'ampas kopi', 'kulit telur', 'batang pisang', 
           'kotoran hewan', 'ranting kayu', 'serbuk kayu', 
           'rumput', 'teh celup bekas', 'tisu bekas', 
           'jerami', 'sabut kelapa', 'biji buah', 
           'cangkang udang', 'cangkang kepiting'] 

anorganik =  [
    'plastik', 'botol plastik', 'kaca', 'kaleng', 'besi', 'aluminium', 
    'styrofoam', 'kardus bekas', 'baterai', 'kertas aluminium', 
    'sedotan', 'bungkus makanan', 'tutup botol', 'helm rusak', 
    'ban bekas', 'elektronik bekas', 'lampu neon', 'cd bekas', 
    'dvd bekas', 'kabel', 'paku', 'baut', 'pipa pvc'
]

b3 = [
    'oli bekas', 'aki bekas', 'obat kadaluarsa', 'cat tembok', 
    'deterjen', 'pestisida'
]


@bot.command()
async def sampah(ctx, *, item:str = None):
    if item is None:
        await ctx.send("⚠️masukkan command sampah <jenis sampah>")
        await ctx.send("Contoh: $sampah daun")
    
    if item.lower() in organik:
        await ctx.send(f"{item} adalah sampah organik")
        await ctx.send("Sampah ini termasuk sampah organik")
        await ctx.send("Cara untuk mengolah sampah organik adalah dengan cara mengomposkan sampah organik")
    elif item.lower() in anorganik:
        await ctx.send(f"{item} adalah sampah anorganik")
        await ctx.send("Sampah ini termasuk sampah organik")
        await ctx.send("Cara untuk mengolah sampah anorganik adalah dengan cara mendaur ulang sampah anorganik")
    elif item.lower() in b3:
        await ctx.send(f"{item} adalah sampah B3")
        await ctx.send("Sampah ini termasuk sampah organik")
        await ctx.send("Cara untuk mengolah sampah B3 adalah dengan cara mendaur ulang sampah B3")

    else:
        await ctx.send(f"{item} bukanlah sampah organik atau anorganik atau B3")


bot.run("TOKEN")