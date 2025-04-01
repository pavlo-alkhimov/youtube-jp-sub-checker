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
- YouTube Data API key

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

4. Set up your YouTube API key
- Create a project in Google Cloud Console
- Enable YouTube Data API
- Create credentials (API key)
- Add your API key to `config.py`

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
python main.py
```

3. Enter the YouTube channel URL when prompted

4. The script will display a list of videos that have manually created Japanese subtitles

5. To deactivate the virtual environment when done:
```bash
deactivate
```

## Project Structure

```
youtube-jp-subtitles-checker/
├── main.py              # Main script
├── config.py            # Configuration settings
├── requirements.txt     # Project dependencies
└── README.md
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
