from nextcord.ext import commands
from data import autorised_channel
class Invite(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.command()
  async def invite(self, ctx):
    await ctx.send("__B Community__\n**Un serveur professionnel, de pub et de chill**\n\n**Des règlements simples**\n\n**Des urls custom pour les partenaires**\n\n**Des chats actifs**\n\n**Des staff actifs**\n\n**Des salons pubs à volontée**\nhttps://discord.gg/9ME3mppG7z")

  @commands.Cog.listener("on_message")
  async def censor(self, message):
    if 'staff' not in [role.name for role in message.author.roles] and message.guild.id == 996596265389404241:
      if message.channel.id not in autorised_channel or message.channel.name.startswith("ticket"):
        if any(word in message.content.lower() for word in ['discord.gg/']) and len(message.content) > 12:
          await message.delete()
          await message.author.send(f"Tu as envoyer une invitation.\nContent : {message.content}")

def setup(bot):
  bot.add_cog(Invite(bot))
