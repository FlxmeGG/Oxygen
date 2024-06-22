import discord
from discord.ext import commands

class Kick(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command(
        name="kick",
        description="Kicks a member from the server."
    )
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, reason: str = "No reason provided"):
        await member.kick(reason=reason)
        await ctx.respond(f"{member.mention} has been kicked. Reason: {reason}")

    @kick.error
    async def kick_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.respond("You do not have the required permissions to use this command.")
        else:
            await ctx.respond("An error occurred while processing the command.")

def setup(bot):
    bot.add_cog(Kick(bot))
