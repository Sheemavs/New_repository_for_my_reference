from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.common.by import By

service_obj=Service()
driver=webdriver.Firefox(service=service_obj)
driver.get("http://yens1.fyre.ibm.com:56080/FTM/nosession.jsp?language=en-US")

driver.find_element(By.XPATH, "//a[@href='./']").click()

driver.find_element(By.ID, "username").send_keys("Admin")
driver.find_element(By.XPATH, "//input[@id='security_check_button']").click()
driver.find_element(By.XPATH, "//span[@id='okBtn_label']").click()
driver.find_element(By.ID,"controlContainer_tablist_menuPane").click()
driver.find_element(By.ID, "dijit__TreeNode_3_label").click()
driver.find_element(By.ID, "dijit__TreeNode_9_label").click()
#driver.find_element(By.XPATH, "//input[@id='NAME']").send_keys("Request From Channel2")
#driver.find_element(By.CSS_SELECTOR, "div[id='b_search']").click()
driver.find_element(By.XPATH, "//td[@text()='Request From Channel2']").click()
print("success")