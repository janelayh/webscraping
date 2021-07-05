# webscraping
To web-scrape data from chinese music websites (QQ Music, NetEase Music) and automate downloading hundreds of tracks using Selenium and Requests.

## Scripts:
  1. [qq.py](https://github.com/janelayh/webscraping/blob/main/qq.py): Automate downloading audio tracks and/or music videos from QQ Music in mp4 format.
  2. [netease.py](https://github.com/janelayh/webscraping/blob/main/netease.py): Automate downloading audio tracks from NetEase Music in mp3 format.

## What to install:
  1. [Python3](https://www.python.org/downloads/)
  2. Selenium (`pip3 install selenium`)
  3. VPN with China server
  4. [chromedriver](https://chromedriver.chromium.org/)

## How to use script:
  1. Put all the urls of audio tracks that you want to download in a CSV file (starting from row A1, one row per url).
  2. For qq.py, enter in terminal: `python3 qq.py input.csv`
  3. For netease.py, enter in terminal: `python3 netease.py input.csv`
  4. If any urls have errors (e.g. does not exist, wrong url), they will be written to a file `errors_qq.csv` (for QQ Music script) or `errors_netease.csv` (for NetEase Music script).

> ### Credits to Musiio for giving me the opportunity to learn and build these scripts!
