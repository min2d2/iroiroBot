from discord.ext import commands


class BasicListener(commands.Cog):
    """
    on_messageで何かする系
    prefixありのコマンドはbasic_command.pyの書き方のほうがいい
    """

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return

        if "セミ" in message.content:
            await message.channel.send("セミ！！")
