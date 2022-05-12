import discord
from discord.ext import commands
from discord import app_commands
import random


class Omikuji(commands.Cog):
    """
    おみくじ(スラッシュコマンド)
    結果一覧は設定ファイルに指定、引数で持ってきています
    """

    def __init__(self, bot, guild_id, candidates):
        self.candidates = candidates
        command = app_commands.Command(
            name="omikuji", description="おみくじ", callback=self.omikuji
        )
        bot.tree.add_command(command, guild=discord.Object(id=guild_id))

    async def omikuji(self, interaction: discord.Interaction):
        selected = random.choice(self.candidates)
        text = f"{interaction.user.name} さんの結果は {selected} です"
        await interaction.response.send_message(text)
