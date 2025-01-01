Overview

This project demonstrates how to create a short, cinematic video using Python.
It utilizes powerful libraries like MoviePy to perform tasks such as cutting, transitioning, overlaying text, adding background music, and adjusting aspect ratios to suit different platforms (e.g., social media reels).
                                
Features

Clipping: Extract specific segments of a video based on timestamps.
Cinematic Transitions: Apply smooth fade-in and fade-out effects for professional video transitions.
Dynamic Text Overlays: Add text at specific timestamps with customizable font, size, and effects.
Background Music: Synchronize audio with the video duration for a seamless experience.
Aspect Ratio Adjustment: Optimize the video for platforms like Instagram Reels or TikTok.
Output: High-quality video output with efficient encoding.

Requirements

Before running the code, make sure you have the following installed:

Python 3.x
MoviePy: Install using pip install moviepy
FFmpeg: Ensure FFmpeg is installed and accessible via the system PATH for MoviePy to function correctly.

How to Use

Clone this repository:

                                 git clone https://github.com/ummar40/Video-editing-using-moviepy-python.git
                                 cd Video-editing-using-moviepy-python

Prepare the input video file and place it in the project directory. VideoIN.mov
Prepare the background music file and name it bgm.mp3.
Run the Python script:

                                python editing.py
																
The output video will be saved as VideoOUT2.mp4.

Customization

Timestamps: Modify the timestamps in the script to clip specific parts of your video.
Text Overlays: Update the text_data array in the script to add or customize text overlays.
Music: Replace bgm.mp3 with your own background music file.
Transitions: Change or add transition effects in the vfx section of the script.

