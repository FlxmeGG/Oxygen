import discord
from discord.ext import commands

class Ban(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command(
        name="ban",
        description="Bans a member from the server."
    )
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, reason: str = "No reason provided"):
        await member.ban(reason=reason)
        await ctx.respond(f"{member.mention} has been banned. Reason: {reason}")

    @ban.error
    async def ban_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.respond("You do not have the required permissions to use this command.")
        else:
            await ctx.respond("An error occurred while processing the command.")

def setup(bot):
    bot.add_cog(Ban(bot))