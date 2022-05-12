import discord
from discord.ext import commands
from discord import app_commands
import random


class RandomFromVc(commands.Cog):
    """
    コマンド送信者の接続しているボイスチャットから抽選します。
    """

    def __init__(self, bot, guild_id):
        self.command = app_commands.Command(
            name="chusen",
            description="コマンド送信者の接続しているボイスチャットから抽選します。オプション：人数",
            callback=self.chusen,
        )
        bot.tree.add_command(self.command, guild=discord.Object(id=guild_id))

    async def chusen(self, interaction: discord.Interaction, count:int=1):
        if interaction.user.voice is None:
            await interaction.response.send_message(f"VCに接続していないと抽選ができません")
            return

        await interaction.response.send_message("抽選中…", ephemeral=True)
        ids = list(interaction.user.voice.channel.voice_states.keys())
        random.shuffle(ids)
        selected_ids = ids[:count]
        selected_names = []
        for id in selected_ids:
            member = await interaction.user.guild.fetch_member(id)
            selected_names.append(member.display_name)
        
        text = '\n'.join(selected_names)
        await interaction.channel.send("==抽選結果==\n" + text)

