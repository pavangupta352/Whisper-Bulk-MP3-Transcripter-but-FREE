import os
import whisper
from pathlib import Path

# Load the Whisper model
model_type = "base"  # Adjust model size as needed
model = whisper.load_model(model_type)


def transcribe_audio(file_path, output_dir):
    """
    Transcribes the given audio file and saves the transcription to a text file.
    :param file_path: Path to the audio file.
    :param output_dir: Directory where the transcript text file will be saved.
    """
    # Transcribe the audio
    result = model.transcribe(file_path)
    text = result["text"]

    # Generate the output file path
    output_file_path = os.path.join(output_dir, os.path.splitext(
        os.path.basename(file_path))[0] + ".txt")

    # Save the transcription
    with open(output_file_path, "w") as text_file:
        text_file.write(text)

    print(f"Transcribed: {file_path} -> {output_file_path}")


def main():
    # Directory containing the MP3 files
    input_dir = "X:\whisper\input folder"
    # Directory where the text files will be saved
    output_dir = "X:\whisper\output folder"

    # Create the output directory if it doesn't exist
    Path(output_dir).mkdir(parents=True, exist_ok=True)

    # List all MP3 files
    mp3_files = [f for f in os.listdir(input_dir) if f.endswith(".mp3")]

    # Total number of files
    total_files = len(mp3_files)

    # Iterate over all MP3 files and keep track of progress
    for i, file_name in enumerate(mp3_files, 1):
        file_path = os.path.join(input_dir, file_name)
        print(f"Processing {i}/{total_files}: {file_name}")
        transcribe_audio(file_path, output_dir)

        # # Print progress
        # progress_percentage = (i / total_files) * 100
        # print(f"Progress: {progress_percentage:.2f}%")


if __name__ == "__main__":
    main()
