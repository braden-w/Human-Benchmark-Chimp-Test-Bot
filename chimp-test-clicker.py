from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
driver.get("https://humanbenchmark.com/tests/chimp")
box = driver.find_element_by_xpath("/html/body/div/div/div[4]/div[1]")
# box.click()

try:
    while True:
        newbox = WebDriverWait(driver, 300, poll_frequency=0.001).until(
            EC.presence_of_element_located((By.CLASS_NAME, "css-19b5rdt"))
        )
        newboxes = driver.find_elements_by_class_name("css-19b5rdt")
        entries = {}
        for element in newboxes:
            entries[element.text] = element
        counter = 1
        while counter < len(newboxes):
            for element in newboxes:
                if int(element.text) == counter:
                    element.click()
                    counter += 1
                
finally:
    driver.quit()
