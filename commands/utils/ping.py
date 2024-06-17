from discord.ext import commands

class Ping(Commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.slash_command(name="ping",description="Get the latency of the bot.")
  async def ping(self, ctx):
    latency = self.bot.latency * 1000
    embed = discord.Embed(description=f"Pong! Current latency is {latency}ms")
    embed.set_footer(f"Requested by {ctx.author}")
    await ctx.respond(embed=embed)

def setup(bot):
  bot.add_cog(Ping(bot))
