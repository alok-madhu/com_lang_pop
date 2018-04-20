from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sqlite3
import pandas as pd
from _collections import OrderedDict


def fetch_data_from_url(driver, url):
    driver.get(url)
    data_set = {}
    driver.find_element_by_class_name('table-top20')
    table = driver.find_element_by_class_name('table-top20')
    rows = table.find_elements_by_tag_name('tr')
    for row in rows:
        data_set.add(row.text)
    return data_set


def save_to_database(data_dict):
    pass


if __name__ == "__main__":
    driver = webdriver.Chrome()
    data_from_url = fetch_data_from_url(driver, "https://www.tiobe.com/tiobe-index/")
    print(data_from_url)

    # save_to_database(data_dict)
    driver.quit()
