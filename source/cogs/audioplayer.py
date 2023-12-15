import disnake
from packages.single_video_downloader import download_audio
from disnake.ext import commands



class AudioPlayer(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="griffy",
                            description="Join bot and play music")
    async def download(self, ctx):
        input_link = disnake.ui.Modal.add_text_input(ctx,
                                                     label="Youtube URL",
                                                     custom_id="url",
                                                     style=disnake.TextInputStyle.single_line)
        await ctx.send(f"Downloading video from {video_url}...", ephemeral=True)
        path = await download_audio(video_url)
        channel = ctx.author.voice.channel
        voice_client = await channel.connect()
        voice_client.play(disnake.FFmpegOpusAudio(path))




def setup(bot):
    bot.add_cog(AudioPlayer(bot))