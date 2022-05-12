import discord
from discord.ext import commands
from discord import app_commands

import json
import urllib.error
import urllib.request


class ListReactions(commands.Cog):
    """
    メッセージ右クリックしてアプリ選ぶと出てくるやつ
    メッセージについているリアクションとメッセージの情報をjson形式で指定のエンドポイントにポストする
    形式は {'reactions': list, "content":message.content}
    """

    def __init__(self, bot, guild_id, endpoint) -> None:
        self.endpoint = endpoint
        self.ctx_menu = app_commands.ContextMenu(
            name="シートに送信", callback=self.send_sheet
        )
        bot.tree.add_command(self.ctx_menu, guild=discord.Object(id=guild_id))

    async def send_sheet(
        self, interaction: discord.Interaction, message: discord.Message
    ):
        await interaction.response.send_message("OK", ephemeral=True)
        list = []
        for reaction in message.reactions:
            emoji = reaction.emoji
            if type(reaction.emoji) is discord.Emoji:
                emoji = reaction.emoji.name

            users = [user async for user in reaction.users()]
            for user in users:
                obj = {"emoji": emoji, "user": {"id": user.id, "name": user.name}}
                list.append(obj)

        self.request({"reactions": list, "content": message.content})

    def request(self, data):
        request = urllib.request.Request(
            self.endpoint,
            headers={"Content-Type": "application/json"},
            data=json.dumps(data).encode("utf-8"),
        )

        try:
            with urllib.request.urlopen(request, timeout=2) as response:
                response_data = response.read()
            print("request success")
            print(response_data)

        except urllib.error.HTTPError as e:
            print(f"Server returned error: " f"status = {e.code} reason = {e.reason}")
        except urllib.error.URLError as e:
            print(f"Handler returned error: " f"reason = {e.reason}")
