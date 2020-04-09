import json
import os
from discord.ext.commands import Bot

with open('config.json', 'r') as f:
    config = json.load(f)

bot = Bot(command_prefix=config['prefix'], description=config['description'])


async def load_modules():
    for file in os.listdir('cogs'):
        if file.endswith('.py'):
            name = file[:-3]
            bot.load_extension(f'cogs.{name}')


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} (ID: {bot.user.id}')
    print('-----')

    await load_modules()

bot.run(config['token'])
