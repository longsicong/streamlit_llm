from pytube import YouTube

VIDEO_ID = "ERK34RQq9YU"

# Replace with the YouTube video URL you want to download audio from
video_url = "https://www.youtube.com/watch?v=" + VIDEO_ID

# Create a YouTube object
yt = YouTube(video_url)

# # Create a YouTube object
# yt = YouTube(video_url)

# Get the video title
video_title = yt.title

# Choose the audio stream with the highest quality
audio_stream = yt.streams.filter(only_audio=True, file_extension="mp4").first()

# Define the path to save the downloaded audio
save_path = video_title + ".mp3"  # Save as MP3 format

# Download the audio
audio_stream.download(output_path=save_path)

print("Audio downloaded successfully!")
