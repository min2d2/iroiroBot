import asyncio
import discord
from discord.ext import commands

from cogs.basic_command import BasicCommand
from cogs.basic_listener import BasicListener
from cogs.list_reactions import ListReactions
from cogs.omikuji import Omikuji
from cogs.random_from_vc import RandomFromVc
from cogs.vc_log import VcLog
from cogs.images import Images

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
        await self.tree.sync(guild=discord.Object(id=settings.GUILD_ID))
        print("synced application commands")


async def main():
    bot = MyBot(intents=intents, command_prefix=settings.PREFIX)

    # 不要なCogは以下からコメントアウトしてください
    await bot.add_cog(BasicCommand(bot))
    await bot.add_cog(BasicListener(bot))
    await bot.add_cog(Images(bot, settings.GUILD_ID))
    await bot.add_cog(ListReactions(bot, settings.GUILD_ID, settings.API_ENDPOINT))
    await bot.add_cog(Omikuji(bot, settings.GUILD_ID, settings.OMIKUJI_CANDIDATES))
    await bot.add_cog(RandomFromVc(bot, settings.GUILD_ID))
    await bot.add_cog(VcLog(bot, settings.LOG_CHANNEL))

    await bot.start(settings.TOKEN)


asyncio.run(main())
