#Using Selenium, logs into your email account and sends an email of the string to the provided address. 

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#https://gmail.com
browser = webdriver.Firefox()
browser.get('https://gmail.com')

#Get email address 
emailElem = browser.find_element_by_css_selector('#identifierId')
useremail = input('Enter your email address:')

#Next button
emailElem.send_keys(useremail)
nextbutton = browser.find_element_by_css_selector('#identifierNext')
nextbutton.click()


browser.maximize_window() #For maximizing window
browser.implicitly_wait(90) #gives an implicit wait for 20 seconds

#Get password
password = input('Enter password:')

passwordElem = browser.find_element_by_css_selector('#password > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > input:nth-child(1)')
passwordElem.click()
passwordElem.send_keys(password)
nextbutton = browser.find_element_by_css_selector('#passwordNext')
nextbutton.click()

#Compose 
compose = browser.find_element_by_css_selector('.T-I-KE')
compose.click()

#Recipient email address
recipientemail = input('Enter recipient email address:')

recipient = browser.find_element_by_css_selector('#\:n8')
recipient.send_keys(recipientemail)

#Subject 
subjecttxt = input('Enter Subject:')

Subject = browser.find_element_by_css_selector('#\:mq')
Subject.send_keys(subjecttxt)

#Content
contxt = input('Enter content:')

content = browser.find_element_by_css_selector('#\:nv')
content.send_keys(contxt)

#Sent
send = browser.find_element_by_css_selector('#\:mg')
send.click()
print('Email has successfully sent to ', recipientemail)
