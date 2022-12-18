from logging import exception
import os
import pprint
from urllib import response
import requests
import wget
import ctypes
import time
import random

#getting the random wallpaper from unsplash api's
def getwallpaper_random():
    access_key = os.environ.get('UNSPLASH_ACCESS_KEY1','UNSPLASH_ACCESS_KEY2')
    url = "https://api.unsplash.com/photos/random/?client_id="+access_key
    params = {
        "query" : "HD wallpaper",
        "orientation":"landscape"
    }
    response = requests.get(url,params).json()
    image_url = response['urls']['full']
    wallpaper = wget.download(image_url,"C:\\Users\\singh\\AppData\\Local\\Temp\\wallpaper.jpg")
    return wallpaper

#set random wallpaper on background with help of systemparameters of windows
def setwallpaper_random():
    wallpaper = getwallpaper_random()
    ctypes.windll.user32.SystemParametersInfoW(20, 0, wallpaper , 0)

#running this without parameter function for random wallpaper in every 5 sec until user get his favourite wallpaper 
def main1():
    try:
        while True:
            setwallpaper_random()
            time.sleep(5)
            print("\nSet the wallpaper successfully!!👍👍")
    except KeyboardInterrupt:
        print("\nHope you like this wallpaper!")
    except Exception:
        pass

#getting the specific wallpaper from unsplash api
def getwallpaper_with_query(query):
    # pprint.pprint(dict(os.environ),width=1)
    number = random.randint(0,10)
    access_key = os.environ.get('UNSPLASH_ACCESS_KEY2', 'UNSPLASH_ACCESS_KEY1')
    url = "https://api.unsplash.com/search/photos?page=1&query="+query+"&client_id="+access_key
    params = {
        "query": "HD wallpaper",
        "orientation": "landscape"
    }
    response = requests.get(url,params).json()
    image_url = response['results'][number]['urls']['full']
    wallpaper = wget.download(
        image_url, "C:\\Users\\singh\\AppData\\Local\\Temp\\wallpaper.jpg")
    return wallpaper

#set specific wallpaper on background with help of systemparameters of windows
def setwallpaper_with_query(query):
    wallpaper = getwallpaper_with_query(query)
    ctypes.windll.user32.SystemParametersInfoW(20, 0, wallpaper, 0)


#running this with parameter function for specific wallpaper in every 5 sec until user get his favourite wallpaper
def main2(query):
    try:
        while True:
            setwallpaper_with_query(query)
            time.sleep(5)
            print("\nSet the wallpaper successfully!!👍👍")
    except KeyboardInterrupt:
        print("\nHope you like this wallpaper!")
    except Exception:
        pass

if __name__ == '__main__':
    print("How would u like to set ur wallpaper??\n1.Random Wallpaper\n2.Any specific keyword wallpaper")

#invalid input handling
    while True:
        try:
            question = int(input("Out of these options which would you like to choose ? : "))
            break
        except:
            print("This is not in option! Don't be oversmart bruh!!")

#calling function as per the user choice
    if question == 1:
        main1()

    if question == 2:
        query = input("Enter keyword for specific type of wallpaper set : ")
        main2(query)
    
    else:
        print("Now run again. And don't choose the option which is out of scope!!🧐")
