import os

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import logging

logger = logging.getLogger('simple_example')

logger.setLevel(logging.INFO)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)

browser = webdriver.Firefox(service=Service(f"{os.path.abspath(os.getcwd())}/geckodriver"))

logger.info('Przechodzę na stronę Zalando')

browser.get('https://www.zalando.pl/')

facebook = browser.find_element(By.XPATH, "//a[@aria-label='Facebook']")
instagram = browser.find_element(By.XPATH, "//a[@aria-label='Instagram']")

logger.info('Pobieram link do facebooka i instagrama')

facebook.get_attribute("href") == "https://www.facebook.com/zalando.polska"
instagram.get_attribute("href") == "https://www.instagram.com/zalando/"

logger.info('poprawnie znalezione linki do facebooka i instagrama')

browser.close()
