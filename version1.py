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
import random

"""
Get specific wallpaper of your favourite choice 
"""
def getwallpaper_with_query(query):
    # pprint.pprint(dict(os.environ),width=1)
    access_key = os.environ.get('UNSPLASH_ACCESS_KEY2', 'non')
    url = "https://api.unsplash.com/search/photos?query="+query+"&client_id="+access_key
    params = {
        "query": "HD wallpaper",
        "orientation": "landscape"
    }
    number = random.randint(0,10)
    response = requests.get(url,params).json()
    response1 = response['results']
    # print(number)
    image_url = response1[number]['urls']['full']
    # print(image_url)
    wallpaper = wget.download(
        image_url, "C:\\Users\\singh\\AppData\\Local\\Temp\\wallpaper.jpg")
    return wallpaper


def setwallpaper_with_query(query):
    wallpaper = getwallpaper_with_query(query)
    ctypes.windll.user32.SystemParametersInfoW(20, 0, wallpaper, 0)


def main1(query):
    try:
        while True:
            setwallpaper_with_query(query)
            time.sleep(2)
            print("Set the wallpaper...👍👍")
    except KeyboardInterrupt:
        "Hope you like this wallpaper! Quitting"
    except Exception:
        pass

"""
    for random wallpaper without any query
"""
def getwallpaper_random():
    access_key = os.environ.get('UNSPLASH_ACCESS_KEY1','non')
    url = "https://api.unsplash.com/photos/random/?client_id="+access_key
    params = {
        "query":"HD wallpaper",
        "orientation":"landscape"
    }
    response = requests.get(url,params).json()
    image_url = response['urls']['full']
    wallpaper = wget.download(image_url,"C:\\Users\\singh\\AppData\\Local\\Temp\\wallpaper.jpg")
    print(wallpaper)
    return wallpaper

def setwallpaper_random():
    wallpaper = getwallpaper_random()
    ctypes.windll.user32.SystemParametersInfoW(20, 0, wallpaper , 0)

def main2():
    try:
        while True:
            setwallpaper_random()
            time.sleep(2)
            print("Set the wallpaper...👍👍")
    except KeyboardInterrupt:
        "Hope you like this wallpaper! Quitting"
    except Exception:
        pass


if __name__ == '__main__':
    print("How would u like to set ur wallpaper ??")
    print("1. Random wallpaper")
    print("2. Any specific keyword wallpaper")
    while True:
        try:
            question = int(input("Out of these options which would you like to choose?"))
            break
        except:
            print("This is not in option! Don't be oversmart bruh!!")

    if question == 1:
        main2()
    if question == 2:
        query = input("Enter keyword for specific type of wallpaper set : ")
        main1(query)
    else:
        print("Again run the code bruh and don't choose the option which is out of scope")

