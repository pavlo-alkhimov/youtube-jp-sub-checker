from tqdm import tqdm
from rich.console import Console
import yt_dlp
import sys
import re

def sanitize_filename(name):
    return re.sub(r'[<>:"/\\|?*]', '_', name)

def get_videos_from_channel(channel_url):
    ydl_opts = {
        'quiet': True,
        'extract_flat': True,
        'skip_download': True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(channel_url, download=False)
        if 'entries' not in info:
            print("No videos found or invalid channel URL.", file=sys.stderr)
            sys.exit(1)
        return info.get('title', 'unknown_channel'), [entry['url'] for entry in info.get('entries', [])]

def has_manual_japanese_subs(video_url):
    ydl_opts = {
        'quiet': True,
        'skip_download': True,
        'writesubtitles': True,
        'subtitleslangs': ['ja'],
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            info = ydl.extract_info(video_url, download=False)
            subs = info.get('subtitles', {})
            return 'ja' in subs and 'url' in subs['ja'][0]
        except yt_dlp.utils.DownloadError:
            return False

def main():
    if len(sys.argv) < 2:
        print("Usage: python script.py <YouTube Channel URL>", file=sys.stderr)
        sys.exit(1)

    channel_url = sys.argv[1]

    try:
        channel_name, video_urls = get_videos_from_channel(channel_url)
    except Exception as e:
        sys.exit(1)

    sanitized_name = sanitize_filename(channel_name)
    output_file = f"{sanitized_name}.txt"

    print(f"Searching on {channel_name} for videos with manually written japanese subs and saving found URLs to {output_file}")

    console = Console()

    with open(output_file, "w") as f:
        with tqdm(total=len(video_urls), desc="Processing URLs", ncols=120, unit="url") as pbar:
            for url in video_urls:
                console.print(f" [cyan]Checking:[/cyan] {url}", end="\r")
                
                if has_manual_japanese_subs(url):
                    console.print(f"[bold magenta]✔ Found Manual JP Subs:[/bold magenta] {url}", end="\r")
                    f.write(url + "\n")

                pbar.update(1)  # ✅ Keeps the progress bar moving

if __name__ == "__main__":
    main()
