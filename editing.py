from moviepy.config import change_settings
change_settings({"IMAGEMAGICK_BINARY": "C:/Program Files/ImageMagick-7.1.1-Q16/magick.exe"})
from moviepy.editor import VideoFileClip, concatenate_videoclips, TextClip, CompositeVideoClip, AudioFileClip, vfx

#Load the input video
input_video = "VideoIN.mov"  # Input video file
video = VideoFileClip(input_video)

# Define the timestamps for interesting segments(format m:s:ms)
timestamps = [
    (0 * 60 + 0 + 0 / 1000, 0 * 60 + 1 + 400 / 1000),  # 0:0:000-0:1:400
    (0 * 60 + 8 + 0 / 1000, 0 * 60 + 9 + 700 / 1000),  # 0:8:000-0:9:700
    (0 * 60 + 10 + 500 / 1000, 0 * 60 + 12 + 500 / 1000),  # 0:10:500-0:12:500
    (0 * 60 + 22 + 0 / 1000, 0 * 60 + 25 + 0 / 1000),  # 0:22:000-0:25:000
    (0 * 60 + 31 + 500 / 1000, 0 * 60 + 34 + 500 / 1000),  # 0:31:500-0:34:500
    (0 * 60 + 52 + 0 / 1000, 0 * 60 + 55 + 0 / 1000),  # 0:52:000-0:55:000
    (1 * 60 + 2 + 500 / 1000, 1 * 60 + 7 + 500 / 1000),  # 1:02:500-1:07:500
    (1 * 60 + 33 + 500 / 1000, 1 * 60 + 38 + 0 / 1000),  # 1:33:500-1:38:000
    (1 * 60 + 47 + 500 / 1000, 1 * 60 + 50 + 800 / 1000),  # 1:47:500-1:50:800
    (2 * 60 + 5 + 0 / 1000, 2 * 60 + 8 + 0 / 1000),  # 2:05:000-2:08:000
    (2 * 60 + 11 + 500 / 1000, 2 * 60 + 13 + 500 / 1000),  # 2:11:500-2:13:500
    (2 * 60 + 16 + 0 / 1000, 2 * 60 + 20 + 500 / 1000),  # 2:16:00-2:20:500
]

# Create subclips and add fade-in/out effects
clips = [video.subclip(start, end).fx(vfx.fadein, 0.5).fx(vfx.fadeout, 0.5) for start, end in timestamps]

# Concatenate the clips
final_clip = concatenate_videoclips(clips, method="compose")

# Adjust aspect ratio to 9:16 for social media reels
final_clip = final_clip.crop(width=video.h * 9 // 16, height=video.h, x_center=video.w // 2)

#  Add music and sync it to the video length
music = AudioFileClip("bgm.mp3")  # Replace with a suitable music file
music = music.subclip(0, final_clip.duration)  # Trim or loop to match video length
final_clip = final_clip.set_audio(music)

# Add dynamic text overlays with transitions and effects
text_clips = []
text_data = [
    ("AI in Action: Weaponized Robotics!", 0, 6),
    ("Precision Training for Combat", 6, 15),
    ("Are We Ready for This Future?", 15, 30),
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

# Save the final
output_video = "VideoOUT2.mp4"
final_clip.write_videofile(output_video, fps=30, codec="libx264", audio_codec="aac")

print("Video processing complete. Saved as:", output_video)
