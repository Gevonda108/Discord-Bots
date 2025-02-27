import discord
import random
import asyncio
from discord.ext import commands
from bot_logic import gen_pass



intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def generate_password(ctx):
    await ctx.send("This Is your random password:")
    await ctx.send(gen_pass(8))

@bot.command()
async def pangkatkan(ctx):
    await ctx.send("masukkan angka yang ingin di pangkatkan")
    angka = await bot.wait_for('message', check=lambda m: m.author == ctx.author and m.channel == ctx.channel)
    angka = int(angka.content)
    await ctx.send("berikut pangkat dua dari angka yang anda masukkan")
    await ctx.send(angka**2)

@bot.command()
async def perintah(ctx):
    await ctx.send("Output the following command:"),
    await ctx.send("$hello"),
    await ctx.send("$heh"),
    await ctx.send("$generate_password"),
    await ctx.send("$guess"),
    await ctx.send("$pangkatkan")


@bot.command()
async def on_message(self, message):
    if message.content.startswith('$guess'):
        await message.channel.send('Guess a number between 1 and 10.')

        def is_correct(m):
            return m.author == message.author and m.content.isdigit()

        answer = random.randint(1, 10)

        try:
            guess = await self.wait_for('message', check=is_correct, timeout=5.0)
        except asyncio.TimeoutError:
            return await message.channel.send(f'Sorry, you took too long it was {answer}.')

        if int(guess.content) == answer:
            await message.channel.send('You are right!')
        else:
            await message.channel.send(f'Oops. It is actually {answer}.')


intents = discord.Intents.default()
intents.message_content = True
bot.run("YOUR TOKEN HERE")
