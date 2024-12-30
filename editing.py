from moviepy.config import change_settings
change_settings({"IMAGEMAGICK_BINARY": "C:/Program Files/ImageMagick-7.1.1-Q16/magick.exe"})
from moviepy.editor import VideoFileClip, concatenate_videoclips, TextClip, CompositeVideoClip, AudioFileClip, vfx

# Load the input video
input_video = "VideoIN.mov"  # Input video file
video = VideoFileClip(input_video)

# Define timestamps for interesting segments
timestamps = [
    (0.3 + 700 / 1000, 0.5 + 152 / 1000),
    (0.11 + 153 / 1000, 0.12 + 905 / 1000),
    (0.21 + 400 / 1000, 0.28 + 500 / 1000),
    (0.31 + 0 / 1000, 30.3 + 0 / 1000),
    (0.39 + 500 / 1000, 0.45 + 0 / 1000),
    (0.47 + 300 / 1000, 0.56 + 0 / 1000),
    (1.3 + 100 / 1000, 1.6 + 500 / 1000),
    (1.10 + 0 / 1000, 1.13 + 500 / 1000),
    (1.31 + 0 / 1000, 1.40 + 9 / 1000),
    (1.44 + 200 / 1000, 1.54 + 0 / 1000),
    (2.3 + 0 / 1000, 2.10 + 0 / 1000),
    (2.11 + 0 / 1000, 2.20 + 0 / 1000),
    (3.25 + 0 / 1000, 3.35 + 400 / 1000),
]

# Create subclips and add fade-in/out effects
clips = [video.subclip(start, end).fx(vfx.fadein, 0.5).fx(vfx.fadeout, 0.5) for start, end in timestamps]

# Concatenate the clips
final_clip = concatenate_videoclips(clips, method="compose")

# Adjust aspect ratio to 9:16 for social media reels
final_clip = final_clip.crop(width=video.h * 9 // 16, height=video.h, x_center=video.w // 2)

# Add music and sync it to the video length
music = AudioFileClip("bgm.mp3")  # Replace with a suitable music file
music = music.subclip(0, final_clip.duration)  # Trim or loop to match video length
final_clip = final_clip.set_audio(music)

# Add dynamic text overlays with transitions and effects
text_clips = []
text_data = [
    ("AI in Action: Weaponized Robotics!", 0, 9),
    ("Precision Training for Combat", 9, 20),
    ("Are We Ready for This Future?", 20, 31),
]

# Create text overlays and position them slightly above the bottom, centered horizontally
for text, start, end in text_data:
    txt_clip = (
        TextClip(
            text,
            fontsize=40,
            color="white",
            bg_color="rgba(0, 0, 0, 0.6)",  # Semi-transparent background
            font="Arial-Bold"  # Specify a bold font for emphasis
        )
        .set_position(("center", "bottom"))  # Center horizontally, slightly above the bottom
        .set_start(start)
        .set_duration(end - start)
        .fx(vfx.fadein, 0.5)  # Add fade-in effect
        .fx(vfx.fadeout, 0.5)  # Add fade-out effect
    )
    text_clips.append(txt_clip)

# Add text overlays to the video
final_clip = CompositeVideoClip([final_clip, *text_clips])

#Save the final video with high quality
output_video = "VideoOUT.mp4"
final_clip.write_videofile(output_video, fps=30, codec="libx264", audio_codec="aac")

print("Video processing complete. Saved as:", output_video)
