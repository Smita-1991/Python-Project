import bs4, requests

# res = requests.get('https://automatetheboringstuff.com/files/rj.txt')

# print(type(res))

# print(res.text)

# print(len(res.text[:500]))

# if(res.status_code!=200):
#     print("Error occur while downloading:"+str(res.status_code))
# else:
#     print("File successfully downoladed")
    
#//////////////////////////////
# def getAmazonPrice(productUrl):
#     res=requests.get(productUrl)
#     soup=bs4.BeautifulSoup(res.text,'html.parser')
#     element=soup.select("div[id='side1'] div div div div div:nth-child(3) span")
#     return element[0].text.strip()

# bookPrice=getAmazonPrice("https://www.abebooks.com/9781593275990/Automate-Boring-Stuff-Python-Practical-1593275994/plp")
# print("The price of book is:"+str(bookPrice))


#////////////////////////////
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Firefox()
driver.get("https://www.abebooks.com/9781593275990/Automate-Boring-Stuff-Python-Practical-1593275994/plp")
driver.find_element(By.CSS_SELECTOR,"input[id='header-searchbox-input']").send_keys("Automation")
element=driver.find_element(By.CSS_SELECTOR,"div[id='side1'] div div div div div:nth-child(3) span")
print("Book price is : "+element.text)
driver.close()