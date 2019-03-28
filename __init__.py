import logging
import os

import discord
from discord.ext import commands

from util.config.config_handler import Config

config = Config()
bot = commands.Bot(command_prefix=config.prefix)
bot.remove_command('help')


@bot.event
async def on_ready():
    logging.info(f'Logged in as {bot.user.name}')
    logging.info(f'Version: {discord.__version__}')

    game = discord.Game(name="Tom Clancy's The Division 2")
    await bot.change_presence(activity=game)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)

    initial_extensions = ['commands.' + i.split('.')[0] for i in os.listdir('commands') if '.py' in i]
    logging.info(f'Extensions: {initial_extensions}')
    for extension in initial_extensions:
        bot.load_extension(extension)
#        try:
#            bot.load_extension(extension)
#        except Exception as e:
#            logging.info(f'Failed to load extension {extension}')


try:
    bot.run(config.token, bot=True, reconnect=True)
except KeyboardInterrupt:
    bot.logout()
