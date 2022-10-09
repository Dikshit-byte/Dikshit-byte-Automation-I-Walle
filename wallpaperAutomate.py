"""
 tasks -> 1. Get wallpaper from the internet
 2. Save it to a temp directory
 3. set the wallpaper
 4. Automate the calls to this script
"""
from logging import exception
import os
import pprint
from urllib import response
import requests
import wget
import ctypes
import time

def getwallpaper():
    os.environ['UNSPLASH_ACCESS_KEY'] = 'OkTe6NDCvHrJkZe0FREv2Eu4cha4EgiPwrxfJ8zgGI0'
    # pprint.pprint(dict(os.environ),width=1)
    access_key = os.environ.get('UNSPLASH_ACCESS_KEY','non')
    # print(access_key)
    url = "https://api.unsplash.com/photos/random/?client_id="+access_key
    params = {
        "query":"HD wallpaper",
        "orientation":"landscape"
    }
    response = requests.get(url,params).json()
    image_url = response['urls']['full']
    # print(image_url)
    wallpaper = wget.download(image_url,"C:\\Users\\singh\\AppData\\Local\\Temp\\wallpaper.jpg")
    print(wallpaper)
    # print(response.status_code)
    # print(response.json())
    return wallpaper

def setwallpaper():
    wallpaper = getwallpaper()
    ctypes.windll.user32.SystemParametersInfoW(20, 0, wallpaper , 0)

def main():
    try:
        while True:
            setwallpaper()
            time.sleep(2)
            print("Set the wallpaper...👍👍")
    except KeyboardInterrupt:
        "Hope you like this wallpaper! Quitting"
    except Exception:
        pass


if __name__ == '__main__':
    main()
