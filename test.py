from selenium import webdriver
from selenium.webdriver.common.by import By
from PIL import Image,ImageEnhance
import pytesseract
import code_img
options = webdriver.EdgeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Edge(options=options)
driver.get("https://netinfo.takming.edu.tw/tip/index_new.htm")
key = driver.find_element('name' ,"key_id")
key.send_keys('D11119132')
pwd = driver.find_element(By.NAME,"key_pwd")
pwd.send_keys("eddy5889")
driver.save_screenshot("test.jpg")
jpg = driver.find_element(By.ID,"cap")
left = jpg.location['x']-5
right = jpg.location['x']+jpg.size['width']+5
top = jpg.location['y']-5
bottom = jpg.location['y']+jpg.size['height']+5
img = Image.open("test.jpg")
imgs=img.crop((left,top,right,bottom))
img_i = imgs.convert("RGB")
img_i.save('te.jpg')
code = driver.find_element(By.NAME,"cap")
code_code= code_img.code_pa()
code.send_keys(code_code)
