import discord
from discord.ext import commands
from os import getenv
import aiohttp
import warnings

warnings.filterwarnings("ignore", category=DeprecationWarning)

class Vector(commands.Bot):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
            
        self.session = aiohttp.ClientSession()

    async def on_ready(self):
        print('Bot is ready.')


bot = Vector(command_prefix='v!', case_insensitive=True)

if __name__ == '__main__':
    bot.load_extension('jishaku')
    bot.run(getenv('token'))