import disnake
from source.packages.single_video_downloader import download_audio
from disnake.ext import commands

class AudioPlayer(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="play",
                            description="Download video from youtube and play it in a voice channel")
    async def download(self, ctx, video_url: str):
        await ctx.send(f"Downloading video from {video_url}...", ephemeral=True)
        path = await download_audio(video_url)
        channel = ctx.author.voice.channel
        voice_client = await channel.connect()
        voice_client.play(disnake.FFmpegOpusAudio(path))



def setup(bot):
    bot.add_cog(AudioPlayer(bot))
