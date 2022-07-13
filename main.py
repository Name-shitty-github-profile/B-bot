from nextcord.ext import commands
from nextcord import Intents
bot = commands.Bot(command_prefix=["?"], help_command=None, intents=Intents.all())
from os import listdir, environ, system
for fn in listdir('cogs'): bot.load_extension(f'cogs.{fn[: -3]}') if i.endswith('.py') else print('not a python file')
@bot.event
async def on_message(message):
  if message.guild.id == 996596265389404241:
    await bot.process_commands(message)
bot.run(environ['token'])
