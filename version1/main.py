import discord
import os
from dotenv import load_dotenv
from neuralintents import GenericAssistant
import random

chatbot = GenericAssistant('intents.json')
chatbot.train_model()
chatbot.save_model()

intents = discord.Intents.default()
bot = discord.Client(intents=intents)

load_dotenv()
TOKEN = os.getenv('TOKEN')

@bot.event
async def on_ready():
    print(bot.user.name + ' is running...')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if bot.user.mention in message.content:
        response = chatbot.request(message.content[0:])
        await message.reply(response)
    else:
        pass
        # await message.reply("If you want to chat with me, mention <@949272449000824902> in your message!")


@bot.event
async def on_reaction_add(reaction, user):
    if reaction.emoji == "🖕":
        await reaction.message.channel.send(f"{user.mention} that is not cool man!")

@bot.event
async def on_reaction_add(reaction, user):
    if reaction.emoji == "🖕":
        response = [f"{user.mention} that is not cool man!", f"Hey, that's rude {user.mention}! :angry:", f"{user.mention} remove that reaction! :rage:"]
        await reaction.message.channel.send(random.choice(response))

@bot.event
async def on_connect():
    chan = os.getenv('CHANNEL_ID')
    channel = bot.get_channel(int(chan))
    print(channel)
    await channel.send(content='Hey guys, I am online! :wave:')

bot.run(TOKEN)
