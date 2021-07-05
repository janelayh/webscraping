from selenium import webdriver
import time
import sys
import csv
from urllib.request import urlretrieve
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException, NoSuchElementException, WebDriverException

options = Options()
options.headless = True
CHROMEDRIVER_PATH = "/Users/musiio/WYmusic/chromedriver"
driver = webdriver.Chrome("/Users/musiio/WYmusic/chromedriver")
error_urls = []
tracks = []
def get_next(csv_file):
    with open(csv_file, newline='') as csvfile:
        url_reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in url_reader:
            row_count = 0
            for url in row[0].split(','):
                # print(url)
                tracks.append(url)
                row_count +=1
    return tracks

def process_url(url):
    driver.get(url)
    time.sleep(2)

    iframe=driver.find_element_by_id('g_iframe')
    driver.switch_to.frame(iframe)

    song_id=url.split('=')[-1]
    # print(song_id)
    song_href = "http://music.163.com/song/media/outer/url?id=" + song_id + ".mp3"
    # print(song_href)
    song_name=driver.find_element(By.XPATH, '//em[@class="f-ff2"]').text + '.mp3'
    # print(song_name)
    driver.get(song_href)
    # print(driver.current_url)
    urlretrieve(driver.current_url,song_name)
    print(song_name + ' downloaded' )

if __name__ == '__main__':
    url_csv_file = sys.argv[1]

    for url in get_next(url_csv_file):
        try:
            process_url(url)
        except (TimeoutException, NoSuchElementException, WebDriverException) as e:
            error_urls.append(url)
            continue
    
    driver.quit()

    with open('errors_netease.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        for row in error_urls:
            writer.writerow([row])