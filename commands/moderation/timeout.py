import discord
from discord.ext import commands
import datetime

class Timeout(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command(
        name="timeout",
        description="Timeouts a member."
    )
    @commands.has_permissions(moderate_members=True)
    async def timeout(self, ctx, member: discord.Member, duration: int, unit: discord.Option(str, choices=["seconds", "minutes", "hours", "days"]), reason: str = "No reason provided"):
        if unit == "seconds":
            delta = datetime.timedelta(seconds=duration)
        elif unit == "minutes":
            delta = datetime.timedelta(minutes=duration)
        elif unit == "hours":
            delta = datetime.timedelta(hours=duration)
        elif unit == "days":
            delta = datetime.timedelta(days=duration)

        timeout_until = discord.utils.utcnow() + delta
        await member.timeout(until=timeout_until, reason=reason)
        await ctx.respond(f"{member.mention} has been timed out for {duration} {unit}. Reason: {reason}")

    @timeout.error
    async def timeout_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.respond("You do not have the required permissions to use this command.")
        else:
            await ctx.respond("An error occurred while processing the command.")

def setup(bot):
    bot.add_cog(Timeout(bot))