from pytubefix import YouTube
import argparse
import ffmpeg
import os

DOWNLOAD_PATH = r"<your_file_output_path>"

def download_video(yt, file_name, temp_path):
    print("Downloading video...")

    video_title = f"{file_name}_temp.mp4"

    (
        yt
        .streams
        .order_by('resolution')
        .desc()
        .first()
        .download(output_path=temp_path, filename=video_title)
    )

    return f"{temp_path}\{video_title}"

def download_audio(yt, file_name, temp_path):
    print("Downloading audio...")
    
    audio_title = f"{file_name}.mp3"
    yt.streams.get_audio_only().download(output_path=temp_path, filename=audio_title)

    return fr"{temp_path}\{audio_title}"

def combine_audio_video(audio_path, video_path, output_path):
    print("Combining audio and video...")

    audio = ffmpeg.input(audio_path).audio
    video = ffmpeg.input(video_path).video

    ffmpeg.output(audio, video, output_path, codec="copy").run(overwrite_output=True, quiet=True)

def remove_temp_files(*args):    
    for file in args:
        os.remove(file)

def sanitize_filename(filename):
    return "".join(c if c.isalnum() or c in ' ._-' else '_' for c in filename)

def handle_download_video(yt, download_path):
        file_name = sanitize_filename(f"{yt.title}_{yt.author}")
        video_path = download_video(yt, file_name, download_path)
        audio_path = download_audio(yt, file_name, download_path)

        combine_audio_video(audio_path, video_path, f"{download_path}/{file_name}.mp4")

        remove_temp_files(video_path, audio_path)

def main():
    try:
        parser = argparse.ArgumentParser(description="Download YouTube video.")

        parser.add_argument("link", help="YouTube link to download")
        parser.add_argument("--mp3-only", action="store_true", help="Only download the audio in mp3")
        
        args = parser.parse_args()

        yt = YouTube(args.link)
        file_name = sanitize_filename(f"{yt.title}_{yt.author}")
        mp3_only = args.mp3_only

        if mp3_only:
            download_audio(yt, file_name, DOWNLOAD_PATH)
        else:
            handle_download_video(yt, DOWNLOAD_PATH)
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        print("Done.")

if __name__ == "__main__":
    main()
