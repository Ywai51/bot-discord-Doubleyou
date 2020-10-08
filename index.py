import os
import random
import discord
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
GUILD = 'Sayonara Ｇouki'


bot = commands.Bot(command_prefix='!')
#----------------------------------------------

@bot.command(name='say')
@commands.has_permissions(manage_roles=True)
async def giverole(ctx, user: discord.Member=None, rolename:discord.Role=None):
    if rolename == '@SleepyMan':
        brooklyn_99_quotes = [
            'Dont be too much u useless D...',
            'Just die! MDfcker!',
            (
                'LOL, try to controlled me??'
                '- XD.'
            ),
        ]
    else :
        brooklyn_99_quotes = [
            'You are the best person in the werldd!!',
            'I am doubleyou , nice to meet you!',
            (
                'You are pretty funny'
                '- XD.'
            ),
        ]
    response = random.choice(brooklyn_99_quotes)
    await ctx.send(response)

@bot.command(name='roll_dice', help='Simulates rolling dice.')
@commands.has_role('@Killer')
async def roll(ctx, number_of_dice: int, number_of_sides: int):
    dice = [
        str(random.choice(range(1, number_of_sides + 1)))
        for _ in range(number_of_dice)
    ]
    await ctx.send('Kill or Luck!!.')
    await ctx.send(', '.join(dice))

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.CheckFailure):
        await ctx.send('You not a Killer, a poor human TT')


 

bot.run(TOKEN)
