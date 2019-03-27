from selenium import webdriver

path=r'D:\Chromedriver\chromedriver.exe'
driver=webdriver.Chrome(executable_path=path)
driver.get('https://www.bilibili.com/')
