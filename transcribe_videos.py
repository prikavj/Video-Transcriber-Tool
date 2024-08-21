import whisper
import os
from moviepy.editor import VideoFileClip

# Define the default input and output directories
input_directory = "/path/to/your/input/videos"
output_directory = "/path/to/your/output/transcripts"

# Ensure the output directory exists; create it if it doesn't
os.makedirs(output_directory, exist_ok=True)

# Load the Whisper model; customize the model type as needed
# For more information about the Whisper model, visit:
# https://github.com/openai/whisper
model = whisper.load_model("medium.en")

def transcribe_video(video_path, output_path):
    """
    Extracts audio from the video file, transcribes it using Whisper,
    and saves the transcription as a text file.
    
    Parameters:
    video_path (str): The path to the video file to be transcribed.
    output_path (str): The base path where the output files will be saved (without extension).
    """
    # Extract the audio from the video
    video = VideoFileClip(video_path)
    audio_path = output_path + '.wav'
    video.audio.write_audiofile(audio_path, codec='pcm_s16le')
    
    # Transcribe the extracted audio using Whisper
    result = model.transcribe(audio_path)
    
    # Save the transcription to a text file
    transcript_path = output_path + '.txt'
    with open(transcript_path, 'w') as f:
        f.write(result['text'])

    # Optionally, remove the audio file after transcription to save space
    os.remove(audio_path)
    print(f"Transcription saved to {transcript_path}")

def main():
    """
    Main function to transcribe all MP4 videos in the input directory.
    """
    # Loop through all files in the input directory
    for filename in os.listdir(input_directory):
        if filename.lower().endswith(".mp4"):  # Check if the file is an MP4 video
            video_path = os.path.join(input_directory, filename)
            output_path = os.path.join(output_directory, os.path.splitext(filename)[0])
            transcribe_video(video_path, output_path)

    print("All transcriptions completed.")


if __name__ == "__main__":
    main()
