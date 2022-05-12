from discord.ext import commands


class VcLog(commands.Cog):
    """
    VC接続・切断ログ
    """

    def __init__(self, bot, log_channel_id):
        self.bot = bot
        self.log_channel_id = log_channel_id

    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        log_channel = self.bot.get_channel(self.log_channel_id)
        if before.channel is None:
            msg = f"{member.name} が {after.channel.name} に参加しました。"
            await log_channel.send(msg)

        elif after.channel is None:
            msg = f"{member.name} が {before.channel.name} から退出しました。"
            await log_channel.send(msg)

        else:
            msg = f"{member.name} が {after.channel.name} に移動しました。"
            await log_channel.send(msg)
