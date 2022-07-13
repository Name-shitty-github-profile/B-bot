from nextcord.ext import commands 
import nextcord
class ticket_buttons(nextcord.ui.View):
  def __init__(self):
    super().__init__(timeout = None)
    self.value = None

  @nextcord.ui.button(label="ticket", style = nextcord.ButtonStyle.green)
  async def confirm(self, button : nextcord.ui.Button, interaction : nextcord.Interaction):
    view = cbtn()
    await interaction.response.send_message('Es-tu sure de vouloir faire cela?', view=view, ephemeral=True)
    await view.wait()

class cbtn(nextcord.ui.View):
  def __init__(self):
    super().__init__(timeout = None)
    self.value = None

  @nextcord.ui.button(label="Oui", style = nextcord.ButtonStyle.green)
  async def Oui(self, button : nextcord.ui.Button, interaction : nextcord.Interaction):
    for channel in interaction.guild.channels:
      if channel.name == f'ticket-{interaction.user.id}':
        await interaction.response.edit_message(content=f'Tu as déja un ticket.\n{channel.mention}', view=None)
        return
    channel = await interaction.guild.create_text_channel(f'ticket-{interaction.user.id}', category=interaction.guild.get_channel(996793841845817536))
    await channel.set_permissions(interaction.user, send_messages=True, read_messages=True)
    await interaction.response.edit_message(content=f'{channel.mention}', view=None)
    msg = await channel.send('@everyone')
    await msg.delete()
    await channel.send(embed=nextcord.Embed(title=f'Le staff sera bientot là {interaction.user.name} !', color = 0x2ecc71))

  @nextcord.ui.button(label="Non", style = nextcord.ButtonStyle.red)
  async def Non(self, button : nextcord.ui.Button, interaction : nextcord.Interaction):
    await interaction.response.edit_message(content="Demande annulée!", view=None)

class Down(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.Cog.listener("on_ready")
  async def roles(self):
    guild = self.bot.get_guild(996596265389404241)
    member_role = guild.get_role(996835567025279047)
    for member in guild.members:
      if member.bot is False: await member.add_roles(member_role)

  @commands.Cog.listener("on_ready")
  async def ticket(self):
    channel = self.bot.get_channel(996839336941203576)
    await channel.purge(limit=1)
    view = ticket_buttons()
    await channel.send(embed=nextcord.Embed(title="Faire un ticket", description="Pour faire un ticket veuillez cliquez sur le boutton vert juste en bas du message !\n\nTout ticket inutile serat sanctionné.", color=0x3498db), view=view)
    await view.wait()

def setup(bot):
  bot.add_cog(Down(bot))
