import sys
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import TranscriptsDisabled, VideoUnavailable

def has_manual_japanese_subs(video_url):
    try:
        video_id = video_url.split("v=")[-1].split("&")[0]
        transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)

        # if the vide has manually written japanese subs, print the video url to the stdout
        # if the video has automatically generated japanese subs, print the video url to the stderr
        for transcript in transcript_list:
            if transcript.language_code == 'ja':
                if not transcript.is_generated:
                    print(video_url)
                else:
                    print(video_url, file=sys.stderr)

    except (TranscriptsDisabled, VideoUnavailable, Exception):
        return

if __name__ == "__main__":
    # take the first parameter of thge script and pass it to the function
    # has_manual_japanese_subs(sys.argv[1])
    # if the parameter not provided, do nothing.

    if len(sys.argv) == 2 and "youtube.com/watch?v=" in sys.argv[1]:
        has_manual_japanese_subs(sys.argv[1])
