from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
import getpass

driver = webdriver.Firefox()
driver.set_window_position(0, 500)

driver.get('https://accounts.google.com/signin/v2/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin')
#driver.get('https://login.yahoo.com/config/login?.src=fpctx&.intl=in&.lang=en-IN&.done=https%3A%2F%2Fin.yahoo.com')
email_form = driver.find_element_by_xpath('//*[@id="identifierId"]')
email = input('Enter email ')
email_form.send_keys(str(email))
next_button_1 = driver.find_element_by_xpath('//*[@id="identifierNext"]/content/span')
next_button_1.click()
password = getpass.getpass('Enter password ')
password_form = driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
password_form.send_keys(str(password))
next_button_2 = driver.find_element_by_xpath('//*[@id="passwordNext"]/content/span')
next_button_2.click()
driver.implicitly_wait(10)

try: 
	driver.find_element_by_xpath('//*[@id="idvPin"]')
	veri_code_form = driver.find_element_by_xpath('//*[@id="idvPin"]')
	veri_code = input('Enter verification code ')
	veri_code_form.send_keys(str(veri_code))
	rem_comp_field = driver.find_element_by_css_selector('#view_container > div > div > div.pwWryf.bxPAYd > div > div.WEQkZc > div > form > content > section > div > content > div.T8qVIf > div.uVccjd.iK47pf.N2RpBe')
	rem_comp_field_value = rem_comp_field.get_attribute('aria-checked')
	print(rem_comp_field_value)
	print(type(rem_comp_field_value))
	rem_comp = input('Do you want gmail to remember this computer? Enter 0 for No ')
	
	if int(rem_comp) == 0 and rem_comp_field_value == 'true' :
		rem_comp_button = driver.find_element_by_xpath('//*[@id="view_container"]/div/div/div[2]/div/div[1]/div/form/content/section/div/content/div[3]/div[1]/div[3]')
		rem_comp_button.click()
		print('lol')
	else:
		print('no')
	driver.implicitly_wait(10)
	next_button_3 = driver.find_element_by_xpath('//*[@id="idvPreregisteredPhoneNext"]/content/span')
	next_button_3.click()
except:
	pass

time.sleep(10)

try:
	spam_button_1 = driver.find_element_by_xpath('/html/body/div[7]/div[3]/div/div[2]/div[1]/div[1]/div[1]/div[2]/div/div/div/div[2]/div/div/div[1]/div[1]/div/div[9]/div/div/div[2]/span/a')
	spam_button_1.click()

except:
	more_button = driver.find_element_by_xpath('/html/body/div[7]/div[3]/div/div[2]/div[1]/div[1]/div[1]/div[2]/div/div/div/div[2]/div/div/div[2]/span/span[1]')
	more_button.click()
	spam_button = driver.find_element_by_xpath('/html/body/div[7]/div[3]/div/div[2]/div[1]/div[1]/div[1]/div[2]/div/div/div/div[2]/div/div/div[3]/div/div[1]/div/div[4]/div/div/div[2]/span/a')
	spam_button.click()


i=1
while(1):
	try:
		x_path = str('/html/body/div[7]/div[3]/div/div[2]/div[1]/div[2]/div/div/div/div/div[2]/div/div[1]/div/div[2]/div[3]/div[1]/div/table/tbody/tr['+ str(i) + ']/td[5]')

		table = driver.find_element_by_xpath(str(x_path))
		table.click()

		list_of_links = ['unsubscribe','Unsubscribe','clickhere','preferences']

		count = 0

		for link in list_of_links:

			try:
				unsub_button = driver.find_element_by_partial_link_text(str(link))
				unsub_link = unsub_button.get_attribute('href')
				print(unsub_link)
				conductor = webdriver.Firefox()
				conductor.get(str(unsub_link))

				conductor.implicitly_wait(5)

				'''actions = ActionChains(conductor) 
				actions.send_keys(Keys.TAB)
				actions.perform()
				actions.send_keys(Keys.TAB)
				actions.perform()
				actions.send_keys(Keys.SPACE)
				actions.perform()

				try:
					email_unsub = conductor.find_element_by_id('EMAIL')
					email_unsub = send_keys(str(email))
				except:
					pass'''

				time.sleep(2)

				list = ['.btn','#button1']

				for j in list:
					point = 0
					print(j)
					try:
						final_button = conductor.find_element_by_css_selector(str(j))
						final_button.click()
						print('Done')
						point = 1 
					except:
						pass
					if(point == 1):
						break

				conductor.implicitly_wait(5)
				time.sleep(2)
				conductor.close()

				count += 1



			except:
				pass

			if count == 1:
				break
		

		time.sleep(2)

		back_button = driver.find_element_by_xpath('/html/body/div[7]/div[3]/div/div[2]/div[1]/div[2]/div/div/div/div/div[1]/div[3]/div[1]/div/div[1]/div/div')
		back_button.click()
		print(i)
		i += 1
	except:
		break






