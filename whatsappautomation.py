import openpyxl as excel
from time import sleep
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import datetime
import tkinterwhatsapp
from tkinterwhatsapp import contactlist,image,document,inputmessage,imb,docb,sendmessb,sendmessrandb,sendmesspersonalb
moblie_no_list = []


file = excel.load_workbook(contactlist)
sheet = file.active
firstCol = sheet['A']
for cell in range(len(firstCol)):
    contact = str(firstCol[cell].value)
    contact="91"+contact
    #print(contact)
    c1=contact[0:12]
    if(len(c1)==12):
        moblie_no_list.append(c1)
# get mobile no from excel file file
print(moblie_no_list)

def timescheduling():
    
    hour=datetime.datetime.now().hour
    if(hour >= 5 and hour <= 11):
            text="goodmorning"
    elif (hour >= 21 and hour <= 23):
            text="goodnight"
    else:  # At any other time schedule this.
            text="how are you?"
    return text        

def imaged(im):
    clipButton = driver.find_element_by_xpath('//*[@id="main"]/header/div[3]/div/div[2]/div/span')
    clipButton.click()
    sleep(2)
    driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[1]/div[4]/div[1]/header[1]/div[3]/div[1]/div[2]/span[1]/div[1]/div[1]/ul[1]/li[1]/button[1]/input[1]").send_keys(im)
    sleep(3)
    whatsapp_send_button = driver.find_element_by_xpath('/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[2]/span[1]/div[1]/span[1]/div[1]/div[1]/div[2]/span[1]/div[1]/div[1]/span[1]')
    sleep(2)
    whatsapp_send_button.click()
    sleep(3)
    
def documentd(doc):
    clipButton = driver.find_element_by_xpath('//*[@id="main"]/header/div[3]/div/div[2]/div/span')
    clipButton.click()
    sleep(2)
    driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[1]/div[4]/div[1]/header[1]/div[3]/div[1]/div[2]/span[1]/div[1]/div[1]/ul[1]/li[3]/button[1]/input[1]").send_keys(doc)    
    sleep(3)
    whatsapp_send_button = driver.find_element_by_xpath('/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[2]/span[1]/div[1]/span[1]/div[1]/div[1]/div[2]/span[1]/div[1]/div[1]/span[1]')
    sleep(2)
    whatsapp_send_button.click()
    #print("3")
    sleep(3)

def element_presence(by, xpath, time):
    element_present = EC.presence_of_element_located((By.XPATH, xpath))
    WebDriverWait(driver, time).until(element_present)
    
def send_whatsapp_msg(moblie_no,image,document,inputmessage,imb,docb,sendmessb,sendmesspersonalb,sendmessrandb):


    driver.get(
        "https://web.whatsapp.com/send?phone={}&source=&data=#".format(moblie_no)
    )

    try:
        driver.switch_to_alert().accept()
    except Exception as e:
        pass
    if(sendmessb==1):
        element_presence(
             By.XPATH,
               '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]',
             30)
        txt_box = driver.find_element(
        By.XPATH, '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
    
        txt_box.send_keys(inputmessage)
        txt_box.send_keys("\n")
    if(imb==1):
        imaged(image)
    sleep(2)
    if(docb==1):
        documentd(document)
        

if(sendmessb==1 and sendmessrandb==1):
    inputmessage=timescheduling()
driver = webdriver.Chrome('D:\chromedriver')
driver.get("http://web.whatsapp.com")
sleep(10)
for moblie_no in moblie_no_list:
    try:
        send_whatsapp_msg(moblie_no,image,document,inputmessage,imb,docb,sendmessb,sendmesspersonalb,sendmessrandb)
    except Exception as e:
        sleep(10)
print("Task completed")
driver.quit()
    
