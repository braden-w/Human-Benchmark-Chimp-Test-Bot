from selenium import webdriver

driver = webdriver.Firefox()
driver.get("https://humanbenchmark.com/tests/chimp")

try:
    while True:
        # Create dictionary of <box number>:<box location> before they dissappear
        newboxes = {
            element.text: element
            for element in driver.find_elements_by_class_name("css-19b5rdt")
        }
        # Use box number key in dictionary as lookup from 1 to n
        for counter in range(1, len(newboxes) + 1):
            newboxes[str(counter)].click()
        # try:
        #     driver.find_element_by_class_name("css-qm0ri0").click()
        # except:
        #     continue

finally:
    driver.quit
