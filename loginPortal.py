from selenium import webdriver
import requests
from requests import Session
from requests.cookies import cookiejar_from_dict
from bs4 import BeautifulSoup
import time

URL_SITE = 'https://my.fullerton.edu/Portal/Dashboard/'

if __name__ == "__main__":
    #asks for username and password to use for credentials
    userName_ = str(input("Enter your username: "))
    password_ = str(input("Enter your password: "))
    op = webdriver.ChromeOptions()  #this makes the browser not open so you can get the cookies without having to go in
    op.add_argument('headless')
    driver = webdriver.Chrome(options=op)
    driver.get(URL_SITE)
    #goes through the login page
    driver.find_element_by_xpath('//*[@id="username"]').send_keys(userName_)  
    driver.find_element_by_xpath('//*[@id="password"]').send_keys(password_)
    driver.find_element_by_xpath('//*[@id="Form1"]/div[6]/button').click()
    cookie_jar = driver.get_cookies()
    
    cookies_dict = {} #adds cookies into the cookie jar for the requests use
    for cookie in cookie_jar:
        cookies_dict[cookie['name']] = cookie['value']

    driver.close()

    #sets the cookies to use for the session to get access
    session = requests.Session()
    cookie_jarSess = requests.cookies.RequestsCookieJar()
    for cookie in cookies_dict:
        cookie_jarSess.set(cookie, cookies_dict[cookie])
    session.cookies = cookie_jarSess
    r = session.get(URL_SITE)
    soup = BeautifulSoup(r.content, 'lxml')
    print(soup.prettify())