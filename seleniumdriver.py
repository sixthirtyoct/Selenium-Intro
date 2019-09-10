#pip install selenium
#pip install webdriver_manager

import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

#Initialising Browser
browser=webdriver.Chrome(ChromeDriverManager().install())

browser.maximize_window()

start=time.time()

#Opening Website
browser.get("https://www.youtube.com")
time.sleep(1)
browser.find_element_by_id("search").send_keys("Roman Reigns Theme")
browser.find_element_by_id("search-icon-legacy").click()
time.sleep(1.5)
browser.find_element_by_id("video-title").click()

browser.close()
browser.quit()

end=time.time()
print("Automated!, Time taken:",end-start,"seconds")
