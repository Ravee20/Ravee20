import discord
from discord.ext import commands
import random
import os
import yfinance as yf

intents = discord.Intents.all()
intents.members = True
intents.message_content = True

client = commands.Bot(intents= intents , command_prefix="!")

@client.event
async def on_ready(): # Bot Çalıştırıldığında Çalışır
    print("-------------------------------")
    print("Bot10 Sunucuya Entegre Edildi!")
    print("-------------------------------")

@client.command()
async def who(ctx): # !who ->
    await ctx.send("Ben Bu Sunucunun Botuyum.")

@client.event
async def on_member_join(member: discord.Member): # Sunucuya Birisi Katıldığında
    channel = client.get_channel(1121769999292436492)
    await channel.send(f'Oooo Kimler Gelmiş , Güverteye Hoşgeldin {member.mention}')
    await channel.send("-----------------------------------------------------------")

@client.event
async def on_member_remove(member: discord.Member): # Sunucudan Birisi Ayrıldığında
    channel = client.get_channel(1121769999292436492)
    await channel.send(f'{member.mention} Güverteden Ayrıldı , Görüşürüz.')
    await channel.send("-----------------------------------------------------------")

@client.command()
async def meme_at(ctx):
    secilen_dosya = random.choice(os.listdir("memes"))
    f = open(f'memes/{secilen_dosya}' , "rb")
    memes = discord.File(f)
    await ctx.send(file=memes)

@client.command()
async def hisse(ctx, symbol):
    stock_data = yf.Ticker(f'{symbol}.IS')
    stock_info = stock_data.info
    stock_name = stock_info['shortName']
    stock_price = stock_info['currentPrice']
    await ctx.send(f'Hisse -> {stock_name}')
    await ctx.send(f'Değeri -> {stock_price}')

@client.event
async def on_typing(channel, user, when):
    print(f"{user.name} Şu Anda {channel.name} Kanalında Yazıyor!")

client.run("TOKEN")