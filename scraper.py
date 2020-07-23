from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent

date = "?date=2020-06-23%202020-07-23"

options = Options()
ua = UserAgent()
userAgent = ua.random
options.add_argument(f'user-agent={userAgent}')
options.add_experimental_option("prefs", {
  "download.default_directory": r"C:\Users\Giovanni\Desktop",
  "download.prompt_for_download": False,
  "download.directory_upgrade": True,
  "safebrowsing.enabled": True
})

driver = webdriver.Chrome(chrome_options=options, executable_path="C:/Users/Giovanni/Desktop/chromedriver_win32/chromedriver")
driver.get("https://trends.google.it/trends/?geo=IT")

searchbar = driver.find_element_by_id("input-254")
searchbar.send_keys("Lamezia Terme")
searchbar.send_keys(Keys.ENTER)

actualurl = driver.current_url
splittedurl = actualurl.split("?")
splittedquery = splittedurl[1].split("&")

newurl = splittedurl[0] + date + "&" + splittedquery[1] + "&" + splittedquery[0]
driver.get(newurl)

exportbutton = driver.find_element_by_class_name("widget-actions-item.export")
exportbutton.click()

#driver.close()