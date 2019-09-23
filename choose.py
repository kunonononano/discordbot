import discord
import random

client = discord.Client()

@client.event
async def on_ready():
    print('ログインしました')

@client.event
async def on_message(message):
    if message.content.startswith('/sep'):
        await do_separate(message)
    elif message.content.startswith('/emoji'):
        await create_emoji(message)
    elif message.content.startswith('/how2'):
        await client.send_message(message.channel,
                                  '\"/sep 数字\"と打つと打った人のいるvoice channelの中でランダムに指定した数字の人数が選ばれます。\n観戦者を分けるときにでもどうぞ\n'
                                  + '画像を一枚添付して\"emoji 名前\"と打つと選んだ画像が指定した名前で絵文字になります。\n'
                                  + '絵文字は合計50しか保存できないので管理者の方は注意してね')
    elif message.content.startswith('/quiz'):
        await create_quiz(message)
    elif message.content.startswith('/ans'):
        await judge_answer(message)
    elif message.content.startswith('/add'):
        await add_abbreviation(message)
    elif message.content.startswith('/exit'):
        reply = 'ばいば～い'
        await client.send_message(message.channel, reply)
        await client.send_message(message.channel, reply)
        await client.logout()
    elif message.content.startswith('/join'):
        await client.login('NTIxNjQ2MTcyNjA4MTM1MTk3.Du_cfQ.L0aohITRdTXLj0_QP_m3c32u_X8')

@client.event
async def do_separate(message):
    cmd = message.content.split(' ')
    if len(cmd) != 2 or not cmd[1].isdecimal():
        await client.send_message(message.channel, 'コマンド/sepは\"/sep 数字\"の形で使ってください。')
        return
    members = []
    for mem in message.author.voice.voice_channel.voice_members:
        members.append(mem.name if mem.nick is None else mem.nick)
    length = int(cmd[1]) if int(cmd[1]) < len(members) else len(members)
    members = random.sample(members, length)
    for member in members:
        await client.send_message(message.channel, member)

@client.event
async def create_emoji(message):
    cmd = message.content.split(' ')
    if len(cmd) != 2:
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

@client.event
async def create_quiz(message):
    # TODO: 機能が未実装なためhow2を表示
    await client.send_message(message.channel, 'コマンド/quizは\"/quiz\"または\"/quiz 武器種(スペース区切りで複数可能)\"の形で使ってください')
    return
    cmd = message.content.split(' ')
    cmd, *weapon_types = cmd
    
    

@client.event
async def judge_answer(message):
    # TODO: 機能が未実装なためhow2を表示
    await client.send_message(message.channel, 'コマンド/ansは\"/ans (サブの名前) (スペシャルの名前)\"の形で答えてください')
    return
    cmd = message.content.split(' ')
    # TODO: サブウェポン、スペシャルのリストを作ったらスペシャル、サブの順番で答えてるのもここに来るようにする
    if len(cmd) != 3:
        await client.send_message(message.channel, 'コマンド/ansは\"/ans (サブの名前) (スペシャルの名前)\"の形で答えてください')
        return
    cmd, sub, special = cmd

@client.event
async def add_abbreviation(message):
    # TODO: 機能が未実装なためhow2を表示
    await client.send_message(message.channel, 'コマンド/addは\"/add (正式名称) (略称)\"の形で追加してください\nサブウェポン、スペシャルウェポンの略称を登録することができます')
    return
    cmd = message.content.split(' ')
    # TODO: サブウェポン、スペシャルのリストを作ったらスペシャル、サブの順番で答えてるのもここに来るようにする
    if len(cmd) != 3:
        await client.send_message(message.channel, 'コマンド/addは\"/add (正式名称) (略称)\"の形で追加してください\nサブウェポン、スペシャルウェポンの略称を登録することができます')
        return
    cmd, formal, abbreviation = cmd

client.run('NTIxNjQ2MTcyNjA4MTM1MTk3.XYjrVw.3nqYn1QbBPtGFgjIeWogUrK-r_0')
