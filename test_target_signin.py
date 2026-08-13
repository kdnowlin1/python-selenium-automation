from tkinter import Text

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.target.com/")
sleep(2)

driver.find_element(By.ID, "account-sign-in").click()
sleep(2)

driver.find_element(By.CSS_SELECTOR, "[data-test='accountNav-signIn']").click()
sleep(2)

sign_in_text = driver.find_element(By.XPATH, "//*[contains(text(),'Sign in or create account')]")
sign_in_button = driver.find_element(By.ID, "login")
print("Sign in page verified")

driver.quit()
