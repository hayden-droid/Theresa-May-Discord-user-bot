#bad bot by Da532


#---CONFIG---

token = "TOKEN_HERE" # To find this, press CTRL + SHIFT + i in the Discord client revealing the inspect element prompt. Click the arrows, head over to Application, local storage and there you can find your user token :)

#--- BOT ---

import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import random

bot = commands.Bot(command_prefix="crow", self_bot=True)
bot.remove_command("help")

@bot.event
async def on_ready():
    print ("Ready to divide your server!") 

async def detection(message):
    if not message.channel.is_private:
        try:
            workin = message.content.lower()
            still_workin = workin.split(" ")
            if bot.user.id == message.author.id:
                pass
            elif "nhs" in still_workin:
                await bot.send_message(message.channel, "The NHS should be made private. This server is in shambles..")
            elif "wrong" in still_workin:
                await bot.send_message(message.channel, "The only thing I've done wrong is run through barley fields.")
            elif "labour" in still_workin:
                await bot.send_message(message.channel, "Awful, awful people..")
            elif "eu" in still_workin:
                await bot.send_message(message.channel, "B A D")
            elif "european" and "union" in still_workin:
                await bot.send_message(message.channel, "B A D")
            elif "ajit" and "pai" in still_workin:
                await bot.send_message(message.channel, "My husbando ~<3")
            elif "left" and "wing" in still_workin:
                await bot.send_message(message.channel, "Fucking communists..")
            elif "theresa" in still_workin:
                await bot.send_message(message.channel, ":wave:")
            elif "may" in still_workin:
                await bot.send_message(message.channel, ":wave:")
            elif "<@207883755392729088>" in still_workin:
                await bot.send_message(message.channel, ":wave:")
        except:
            pass
            

bot.add_listener(detection, 'on_message')

bot.run(token, bot=False)
