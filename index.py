from faker import Faker
import random
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, WebDriverException, TimeoutException, NoSuchWindowException
from tempfile import mkdtemp
from threading import Thread
from selenium.webdriver.support.ui import Select


language_list = ['sk']
chrome_driver_loc = r"C:/chromedriver.exe"
target_web = r"https://cool.promosuper.live/cc/sk/createaccount/"


def open_browser():
    fake_user_agent = Faker()
    options = webdriver.ChromeOptions()
    # options.binary_location = '/opt/chrome/chrome'
    options.add_experimental_option("excludeSwitches", ['enable-automation', 'enable-logging'])
    options.add_argument('--disable-infobars')
    options.add_argument('--disable-features=ChromeWhatsNewUI')
    options.add_argument('--disable-extensions')
    options.add_argument('--no-first-run')
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--disable-client-side-phishing-detection')
    options.add_argument('--allow-running-insecure-content')
    options.add_argument('--disable-web-security')
    options.add_argument('--lang=' + random.choice(language_list))
    options.add_argument('--user-agent=' + fake_user_agent.user_agent())
    # options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    # options.add_argument("--disable-gpu")
    options.add_argument("--window-size=800x900")
    #options.add_argument("--single-process")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-dev-tools")
    options.add_argument("--no-zygote")
    options.add_argument("-silent")
    options.add_argument(f"--user-data-dir={mkdtemp()}")
    options.add_argument(f"--data-path={mkdtemp()}")
    options.add_argument(f"--disk-cache-dir={mkdtemp()}")
    # options.add_argument("--remote-debugging-port=9222")
    chrome = webdriver.Chrome(chrome_driver_loc, options=options)
    chrome.set_window_size(800, 900)
    return chrome


def terrorize():

    fake = Faker()
    browser = open_browser()
    while True:
        try:
            browser.delete_all_cookies()
            browser.set_page_load_timeout(60)

            browser.get(target_web)

            date = fake.credit_card_expire()
            mon = date.split('/')[0]
            rok = date.split('/')[1]


            target_XPATH = '//*[@id="firstName"]'
            target = WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.XPATH, target_XPATH)))
            target.clear()
            target.send_keys(fake.first_name())

            target_XPATH = '//*[@id="lastName"]'
            target = WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.XPATH, target_XPATH)))
            target.clear()
            target.send_keys(fake.last_name())

            target_XPATH = '//*[@id="address1"]'
            target = WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.XPATH, target_XPATH)))
            target.clear()
            target.send_keys(fake.street_address())

            target_XPATH = '//*[@id="postalCode"]'
            target = WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.XPATH, target_XPATH)))
            target.clear()
            target.send_keys(fake.postcode())

            target_XPATH = '//*[@id="city"]'
            target = WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.XPATH, target_XPATH)))
            target.send_keys(fake.city())

            target_XPATH = '//*[@id="phone"]'
            target = WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.XPATH, target_XPATH)))
            target.clear()
            target.send_keys(fake.msisdn())

            target_XPATH = '//*[@id="email"]'
            target = WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.XPATH, target_XPATH)))
            target.clear()
            target.send_keys(fake.email())

            target_XPATH = '//*[@id="kformSubmit"]'
            target = WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.XPATH, target_XPATH)))
            target.click()

            target_XPATH = '//*[@id="cardNumber"]'
            target = WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.XPATH, target_XPATH)))
            target.send_keys(fake.credit_card_number())

            target_XPATH = '//*[@id="scroll-form"]/div[2]/div[1]/select'
            target = Select(WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.XPATH, target_XPATH))))
            target.select_by_value(mon)

            target_XPATH = '//*[@id="scroll-form"]/div[2]/div[2]/select'
            target = Select(WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.XPATH, target_XPATH))))
            target.select_by_value("20" + rok)

            target_XPATH = '//*[@id="scroll-form"]/div[2]/div[3]/input'
            target = WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.XPATH, target_XPATH)))
            target.send_keys(fake.credit_card_security_code())

            target_XPATH = '//*[@id="kformSubmit"]'
            target = WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.XPATH, target_XPATH)))
            target.click()

            sleep(3)

        except TimeoutException:
            continue

if __name__ == '__main__':
    Thread(name='trash_traffic', target=terrorize).start()
    Thread(name='trash_traffic_1', target=terrorize).start()
    Thread(name='trash_traffic_ninja2', target=terrorize).start()
    Thread(name='trash_traffic_ninja3', target=terrorize).start()
    Thread(name='trash_traffic_ninja4', target=terrorize).start()
    Thread(name='trash_traffic_ninja5', target=terrorize).start()
    Thread(name='trash_traffic_ninja6', target=terrorize).start()
    Thread(name='trash_traffic_ninja7', target=terrorize).start()
