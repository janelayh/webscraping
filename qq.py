import requests
import csv
import time
from selenium import webdriver
import sys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException, NoSuchElementException, WebDriverException

options = Options()
options.headless = True
CHROMEDRIVER_PATH = "/Users/musiio/WYmusic/chromedriver"
driver = webdriver.Chrome(CHROMEDRIVER_PATH, options=options)
wait = WebDriverWait(driver, 50)

#https://y.qq.com/n/yqq/mv/v/i00348iiq8l.html
#https://c.y.qq.com/base/fcgi-bin/u?__=3YNCfEW
#https://c.y.qq.com/base/fcgi-bin/u?__=oT7xfEh


tracks = []
def get_next(csv_file):
    with open(csv_file, newline='') as csvfile:
        url_reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in url_reader:
            row_count = 0
            for url in row[0].split(','):
                tracks.append(url)
                row_count +=1
    return tracks
    
error_urls = []
# tracks = ["https://c.y.qq.com/n/ryqq/songDetail/002m8nmu2Xtwah", "https://c.y.qq.com/base/fcgi-bin/u?__=oT7xfEh", "https://y.qq.com/n/yqq/mv/v/i00348iiq8l.html"]

def process_url(url):
            if url.split('/')[3] == "base" or url.split('/')[5] == "songDetail": 

                driver.get(url)                
                time.sleep(5)

                driver.current_url
                
                title= driver.find_element(By.XPATH, '//h1[@class="data__name_txt"]').get_attribute('title')
                wait.until(EC.element_to_be_clickable((By.XPATH, '//span[@class="btn__txt"]/..'))).click()
                time.sleep(5)

                driver.switch_to.window(driver.window_handles[-1])
                time.sleep(5)

                button=driver.find_element(By.XPATH, '//span[@class="yqq-dialog-close-x"]')
                button.click()

                song_href = driver.find_element(By.XPATH, '//audio[@preload="auto"]').get_attribute('src')
                song_name = title + " - " + driver.find_element(By.XPATH, '//a[@class="playlist__author"]').get_attribute('title')
                music = requests.get(url=song_href)

                with open('%s.mp4' % song_name, 'wb') as file:
                        file.write(music.content)
                        print('<%s> successfully downloaded!' % song_name)
                driver.switch_to.window(driver.window_handles[0])

            elif url.split('/')[5] == "mv":
                driver.get(url)
              
                wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="mv__name"]')))

                song_name = driver.find_element(By.XPATH, '//span[@class="mv__name"]').get_attribute('title') + "-" + driver.find_element(By.XPATH, '//a[@class="mv__singer js_singer"]').text
                song_href = driver.find_element(By.XPATH, '//video[@id="video_player__source"]').get_attribute('src')

                music = requests.get(url=song_href)

                with open('%s.mp4' % song_name, 'wb') as file:
                        file.write(music.content)
                        print('<%s> successfully downloaded!' % song_name)
            else:
                error_urls.append(url)
        
if __name__ == '__main__':
    url_csv_file = sys.argv[1]

    for url in get_next(url_csv_file):
        try:
                process_url(url)
        except (TimeoutException, NoSuchElementException, WebDriverException) as e:
            error_urls.append(url)
            continue
        
    with open('errors_qq.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        for row in error_urls:
            writer.writerow([row])
