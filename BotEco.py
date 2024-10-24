import discord
from discord.ext import commands
import random

intents = discord.Intents.default()
intents.message_content = True

boteco = commands.Bot(command_prefix='@', intents=intents)

@boteco.event
async def on_ready():
    print(f'We have logged in as {boteco.user}')

manuideas=["Crear una maceta con una botella de plástico.", "Crear un comedor para pájaros con una cja de leche.", ""]
reciclables=["botella de plástico","papel","cartón"]
basura=["pañales","jeringas","licopor","hisopos"]

@boteco.command
async def manualidades (ctx):
    print(ctx.messenge.content)
    await ctx.send(random.choice(manuideas))
    

@boteco.command
async def clasfy (ctx,*,objeto:str):
    if objeto in reciclables:
        await ctx.send(f"El objeto: {objeto} es reciclable")
    elif objeto in basura:
        await ctx.send(f"El objeto {objeto} NO es reciclable")
    else:
        await ctx.send ("Desconozco si el objeto es reciclable o no, preguntame esto en el futuro")

boteco.run("El token va aqui")
