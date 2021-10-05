from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
import random


PATH = "E:\\Code\\KSF\\chromedriver.exe"
timeout = 3

# options for Chrome
options = webdriver.ChromeOptions()
options.add_argument("--headless")

driver = webdriver.Chrome(PATH, options=options)

# website
driver.get("https://www.pravda.com.ua/news/")

# acquiring lenght of news list to pick a random news in that range
sub_news = driver.find_elements_by_class_name("article_news_list")
lenght = len(sub_news)

# randomly guessing which news header are we going to work with
item_in_list = random.randint(1, lenght)

# acquiring a news header name on the first page
header = driver.find_element_by_xpath("//div[@class='container_sub_news_list_wrapper mode1']/div[{}]/div[@class='article_content']/div[@class='article_header']/a".format(item_in_list)).text

# removing supplemental words, that are use throughout
remove_words = ['Відео','Інфографіка', "Документ", "Фото", "Доповнено"]
header = ' '.join(i for i in header.split() if i not in remove_words)

time.sleep(timeout)

# acquiring a navigating to address of the chosen news header
link_address = driver.find_element_by_xpath("//div[@class='container_sub_news_list_wrapper mode1']/div[{}]/div[@class='article_content']/div[@class='article_header']/a".format(item_in_list)).get_attribute('href')
driver.get(link_address)

time.sleep(timeout)

# acquiring news header from another page, sometimes website
post_title = driver.find_element_by_xpath("//h1").text

# printing results
if str(post_title) == str(header):
    print("Success")
else:
    print("Failed")

time.sleep(timeout)
driver.quit()


