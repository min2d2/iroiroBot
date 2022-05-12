from discord.ext import commands


class BasicCommand(commands.Cog):
    """
    app.py で prefix指定した文字 +コマンド名でコマンド発動
    (この例では [プレフィックス]hello で発動)
    複数ファイルに分けてコマンドを書く場合でもon_command_errorは共通なので1個でいい
    コマンドを作るならslash.pyのようにスラッシュコマンドにするほうがいいかも？
    """

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="hello")
    async def sample(self, ctx):
        await ctx.send("world")

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        await ctx.send("そのコマンドは存在しません。「/」から始まるコマンドもお試し下さい。")
        return
