import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def main():
    driver = webdriver.Chrome('chromedriver.exe')
    driver.get("http://127.0.0.1:5000/")
    search_field = driver.find_element_by_id("search")
    search_field.clear()
    search_field.send_keys('Interstellar')
    search_field.send_keys(Keys.RETURN)

    # print(driver.page_source)

    search_results = WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.ID, "result")))

    results = search_results.find_elements_by_name("movie-box")

    for result in results:
        print(result.text)

    driver.close()




if __name__ == '__main__':
    main()
