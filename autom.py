import re
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.common.exceptions import NoSuchElementException

cover= '''
Dear Sir/Madam,
I am writing this letter to you to apply for the position of Web developer in your company. I came across the position and wanted to apply for the same.With my various projects in the field, I have learned valuable skills that appear relevant to the position desired by your company. As you can see in my resume, I have the qualifications and i also possess the experience in ui designing and building personal projects with react, jquery, javascript, html, bootstrap and css. Furthermore I'm dedicated to my craft, possess a strong work ethic and am always willing to learn for what I lack. Thank you for your time and for considering me as a candidate. I have mentioned my contacts in my resume.

Yours Truly
your name 
'''
driver=webdriver.Chrome()
driver.maximize_window()
driver.get('https://internshala.com/student/dashboard')

#login
mail=driver.find_element(By.ID, value='email')
mail.send_keys("your@gmail.com")
driver.find_element(By.ID,value="password").send_keys("your pass")
driver.find_element(By.ID,value="login_submit").click()
time.sleep(5)

driver.get('https://internshala.com/internships/work-from-home-react-internships/stipend-2000')
time.sleep(3)
but_details=driver.find_elements(By.LINK_TEXT,'View details')
for button in but_details:
    try:
        driver.switch_to.window(driver.window_handles[0])
        button.click()
        time.sleep(2)
        driver.switch_to.window(driver.window_handles[1])
        time.sleep(2)
        but_apply=driver.find_element(By.LINK_TEXT,'Apply now')
        but_apply.click()
        time.sleep(3)
        but_proceed=driver.find_element(By.XPATH,'//*[@id="layout_table"]/div[4]/button')
        but_proceed.click()
        time.sleep(2)
        cover_letter_field = driver.find_element(By.XPATH, "/html/body/div[1]/div[19]/div/div/div[2]/div[2]/form/div/div[2]/div[1]/div[4]/div/div[1]")
        actions = ActionChains(driver)
        actions.move_to_element(cover_letter_field).perform()
        cover_letter_field.send_keys(cover)
        driver.find_element(By.ID,value='submit').click()
        time.sleep(2)
    except Exception as e:
        print("Exception occurred:", str(e))
        continue
time.sleep(5)

driver.quit()