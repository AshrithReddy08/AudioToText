# Audio to Text Converter


Convert speech to text efficiently using Python and Google Speech API.

## Features

- Supports multiple audio formats (MP3, WAV, FLAC).
- Fast and accurate transcription.
- Simple command-line interface.
- Supports batch audio processing.
- Error handling for missing or corrupt files.

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/AshrithReddy08/AudioToText.git
   cd AudioToText
   ```
2. **Create a Virtual Environment (Recommended)**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use 'venv\\Scripts\\activate'
   ```
3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Run the script for a single file**:
   ```bash
   python src/main.py --file path/to/audio.wav
   ```
2. **Run for multiple files**:
   ```bash
   python src/main.py --folder path/to/audio_directory
   ```
3. **Output**:
   - The transcribed text is saved in `output/`.

## Directory Structure
```
AudioToText/
├── src/                  # Source code
│   ├── main.py           # Main script
│   ├── transcriber.py    # Core transcription logic
│   ├── utils.py          # Utility functions
├── tests/                # Unit tests
├── data/                 # Sample audio files
├── output/               # Transcription output
├── docs/                 # Documentation
├── requirements.txt      # Required packages
├── .gitignore            # Ignore unnecessary files
├── LICENSE               # License information
├── README.md             # Project description
```

## Technologies Used
- Python
- Google Speech Recognition API
- pydub (for audio processing)
- wave (for handling WAV files)

## Contributing
Contributions are welcome! Feel free to open an issue or submit a pull request.

## License
This project is licensed under the MIT License.

---
