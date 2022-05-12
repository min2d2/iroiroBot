import discord
from discord.ext import commands
from discord import app_commands


class Images(commands.Cog):
    """
    画像を返す
    """

    def __init__(self, bot, guild_id):
        self.command = app_commands.Command(
            name="image", description="sample command", callback=self.image
        )
        bot.tree.add_command(self.command, guild=discord.Object(id=guild_id))

    async def image(self, interaction: discord.Interaction):
        await interaction.response.send_message("み", file=discord.File('assets/my_image.png'))