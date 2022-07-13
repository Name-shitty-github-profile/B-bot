from nextcord.ext import commands
from data import autorised_channel
class Invite(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.Cog.listener("on_message")
  async def invite(self, message):
    if 'staff' not in [role.name for role in message.author.roles] and message.guild.id == 996596265389404241:
      if message.channel.id not in autorised_channel or message.channel.name.startswith("ticket"):
        if any(word in message.content.lower() for word in ['discord.gg/']) and len(message.content) > 12:
          await message.delete()
          await message.author.send(f"Tu as envoyer une invitation.\nContent : {message.content}")

def setup(bot):
  bot.add_cog(Invite(bot))
