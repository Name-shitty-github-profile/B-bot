from nextcord.ext import commands
from nextcord import Embed
class Welcome(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.Cog.listener("on_member_join")
  async def welcome(self, member):
    if member.guild.id == 996596265389404241: 
      await self.bot.get_channel(996827923472466041).send(embed=Embed(title=f"Bienvenue {member.name}!", description="J'espere que tu va t'amuser ici !\nJe t'invite à lire les règlements", color=0x3498db).set_image(url='https://i.pinimg.com/originals/0f/f3/ee/0ff3ee57827c9c68f1a4d4ab72a81572.gif'))
      member.add_roles(member.guild.get_role(996835567025279047))

def setup(bot):
  bot.add_cog(Welcome(bot))
