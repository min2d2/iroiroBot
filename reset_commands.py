import asyncio
import discord
from discord.ext import commands

import settings

intents = discord.Intents.default()
intents.message_content = True
intents.typing = False
intents.presences = False


class MyBot(commands.Bot):
    def __init__(self, command_prefix, intents):
        super().__init__(command_prefix=command_prefix, intents=intents)

    async def on_ready(self):
        print("-----")
        print(self.user.name)
        print(self.user.id)
        print("-----")
        # スラッシュコマンド・コンテキストメニューの反映
        self.tree.clear_commands(guild=discord.Object(id=settings.GUILD_ID))
        await self.tree.sync(guild=discord.Object(id=settings.GUILD_ID))
        print("synced application commands")
        await self.close()


def prefix(bot, message):
    return ["!", settings.BOT_NAME]


async def main():
    bot = MyBot(intents=intents, command_prefix=prefix)
    await bot.start(settings.TOKEN)


asyncio.run(main())


# スラッシュコマンド・コンテキストメニューのリセット用スクリプトです
# スラッシュコマンド・コンテキストメニューがすべて消えます。
# 削除は成功しますが終了時エラー出ます(デバッグ使用のみなので放置)
