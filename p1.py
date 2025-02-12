import argparse
from src.transcriber import transcribe_audio

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert Audio to Text")
    parser.add_argument("--file", type=str, help="Path to audio file")
    parser.add_argument("--folder", type=str, help="Path to folder containing audio files")
    args = parser.parse_args()
    
    if args.file:
        transcribe_audio(args.file)
    elif args.folder:
        import os
        for file in os.listdir(args.folder):
            if file.endswith(".wav"):
                transcribe_audio(os.path.join(args.folder, file))
    else:
        print("Please provide an audio file or folder.")
```

**2. src/transcriber.py (Enhanced Transcription Logic)**
```python
import speech_recognition as sr
import os
import logging

def transcribe_audio(file_path: str) -> None:
    """Convert speech to text from an audio file and save the output."""
    logging.basicConfig(level=logging.INFO)
    recognizer = sr.Recognizer()
    
    try:
        with sr.AudioFile(file_path) as source:
            logging.info(f"Processing file: {file_path}")
            audio = recognizer.record(source)
            text = recognizer.recognize_google(audio)
            
            output_file = os.path.join("output", os.path.basename(file_path).replace(".wav", ".txt"))
            with open(output_file, "w") as f:
                f.write(text)
                logging.info(f"Transcription saved to {output_file}")
    except Exception as e:
        logging.error(f"Error processing {file_path}: {e}")
```

**3. tests/test_transcriber.py (Unit Test Added)**
```python
import unittest
from src.transcriber import transcribe_audio
import os

class TestTranscriber(unittest.TestCase):
    def test_transcription_output(self):
        test_file = "data/sample.wav"
        transcribe_audio(test_file)
        output_file = "output/sample.txt"
        self.assertTrue(os.path.exists(output_file))
        
if __name__ == "__main__":
    unittest.main()
