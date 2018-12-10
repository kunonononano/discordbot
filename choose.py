import discord
import random

client = discord.Client()

@client.event
async def on_ready():
    print('ログインしました')

@client.event
async def on_message(message):
    if message.content.startswith('/neko'):
        reply = 'にゃーん'
        await client.send_message(message.channel, reply)
    elif message.content.startswith('/sep'):
        cmd = message.content.split(' ')
        if len(cmd) !=2 or not cmd[1].isdecimal():
            await client.send_message(message.channel, 'コマンド/sepは\"/sep 数字\"の形で使ってください')
            return
        members = []
        for mem in message.author.voice.voice_channel.voice_members:
            members.append(mem.name if mem.nick is None else mem.nick)
        length = int(cmd[1]) if int(cmd[1]) < len(members) else len(members)
        members = random.sample(members, length)
        for member in members:
            await client.send_message(message.channel, member)
    elif message.content.startswith('/exit'):
        reply = 'ばいば～い'
        await client.send_message(message.channel, reply)
        await client.logout()
    elif message.content.startswith('/emoji'):
        await create_emoji(message)

@client.event
async def create_emoji(message):
    cmd = message.content.split(' ')
    if len(cmd) !=2:
        await client.send_message(message.channel, 'コマンド/emojiは\"/emoji 名前\"の形で使ってください')
        return
    if len(cmd[1]) < 2:
        await client.send_message(message.channel, '絵文字の名前は二文字以上にしてください')
        return
    cmd, name = cmd
    images = message.attachments
    if len(images) != 1:
        await client.send_message(message.channel, 'コマンド/emojiは写真を一枚だけ添付してください')
        return
    import urllib.request
    headers = {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:47.0) Gecko/20100101 Firefox/47.0",
    }
    request = urllib.request.Request(url=images[0]['url'], headers=headers)
    img_read = urllib.request.urlopen(request).read()
    emoji = await client.create_custom_emoji(message.server, name=name, image=img_read)

client.run('NTIxNjQ2MTcyNjA4MTM1MTk3.Du_cfQ.L0aohITRdTXLj0_QP_m3c32u_X8')