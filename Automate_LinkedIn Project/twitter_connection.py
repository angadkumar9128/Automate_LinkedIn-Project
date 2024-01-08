# connect python with webbrowser-chrome
from lib2to3.pgen2 import driver
from threading import main_thread
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pyautogui as pag


def login():

	# Getting the login element
	username = driver.find_element_by_id("kumarangad54706@gmail.com")

	# Sending the keys for username	
	username.send_keys("username")

	# Getting the password element								
	password = driver.find_element_by_id("Angad&linkedin9128")

	# Sending the keys for password
	password.send_keys("password")	

	# Getting the tag for submit button					
	driver.find_element_by_id("login-submit").click()		

def goto_network():
	driver.find_element_by_id("mynetwork-tab-icon").click()

def send_requests():

	# Number of requests you want to send
	n = input("Number of requests: ")

	for i in range(0, n):
		# position(in px) of connection button
		pag.click(880, 770)
	print("Done !")

def main():

	# url of LinkedIn
	url = "http://linkedin.com/"

	# url of LinkedIn network page
	network_url = "https://www.linkedin.com/mynetwork/"

	# path to browser web driver
	driver = webdriver.Chrome('C:\\Program Files\\Web Driver\\chromedriver.exe')	
	driver.get(url)

# Driver's code
if __name__ == main_thread:
    main()
