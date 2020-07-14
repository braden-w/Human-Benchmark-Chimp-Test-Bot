from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
driver.get("https://humanbenchmark.com/tests/chimp")
# box = driver.find_element_by_xpath("/html/body/div/div/div[4]/div[1]")
# box.click()

try:
    while True:
        newboxes = {
            element.text: element
            for element in driver.find_elements_by_class_name("css-19b5rdt")
        }
        for counter in range(1, len(newboxes) + 1):
            newboxes[str(counter)].click()
        try:
            driver.find_element_by_xpath("/html/body/div/div/div[4]/div[1]/div/div[1]/div[3]/button").click()
        except:
            continue

finally:
    driver.quit
