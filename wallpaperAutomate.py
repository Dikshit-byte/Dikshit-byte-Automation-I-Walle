"""
 tasks -> 1. Get wallpaper from the internet
 2. Save it to a temp directory
 3. set the wallpaper
 4. Automate the calls to this script
"""
import os
import pprint
from urllib import response
import requests
import wget

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
    
def main():
    

if __name__ == '__main__':
    main()
