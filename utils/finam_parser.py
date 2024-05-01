import time

import undetected_chromedriver as uc
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def create_undetected_chrome_driver():
    """
    Create undetected chrome driver
    :return: driver object
    """

    options = uc.ChromeOptions()

    # options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument("--disable-gpu")

    driver = uc.Chrome(options=options, use_subprocess=True)
    driver.set_page_load_timeout(35)
    return driver


def get_top_finam_gainers_losers():
    """
    Get top gainers and losers from finam.ru
    :return: list of top gainers and losers
    """

    driver = create_undetected_chrome_driver()
    url = 'https://www.finam.ru'
    top_class = 'HomeDesktop__borderLeft--2AH'

    driver.get(url)
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, top_class)))

    soup = BeautifulSoup(driver.page_source, 'html.parser')

    top_gainers = []
    top_losers = []

    div_top = soup.find('div', class_=top_class).find('div', class_='Item__container--2AY')
    elements_top = div_top.find_all('table', class_='Item__container--24M')

    for key_element, tag_element in enumerate(elements_top):
        cells_element = tag_element.find_all('td')
        ticker = cells_element[0].text
        change_percentage = cells_element[2].text

        ticker_info = {
            'ticker': ticker,
            'change_percentage': change_percentage,
        }

        if key_element % 2 == 0:
            top_gainers.append(ticker_info)
        else:
            top_losers.append(ticker_info)

    driver.close()
    time.sleep(1)

    return top_gainers, top_losers
