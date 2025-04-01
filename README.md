# YouTube Japanese Subtitles Checker

A tool that checks YouTube channels for videos with manually created Japanese subtitles.

## Features

- Takes a YouTube channel URL as input
- Scans all videos in the channel
- Identifies videos with manually created Japanese subtitles
- Provides a list of videos with Japanese subtitles

## Getting Started

### Prerequisites

- Python 3.x

### Installation

1. Clone the repository
```bash
git clone https://github.com/yourusername/youtube-jp-subtitles-checker.git
cd youtube-jp-subtitles-checker
```

2. Create and activate virtual environment
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

### Usage

1. Make sure your virtual environment is activated
```bash
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
```

2. Run the script:
```bash
# example usage:
python jp.py https://www.youtube.com/@mikurealjapanese/videos
```

4. The script outputs a list of URLs with titles to the file named after the channel, like this:
```
https://www.youtube.com/watch?v=prTT0FFIH4I Let’s walk around Yokohama and learn Kanji !!
https://www.youtube.com/watch?v=0-JdEeHmrcI "GOEN" ご縁 Japanese listening about LIFE -
https://www.youtube.com/watch?v=oj39VCXLqM8 How much can you understand? Japanese conversation
...
```

## Project Structure

```
youtube-jp-subtitles-checker/
├── jp.py            # Main script
├─ helpers/           # Helper scripts, which were used to develop the main script
│  ├── video-has-manually-written-japanese-subs.py
│  └── get-list-of-videos-from-channel.py
└── README.md        # Project documentation
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Third-Party Libraries and Licenses

This project uses the following third-party libraries:

| Library | License | Description |
|---------|---------|-------------|
| [tqdm](https://github.com/tqdm/tqdm) | [MPLv2.0](https://github.com/tqdm/tqdm/blob/master/LICENCE) | A fast, extensible progress bar for Python |
| [rich](https://github.com/Textualize/rich) | [MIT](https://github.com/Textualize/rich/blob/master/LICENSE) | Rich text and beautiful formatting in the terminal |
| [yt-dlp](https://github.com/yt-dlp/yt-dlp) | [The Unlicense](https://github.com/yt-dlp/yt-dlp/blob/master/LICENSE) | A youtube-dl fork with additional features and fixes |

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
