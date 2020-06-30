import requests
import json
from bs4 import BeautifulSoup
from config import userName  #this and password come from another py file i made to hold my info
from config import passWord


URL_LINK = 'https://my.fullerton.edu/'

payload = {
    'j_username' : userName,
    'j_password' : passWord,
    '_eventId_proceed' : ''
}

parexe = {
    'execution' : 'e2s1'
}

s = requests.Session()

response = s.get(URL_LINK)

JSESSION = response.url[75:107]

cooki = {
    'JSESSIONID' : JSESSION
}
response2 = s.get(URL_LINK)

login_post = s.post("https://shibboleth.fullerton.edu/idp/profile/SAML2/Redirect/SSO?execution=e2s1", data=payload, cookies = cooki)

soup = BeautifulSoup(login_post.content, 'lxml')
#print(soup.prettify())
inputRelay = soup.find(attrs={"name":"RelayState"})
outputRelay = inputRelay['value']
inputSAML = soup.find(attrs={"name":"SAMLResponse"})
outputSAML = inputSAML['value']

data_2 = {
    'RelayState': inputRelay['value'],
    'SAMLResponse': inputSAML['value'],
}

data_3 = {
    'SAMLResponse': inputSAML['value']
}

finalPost = s.post("https://my.fullerton.edu/Shibboleth.sso/SAML2/POST", data=data_2)

canvas = s.post("https://csufullerton.instructure.com/login/saml", data=data_3)
print(canvas.text)
'''
print ("relay -----> " + str(outputRelay))
print("------------------------------------")
print("------------------------------------")
print("------------------------------------")
print("------------------------------------")
print("------------------------------------")
print("------------------------------------")
print("------------------------------------")
print ("saml ----->"  + str(outputSAML)) '''