#-*-coding:utf-8-*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from shutil import copyfile,move
from bs4 import BeautifulSoup
import time
import os
import shaonutil
import wget
import pickle
import selenium.webdriver 
import timeit
import winsound

Xpath_ = 'add your xpath here'
beep_frequency = 2500  # Set beep_frequency To 2500 Hertz
beep_duration = 1000  # Set beep_duration To 1000 ms == 1 second


start_time = time.time()


chrome_driver_path = "resources/drivers/chromedriver.exe"
browser = webdriver.Chrome(chrome_driver_path)
browser.set_window_size(700, 600)

# Move the window to position x/y
browser.set_window_position(0, 0)

browser.get("place your url here")

cookies = pickle.load(open("cookies.pkl", "rb"))
for cookie in cookies:
    browser.add_cookie(cookie)

browser.get("Place your url here")

#input("press to continue and ready save cookie")

#pickle.dump( browser.get_cookies() , open("cookies.pkl","wb"))


print("Need "+str(500*20))

n = 1
while n<501:
	print("page ="+str(n))
	
	try:
		browser.get('place your url here='+str(n))
		
		try:
			wait = WebDriverWait(browser, 15)
			wait.until(EC.visibility_of_element_located((By.XPATH, Xpath_)))
			images = browser.find_elements_by_xpath(Xpath_)
		except:
			raise ValueError("")

		if len(images) != 20:
			print("images found "+str(len(images)))
			raise ValueError("")

		for image in images:
			url = image.get_attribute("src").split('?',1)[0]
			filename = url.split('/')[-3] + '.' + url.split('.')[-1]
			try:
				wget.download(url,'downloads/'+filename)
			except:
				os.remove('downloads/'+filename)
				raise ValueError("")
		
		f = open("run.log", "a")
		f.writelines([str(n)+"\n"])
		f.close()
		n+=1
	except:
		print("class not found")
		winsound.Beep(beep_frequency, beep_duration)

print("--- %s seconds ---" % (time.time() - start_time))