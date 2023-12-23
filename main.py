from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By

response = requests.get("https://appbrewery.github.io/Zillow-Clone/")

zillow_web_page = response.text
soup = BeautifulSoup(zillow_web_page, "html.parser")
links = [link.get("href") for link in soup.find_all(name="a", class_ ="StyledPropertyCardDataArea-anchor" )]
prices = [price.get_text().replace("/","+").split("+")[0] for price in soup.find_all(name="span", class_ = "PropertyCardWrapper__StyledPriceLine")]
addresses = [address.get_text().strip().replace("|","").replace("#","") for address in soup.find_all(name="address" ) ]

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://docs.google.com/forms/d/e/1FAIpQLSdGFJARzPkboDbWsP8AGod6eiMhJyDzKI7B9psz7gCN-EAeoQ/viewform?usp=sf_link")


for i in range(len(addresses)):
    inputs = [input for input in driver.find_elements(By.CSS_SELECTOR, value=".o3Dpx input")]
    inputs[0].send_keys(addresses[i])
    inputs[1].send_keys(prices[i])
    inputs[2].send_keys(links[i])

    send_button = driver.find_element(By.CSS_SELECTOR, value=".lRwqcd div")
    send_button.click()

    send_another_answer_button = driver.find_element(By.LINK_TEXT, value= driver.find_element(By.CSS_SELECTOR, value=".c2gzEf a").text)
    send_another_answer_button.click()
