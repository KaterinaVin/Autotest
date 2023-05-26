from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

s=Service('C:\chromedriver_win32\chromedriver.exe')
driver = webdriver.Chrome(service=s)

driver.get("https://qahacking.guru/")
driver.set_window_size(1936, 1048)
driver.find_element(By.CSS_SELECTOR, ".uk-navbar-nav > li:nth-child(1) > a").click()
driver.find_element(By.CSS_SELECTOR, ".uk-navbar-nav > li:nth-child(2) > a").click()
driver.execute_script("window.scrollBy(0,2200)", "")
time.sleep(1)
driver.find_element(By.ID, "mod-rscontact-full-name-91").send_keys("Katerina")
time.sleep(1)
driver.find_element(By.ID, "mod-rscontact-email-91").send_keys("k@mail.ru")
driver.find_element(By.ID, "mod-rscontact-mobile-phone-91").send_keys("8-999-99-99-99")
time.sleep(1)
driver.find_element(By.ID, "mod-rscontact-subject-91").send_keys("Хочу собачку")
driver.find_element(By.ID, "mod-rscontact-submit-btn-91").click()
time.sleep(3)