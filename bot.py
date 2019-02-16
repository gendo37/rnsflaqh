import discord
import asyncio
from discord.ext.commands import Bot
import os
from discord.voice_client import VoiceClient
from discord.ext import commands
import time
import random
from discord import opus
 
OPUS_LIBS = ['libopus-0.x86.dll', 'libopus-0.x64.dll', 'libopus-0.dll', 'libopus.so.0', 'libopus.0.dylib']
 
def load_opus_lib(opus_libs=OPUS_LIBS):
    if opus.is_loaded():
        return True
 
    for opus_lib in opus_libs:
            try:
                opus.load_opus(opus_lib)
                return
            except OSError:
                pass
 
    raise RuntimeError('Could not load an opus lib. Tried %s' % (', '.join(opus_libs)))
 
load_opus_lib()
bot = commands.Bot("")
for ext in  ["music"]:
    bot.load_extension(ext)



@bot.event
async def on_ready():
    print("준비완료!")
    while True:
        await bot.change_presence(game=discord.Game(name='트위치 군림보채널에서 방송중'))
        await asyncio.sleep(10)
        await bot.change_presence(game=discord.Game(name='비틀즈 냠냠'))
        await asyncio.sleep(10)
        await bot.change_presence(game=discord.Game(name='컴마왕!!!!!'))
        await asyncio.sleep(10)
        await bot.change_presence(game=discord.Game(name='손 씻는중'))
        await asyncio.sleep(10)
         

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
	




bot.run(os.environ['BOT_TOKEN'])
