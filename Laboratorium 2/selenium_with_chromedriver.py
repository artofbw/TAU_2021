import os
import time

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

browser = webdriver.Chrome(service=Service(f"{os.path.abspath(os.getcwd())}/chromedriver"))

logger.info('Przechodzę na stronę Zalando')

browser.get('https://www.zalando.pl/')

temp = browser.find_element(By.CLASS_NAME, 'z-navicat-header_navToolItemLink')
temp.click()
logger.info('Przechodzę na stronę logowania')

time.sleep(2)

logger.info('Uzupełniam dane logowania')

login = browser.find_element(By.XPATH, "//input[@id='login.email']")
login.send_keys('login')

login_button = browser.find_element(By.XPATH, "//button[@data-testid='login_button']")
login_button.click()

time.sleep(2)

logger.info('Pobieram błędy walidacji')
login_validation = browser.find_element(By.XPATH, "//span[contains(.,'Podaj pełny adres e-mail (np. jan.kowalski@domena.pl).')]")
password_validation = browser.find_element(By.XPATH, "//span[contains(.,'Pole obowiązkowe')]")

assert login_validation.text == "Podaj pełny adres e-mail (np. jan.kowalski@domena.pl)."
assert password_validation.text == "Pole obowiązkowe"

logger.info('poprawnie znalezione walidacje dla błędnego loginu i hasło')

browser.close()
