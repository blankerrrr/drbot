

from os import strerror
from typing import Text
import discord, asyncio
import random
import datetime
import openpyxl
import requests
from datetime import date
from random import sample
i = 1,2,3,4,5,6
e = 1,2,3

client = discord.Client()
@client.event
async def on_ready(): 
    print("ㅇㅇㅇ")
    await client.change_presence(status=discord.Status.online, activity=discord.Game("ㄹ 도움"))
@client.event
async def on_message(message):
    if message.content == "ㄹ ㅂㅇ": 
        await message.channel.send ("안녕히계세요")
    elif message.content == "ㄹ 도움":
        embed = discord.Embed(title='도움말',description='접두사:ㄹ',color=0x0000ff)
        embed.set_footer(text="bot made by.공백#1976", icon_url="https://cdn.discordapp.com/attachments/888305993891577879/888995261957943296/download20210900124934.png")
        embed.add_field(name = '```주요 명령어```', value = '||ㅎㅇ||,||ㅂㅇ||,||뭐해||,||핑||,||#1976||,||맨션해봐||,||ㅋㅋㄹㅃㅃ||,||디르야 일해||')
        embed.add_field(name = '```놀이기능```', value = '||주사위(100,1000)||')
        embed.add_field(name = '```팀 파이 공식 사이트```',value = '[사이트바로가기](https://teamfielee.quv.kr/)')
        embed.set_thumbnail(url = 'https://cdn.discordapp.com/attachments/888305993891577879/888995261957943296/download20210900124934.png')
        await message.channel.send(embed = embed)
    elif message.content == "ㄹ ㅎㅇ": 
        await message.channel.send ("안녕하세요")
    elif message.content == "ㄹ 뭐해":
        await message.channel.send (format(message.author.mention)+"님과 대화하고있어요")
    elif message.content == "ㄹ 핑":
        await message.channel.send(embed = discord.Embed(title ='퐁!', description = f'현제 핑은 {round(client.latency * 1000)}ms 입니다'))
    elif message.content == "ㄹ #1976":
        await message.channel.send ("공백님의 테그에요!")
    elif message.content == "ㄹ 맨션해봐":
        await message.channel.send (format(message.author.mention))
    elif message.content == "ㄹ ㅋㅋㄹㅃㅃ":
        await message.channel.send (format(message.author.mention)+"너도 잼민이구나...")
    elif message.author.bot:
            return None
    elif message.content == "ㄹ 주사위100":
        await message.channel.send (embed = discord.Embed(title='결과',description=random.sample(range(1,100),1),color=0x0000ff))
    elif message.content == "ㄹ 주사위":
        i = 1,2,3,4,5,6
        await message.channel.send (embed = discord.Embed(title='결과',description=random.sample(i,1),color=0x0000ff))
    elif message.content == "ㄹ 주사위1000":
        await message.channel.send (embed = discord.Embed(title='결과',description=random.sample(range(1,1000),1),color=0x0000ff))
    elif message.content == "디르야 일해":
        await message.channel.send ('하..인생 댕같다.....')

    elif message.content.startswith(""):
            file = openpyxl.load_workbook("레벨.xlsx")
            exp = [10,20,30,40,50]
            sheet = file.active
            i=1
            while True:
                if sheet["A" + str(i)].value == str(message.author.id):
                    sheet["B" + str(i)].value =sheet["B" + str(i)].value +5
                    if sheet["B" + str(i)].value >= exp[sheet["C"+str(i)].value]:
                        sheet["C"+str(i)].value = sheet["C"+str(i)].value + 1
                        await message.channel.send("레벨이 올랐습니다.\n현재레벨:"+str(sheet["C"+str(i)].value)+ "\n 경험치:"+str(sheet["B" + str(i)].value))
                        file.save("레벨.xlsx")
                        break
                
                if sheet["A" + str(i)].value == None:
                    sheet["A" + str(i)].value = str(message.author.id)
                    sheet["B" + str(i)].value = 0
                    sheet["C" + str(i)].value = 1
                    file.save("레벨.xlsx")
                    break
    
    
    
    # 파이썬의 기본 내장 함수가 아닌 다른 함수 혹은 다른 기능이 필요할 때 사용함


client.run('ODg4Nzg4NjE1OTIzMTA1ODcy.YUXy5g.Qex6TFfyZ0Mm-f78RQ1nUM01leQ')
