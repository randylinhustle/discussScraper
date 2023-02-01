from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import csv

options = Options()
options.headless = True

browser = webdriver.Chrome(executable_path='/Users/randylin/Desktop/hkdiscuss/chromedriver', options=options)

base_url = 'https://www.discuss.com.hk/archiver/?tid-'

with open('27940000_29000000.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['id', 'title'])

    for i in range(28050599, 29000000):
        url = f'{base_url}{i}.html'
        browser.get(url)

        try:
            element = browser.find_element_by_xpath('/html/body/div/h1/a')
            element_text = element.text.replace("查看完整版本 : ", "").strip()
            writer.writerow([i, element_text])
            print(f'Page {i}: {element_text}')
        except:
            pass

browser.quit()