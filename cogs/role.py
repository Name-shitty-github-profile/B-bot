import nextcord
from data import value_id
class pingbtn(nextcord.ui.Select):
  def __init__(self):
    options: list = [
      nextcord.SelectOption(label='Partenariat', description="Vous allez vous faire ping lors des partenariats"),
      nextcord.SelectOption(label="Chat reviver", description="Vous allez vous faire ping pour faire revire le chat"),
      nextcord.SelectOption(label="Annonce", description="Vous allez vous faire ping lors des annonces")
    ]
    super().__init__(placeholder="Veuillez selectionner vos pings.", min_values=1, max_values=3, options=options)

  async def callback(self, interaction: nextcord.Interaction):
    msg: str = 'Voici vos selections : '
    for i in self.values:
      await interaction.user.add_roles(interaction.guild.get_role(value_id[i]))
      msg += i + ' '
    await interaction.response.send_message(content=msg, ephemeral=True)

class Viewrapper(nextcord.ui.View):
  def __init__(self):
    super().__init__(timeout=None)
    self.add_item(pingbtn())

from nextcord.ext import commands
class Roles(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.Cog.listener("on_ready")
  async def role(self):
    channel = self.bot.get_channel(996884381148917921)
    await channel.purge(limit=1)
    view = Viewrapper()
    await channel.send('Veuillez selectionnez vos roles !', view=view)
    await view.wait()

def setup(bot):
  bot.add_cog(Roles(bot))
