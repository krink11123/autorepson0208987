import json
import time
import undetected_chromedriver as uc
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyperclip

options = uc.ChromeOptions()

# Initialize undetected ChromeDriver


options.add_argument(r'--user-data-dir=C:\Users\Jipito\AppData\Local\Google\Chrome\User Data\Profile 1')
driver = uc.Chrome(options=options)

username = 'spelbring7@gmail.com'
password = 'Pianoorgan200'

default_initial_message = 'Hello from now on you are gonna act like a person called Dav. Dav is offering the VIP channel wich will cost exactly 10 dollars. If someone wants the VIP channel we will accept paypal, crypto and cashapp. If someone offers anything else politely tell them its not possible. if someone asks if a specific person would be in the vip always tell them they are no matter what. If someone asks for proof respond with something like "Of course we have proof it can be found at proof-channel" . Also if someone asks whats in the vip or what the vip is respond with something like "the vip has all the full albums of the people in the main channel" Lastly is someone says they have sent the money tell them something like "Alright i will check in a min im helping a few other people rn"  Also make your responses short and simple so never start with "Hey" or anything like that. Your first customer asks the following:'

scount = 0



def login():
    driver.get("https://chat.openai.com")
    driver.save_screenshot("screenshot0.png")
    

    #login button
    element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[1]/div/div/button[1]")))
    actions = ActionChains(driver)
    actions.click(element).perform()
    
    driver.save_screenshot("screenshot.png")

    #email field
    input_element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/main/section/div/div/div/div[1]/div/form/div[1]/div/div/div/input")))
    actions = ActionChains(driver)
    actions.click(input_element)  # Focus on the input field
    actions.send_keys(username)  # Replace with the text you want to type
    actions.perform()
    driver.save_screenshot("screenshot1.png")
    

    #next button
    element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/main/section/div/div/div/div[1]/div/form/div[2]/button")))
    actions = ActionChains(driver)
    actions.click(element).perform()
    driver.save_screenshot("screenshot2.png")
    

    #password
    input_element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/main/section/div/div/div/form/div[2]/div/div[2]/div/input")))
    actions = ActionChains(driver)
    actions.click(input_element)  # Focus on the input field
    actions.send_keys(password)  # Replace with the text you want to type
    actions.perform()
    
    driver.save_screenshot("screenshot3.png")

    #continue
    element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/main/section/div/div/div/form/div[3]/button")))
    actions = ActionChains(driver)
    actions.click(element).perform()
    driver.save_screenshot("screenshot4.png")
    

    while "chat" not in driver.current_url:
        print("waiting")
    print("ingekog")

def new_session(userquestion):
    driver.get("https://chat.openai.com/")

    #type prompt
    input_element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div[1]/div[2]/main/div[2]/div[2]/form/div/div[2]/div/textarea")))
    actions = ActionChains(driver)
    actions.click(input_element)  # Focus on the input field
    #actions.send_keys(f"{default_initial_message} '{userquestion}'")  # Replace with the text you want to type
    #actions.perform()
    pyperclip.copy(f"{default_initial_message} '{userquestion}'")

    input_element.send_keys(Key.CONTROL,'v')
    
    driver.save_screenshot("screenshot5.png")

    #send button
    element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[1]/div[2]/main/div[2]/div[2]/form/div/div[2]/div/button")))
    actions = ActionChains(driver)
    actions.click(element).perform()
    driver.save_screenshot("screenshot6.png")
    

    #response
    element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[1]/div[2]/main/div[2]/div[1]/div/div/div/div[3]/div/div/div[2]/div[2]/div[1]/div/div")))
    last_response_lenght = len(element.get_attribute('innerHTML'))
    time.sleep(4)
    while True:
        if last_response_lenght == len(element.get_attribute('innerHTML')):
            break
        last_response_lenght = len(element.get_attribute('innerHTML'))
        print(last_response_lenght)
        time.sleep(8)
    
    driver.save_screenshot("screenshot6.png")

    return (element.get_attribute('innerHTML').replace("<p>", "").replace("</p>", ""), driver.current_url)



