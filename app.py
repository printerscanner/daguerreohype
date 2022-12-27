from os import path
import time
import sys
from urllib.parse import urljoin
from bs4 import BeautifulSoup
import os
import shutil
import requests

import tweepy
import random
import urllib.request



daguerreotypes = requests.get(
    "https://www.loc.gov/collections/daguerreotypes/?fo=json&sp=12").json()  # get the JSON data

def get_image(image_url, title):

    """
    Get image based on url.
    :return: Image name if everything OK, False otherwise
    """

    image_name = path.split(image_url)[1]
    try:
        image = requests.get(image_url)
    except OSError:  # Little too wide, but work OK, no additional imports needed. Catch all conection problems
        return False
    if image.status_code == 200:  # we could have retrieved error page
        # Use your own path or "" to use current working directory. Folder must exist.
        base_dir = path.join(path.dirname(path.realpath(__file__)), "images")
        with open(path.join(base_dir, title + ".jpg"), "wb") as f:
            f.write(image.content)
        return image_name

for item in daguerreotypes['results']:
	get_image(item["image_url"][-1], item["title"][1:-1])

