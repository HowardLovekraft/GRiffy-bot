from datetime import datetime
from pytube import YouTube
from pytube.exceptions import VideoUnavailable
from icecream import ic

async def download_audio(video_url: str, is_debug=False) -> str|bool:
    try:
        yt = YouTube(video_url, use_oauth=True, allow_oauth_cache=True)
    except VideoUnavailable:
        ic(f"Video {video_url} is not available")
    else:
        cur_date = datetime.today()
        date = {"year": cur_date.year, "month": cur_date.month, "day": cur_date.day}
        streams = yt.streams.filter(only_audio=True).first()
        if is_debug:
            ic(streams)
        try:
            streams.download(filename=f"{yt.title}.opus",
                             output_path=f"audios/{date['year']}/{date['month']}/{date['day']}")
            return f"audios/{date['year']}/{date['month']}/{date['day']}/{yt.title}.opus"
        except:
            ic("Error downloading audio")
        return False

# download_audio("https://www.youtube.com/watch?v=44UaY-AN6ho")