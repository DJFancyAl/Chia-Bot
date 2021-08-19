# chia_bot.py
import os
import discord
import datetime
from dotenv import load_dotenv
from discord.ext import commands
from utilities.chia import check_balance, check_farm, process_running, get_running_plots
from utilities.parser import get_config, settings
from utilities.logs import old_balance, compare_chia, update_log

# Load Discord .env Parameters
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

# Load Configuration
config = get_config()
settings = settings(config)
current_path = os.path.dirname(__file__)

# Initialize the Bot
bot = commands.Bot(command_prefix='$')
@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')


# Clear Command
@bot.command(name='clear', help='Deletes messages from this channel - use syntax "$clear 5"')
@commands.has_role("Administrator")
async def clear_channel(ctx, amount=2):
    await ctx.channel.purge(limit=amount+1)


# Check Wallet Command
@bot.command(name='wallet')
async def displayembed(ctx):
    await ctx.channel.purge(limit=1)
    user = ctx.message.author.mention

    wallet = check_balance(settings['chia_path'])
    prev_balance = old_balance(current_path, wallet)
    today = datetime.datetime.now()

    if compare_chia(wallet, prev_balance):
        message = f'''**You've got new Chia in your Wallet!**'''
    else:
        message = f'''**Your Chia Balance**'''

    embed = discord.Embed(
        title = message,
        description = f'''Hey {user} - the current balance of your Chia wallet is:

__**{wallet}**__ xch.''',
        color = discord.Color(3066993)
    )

    embed.set_footer(text='Fancy Chia Monitoring • ' + str(today.strftime('%x')) , icon_url=f'''https://file.coffee/u/QKz6jIEaZKXEj1.jpg'''),
    embed.set_image(url=''),
    embed.set_thumbnail(url=f'''https://file.coffee/u/QKz6jIEaZKXEj1.jpg''')

    await ctx.channel.send(embed=embed)
    update_log(current_path, wallet)


# Check Farm Command
@bot.command(name='farm')
async def displayembed(ctx):
    await ctx.channel.purge(limit=1)
    user = ctx.message.author.mention

    farm = check_farm(settings['chia_path'])
    farm_size = float(farm[1])
    plots = farm[0]
    today = datetime.datetime.now()

    embed = discord.Embed(
        title = '**Your Chia Farm:**',
        description = f'''Hey {user} - here's your farm's summary:

- The farm is {farm_size:.2f} TiB in size.
- It's made of {plots} plots.''',
        color = discord.Color(3066993)
    )

    embed.set_footer(text='Fancy Chia Monitoring • ' + str(today.strftime('%x')) , icon_url=f'''https://file.coffee/u/QKz6jIEaZKXEj1.jpg'''),
    embed.set_image(url=''),
    embed.set_thumbnail(url=f'''https://file.coffee/u/QKz6jIEaZKXEj1.jpg''')

    await ctx.channel.send(embed=embed)


# Check Plotter Command
@bot.command(name='plotter')
async def displayembed(ctx):
    await ctx.channel.purge(limit=1)
    user = ctx.message.author.mention

    if not settings['plotting']:
        await ctx.channel.send('Sorry {}! Set "Plotting" to "True" in the config file to use this feature.'.format(user))
        return

    check_plotter = process_running(settings['plot_process'])
    today = datetime.datetime.now()

    if check_plotter:
        embed = discord.Embed(
            title = '**Your Chia Plotter:**',
            description = f'''Hey {user} - your plotter is running!

Currently {get_running_plots()} plots are running.''',
            color = discord.Color(3066993)
        )

        embed.set_footer(text='Fancy Chia Monitoring • ' + str(today.strftime('%x')) , icon_url=f'''https://file.coffee/u/QKz6jIEaZKXEj1.jpg'''),
        embed.set_image(url=''),
        embed.set_thumbnail(url=f'''https://file.coffee/u/QKz6jIEaZKXEj1.jpg''')
    else:
        embed = discord.Embed(
            title = '**Something is Wrong!**',
            description = f'''Hey {user} - your plotter is not running!

Verify that the config setting is correct and that your plotting app is running.''',
            color = discord.Color(3066993)
        )

        embed.set_footer(text='Fancy Chia Monitoring • ' + str(today.strftime('%x')) , icon_url=f'''https://file.coffee/u/J9zehdqvjsVERG.jpg'''),
        embed.set_image(url=''),
        embed.set_thumbnail(url=f'''https://file.coffee/u/J9zehdqvjsVERG.jpg''')

    await ctx.channel.send(embed=embed)


# Check Price Command
@bot.command(name='price')
async def displayembed(ctx, coin=""):
    await ctx.channel.purge(limit=1)
    user = ctx.message.author.mention

    if coin == "":
        await ctx.channel.send('That didn\'t work {}! You must include a crypto name. For example: \"$price Chia\" or \"$price BTC\"'.format(user))
        return

    data = get_price(coin)

    if not data:
        await ctx.channel.send('That didn\'t work {}! Use a different command or try again later.'.format(user))
    else:
        today = datetime.datetime.now()

        embed = discord.Embed(
            title = f'''**{data[0]} Price**''',
            description = f'''Hey {user} - the current price of {data[0].capitalize()} ({data[1].upper()}) is **{data[2]}**

    or Equal to {data[3]} (Bitcoin)''',
            color = discord.Color(3066993)
        )

        embed.set_footer(text='Fancy Chia Monitoring • ' + str(today.strftime('%x')) , icon_url=f'''https://file.coffee/u/QKz6jIEaZKXEj1.jpg'''),
        embed.set_image(url=''),
        embed.set_thumbnail(url=data[4])

        await ctx.channel.send(embed=embed)

bot.run(TOKEN)
