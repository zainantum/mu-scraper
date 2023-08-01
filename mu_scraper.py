# Import Modules

from selenium import webdriver
# import undetected_chromedriver as uc
from webdriver_manager.chrome import ChromeDriverManager
import requests
import os
import sys
import time
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, WebDriverException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from eth_account import Account
import secrets

with open('ip.txt') as f:
    datafile = f.readlines()

found = False
listEth = open("privatekey.txt", "a")


def check(ip):
    global found
    for line in datafile:
        if ip in line:
            found = True


def run(propro):
    # chrome_options = uc.ChromeOptions()
    chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument('--proxy-server=socks5://52.157.88.150:80')
    # chrome_options.add_argument(f'-- proxy-server={propro}')
    # driver = uc.Chrome(use_subprocess=True, chrome_options=chrome_options)
    # chrome_options.add_argument('headless')
    #chrome_options.add_argument('--no-sandbox')
    #chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument("window-size=1280,800")
    #chrome_options.add_argument('--disable-blink-features=AutomationControlled')
    # driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver", options=chrome_options)
    driver2 = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=chrome_options)
    driver2.delete_all_cookies()
    driver2.get("https://wallet.kukai.app/")
    driver2.find_element(By.XPATH, "/html/body/app-root/app-agreement/div/div/div/div/div[1]/button").click()
    driver2.find_element(By.XPATH, "/html/body/app-root/app-header/div[1]/div/div/span[2]").click()
    driver2.find_element(By.XPATH, "/html/body/app-root/app-new-wallet/form/div/div/div/div/span").click()
    info = driver2.find_element(By.XPATH, "/html/body/app-root/app-new-wallet/form/div/div/div").text
    print(info)
    driver2.find_element(By.XPATH, "/html/body/app-root/app-new-wallet/form/div/div/button").click()
    for i in range(5):
        word1 = driver2.find_element(By.XPATH, "/html/body/app-root/app-new-wallet/form/div/div/div/div[2]/span").text
        print(word1)
        word1 = word1.split(" ")
        print(word1[1])
        phrase = info.split(" ")
        # print(word1[1]-1)
        pw = driver2.find_element(By.XPATH, "//*[@id='wordInput']")
        pw.send_keys(phrase[int(word1[1])-1])
        time.sleep(1)
    driver2.find_element(By.XPATH, "/html/body/app-root/app-new-wallet/form/div/div/button").click()
    pw = driver2.find_element(By.XPATH, "/html/body/app-root/app-new-wallet/form/div/div/input[1]")
    pw.send_keys("kopisaja")
    pw1 = driver2.find_element(By.XPATH, "/html/body/app-root/app-new-wallet/form/div/div/input[2]")
    pw1.send_keys("kopisaja")
    driver2.find_element(By.XPATH, "/html/body/app-root/app-new-wallet/form/div/div/button").click()
    time.sleep(20)
    driver2.find_element(By.XPATH, "/html/body/app-root/app-new-wallet/form/div/div/button[1]").click()
    time.sleep(2)
    driver2.find_element(By.XPATH, "/html/body/app-root/app-new-wallet/form/div/div/button[2]").click()
    time.sleep(5)
    driver2.get("https://collectibles.manutd.com/")
    time.sleep(5)
    driver2.find_element(By.XPATH, "//*[@id='__next']/div/div[2]/div/div/div[2]/button[1]").click()
    driver2.find_element(By.XPATH, "//*[@id='__next']/div/div[2]/div[2]/div/div[2]/div/button").click()
    # driver2.find_element(By.XPATH, "//*[@id='chakra-modal--body-:R4td9f6:']/div/div/p[3]/a").click()
    WebDriverWait(driver2, 120).until(
        EC.presence_of_element_located((By.XPATH,
                                        "//*[@id='chakra-modal--body-:R4td9f6:']/div/div/p[3]/a"))
    ).click()
    time.sleep(10)
    driver2.execute_script('''return document.querySelector('div[id^="beacon-alert-wrapper"]').shadowRoot.querySelector('a[id="wallet_kukai_web"]')''').click()

    # driver2.find_element(By.XPATH, "//*[@id='wallet_kukai_web']").click()
    # WebDriverWait(driver2, 120).until(
    #     EC.presence_of_element_located((By.XPATH,
    #                                     "//*[@id='wallet_kukai_web']"))
    # ).click()
    time.sleep(10)
    # time.sleep(20)
    driver2.switch_to.window(driver2.window_handles[1])
    # time.sleep(40)
    WebDriverWait(driver2, 120).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/app-root/app-logged-in/app-uri-handler/app-permission-request/div/div/div[3]/div[2]/button"))
    ).click()
    # driver2.find_element(By.XPATH, "/html/body/app-root/app-logged-in/app-uri-handler/app-permission-request/div/div/div[3]/div[2]/button").click()
    time.sleep(5)
    driver2.switch_to.window(driver2.window_handles[0])
    time.sleep(3)
    pw11 = driver2.find_element(By.XPATH, "//*[@id='email']")
    pw11.send_keys(propro)
    driver2.find_element(By.XPATH, "//*[@id='chakra-modal--body-:R4td9f6:']/div/form/div[3]/div[1]/label/span[1]").click()
    driver2.find_element(By.XPATH,
                         "//*[@id='chakra-modal--body-:R4td9f6:']/div/form/div[3]/div[2]/label/span[1]").click()
    driver2.find_element(By.XPATH,
                         "//*[@id='chakra-modal--body-:R4td9f6:']/div/form/div[5]/div/div/label[2]/span[1]").click()
    time.sleep(5)
    print("register")
    driver2.find_element(By.XPATH, "//*[@id='chakra-modal--body-:R4td9f6:']/div/div/button").click()
    time.sleep(60)
    ina = WebDriverWait(driver2, 120).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='tabs-:rh:--tabpanel-1']/div/div/div/h2"))
    ).text
    if("rare" in ina):
        print("ini rare")


file_object = open('ip.txt', 'a')


def mulai():
    with open('ip.txt') as f:
        for line in f:
            print(line)
            run(line)


mulai()
file_object.close()
listEth.close()
