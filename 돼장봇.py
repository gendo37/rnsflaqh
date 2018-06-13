
import random
import discord

from discord.ext import commands
from discord.ext.commands import Bot
from discord.voice_client import VoiceClient


startup_extensions = ["Music"]
BOT_PREFIX = ("")
TOKEN = "NDU1NzIwOTUwNTIxMDA0MDQy.DgAGvA.5s-bfmdnsIRA77JvevDv7_lSfNs"
 

bot = commands.Bot("")

@bot.event
async def on_ready():
	print('시작!')

class Main_Commands():
        def __init__(self, bot):
         self.bot = bot
        def setup(bot):
            bot.add_cog(Music(bot))
            print("Music is loaded")

@bot.command()
async def 돼장님():
    possible_responses = [
        '네',
        '왜 그러시죠',

    ]
    await bot.say(random.choice(possible_responses))

@bot.command()
async def 군하():
    possible_responses = [
        '아이고 감사합니다',
        '안녕하세요',

    ]
    await bot.say(random.choice(possible_responses))

@bot.command()
async def 후원():
    possible_responses = [
        '아이고 방송 봐주시는 것만 해도 감사한데',
        '감사합니다 꼬맙습니다',
        '통 큰 후원감사합니다',


    ]
    await bot.say(random.choice(possible_responses))

@bot.command()
async def 김블루():
    possible_responses = [
        '내가  간다 김블루!',
        '김블루님 언급은 김블루님 방송에서 해주세요',
        '이거 제 방송입니다 ㅠㅠ',
        '타 스트리머 언급은 자제 부탁드려요 찡긋',

    ]
    await bot.say(random.choice(possible_responses))
	
@bot.event
async def on_message(message):
    elif '시발' in message.content.lower():
        await bot.send_message(message.channel, f'욕은 자제해주세요, {message.author.name}')








bot.run(TOKEN)
