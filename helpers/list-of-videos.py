import sys
import subprocess
import json

def get_channel_videos(channel_url):
    command = [
        "yt-dlp",
        "--flat-playlist",
        "-J",
        channel_url
    ]
    result = subprocess.run(command, capture_output=True, text=True)

    data = json.loads(result.stdout)
    video_urls = [entry["url"] for entry in data["entries"]]

    return video_urls

if __name__ == "__main__":

    # take the first parameter of thge script and pass it to the function
    # has_manual_japanese_subs(sys.argv[1])
    # if the parameter not provided, do nothing.

    if len(sys.argv) == 2 and "youtube.com/" in sys.argv[1]:
        video_urls = get_channel_videos(sys.argv[1])

        # output to stderr
        print(f"Total Videos: {len(video_urls)}", file=sys.stderr)
    
        for url in video_urls:
            print(url)
